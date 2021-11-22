from FMCV import Setting

import tensorflow_hub as hub
import tensorflow as tf
import keras

import cv2
import os
import numpy as np
import time
import traceback

import matplotlib.pyplot as plt

FV_DIR = os.path.join(Setting.cwd,'FMCV','TF','FV')

model = None

np.set_printoptions(suppress=True)

def default_model(classes):
    #https://tfhub.dev/google/imagenet/mobilenet_v3_small_100_224/feature_vector/5
    #https://tfhub.dev/google/imagenet/mobilenet_v3_large_075_224/feature_vector/5
    #https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/4
    new_model = tf.keras.Sequential([
     hub.KerasLayer(FV_DIR,
     trainable=False),
     tf.keras.layers.Dense(1280, activation='sigmoid'),  
     tf.keras.layers.Dropout(.2),
     tf.keras.layers.Dense(1280, activation='sigmoid'),
     tf.keras.layers.Dropout(.2),
     tf.keras.layers.Dense(classes, activation='softmax')
    ])
    new_model.build([None, 224, 224, 3])
    print("build model in memory")
    #model.summary()

    new_model.compile(
     optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
     loss=tf.keras.losses.CategoricalCrossentropy(),
     metrics=['acc'])
     
    return new_model

def model_dir():
    return os.path.join(Setting.prog_dir(),"Model")

def reload_model():
    global model
    keras.backend.clear_session()
    model = None
    try:
        if os.path.exists(model_dir()):
            print("loading model {}".format(model_dir()))
            model = tf.keras.models.load_model(model_dir())
            #model.summary()
        else:
            print("{} Not Found".format(model_dir()))
    except:
        traceback.print_exc()

def predict(im): #image size (224,224)  
    global model
    if model is None:
        reload_model()
    if model is not None:        
        start = time.time()
        im = np.expand_dims(im, axis=0)
        score = model.predict(im)
        score = score[0]
        #print(f'{name} {np.argmax(score)} , {np.max(score)},{score} time {time.time() - start}')
        return np.argmax(score)
    else:
        print("Model not loaded")
    return 0
            
def train(epochs): 
    global model
    print(model_dir())
    data_root = os.path.join(Setting.prog_dir(),"AI")
    os.makedirs(os.path.join(Setting.prog_dir(),"AI","0"), exist_ok=True)
    os.makedirs(os.path.join(Setting.prog_dir(),"AI","1"), exist_ok=True)               

    IMAGE_SHAPE = (224,224) 
    TRAINING_DATA_DIR = str(data_root)
    datagen_kwargs = dict(validation_split=.3,rescale=1./255)#rescale=1./255, validation_split=.6)
    #dct_method='INTEGER_ACCURATE'
    valid_datagen = tf.keras.preprocessing.image.ImageDataGenerator(**datagen_kwargs)
    valid_generator = valid_datagen.flow_from_directory(
        TRAINING_DATA_DIR,
        subset="validation",
        shuffle=True,
        target_size=IMAGE_SHAPE        
        )

    datagen_kwargs = dict(rescale=1./255)#rescale=1./255)
    train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(**datagen_kwargs)
    train_generator = train_datagen.flow_from_directory(
        TRAINING_DATA_DIR,
        subset="training",
        shuffle=True,
        target_size=IMAGE_SHAPE
        )

    for image_batch, label_batch in train_generator:
        break
    image_batch.shape, label_batch.shape
    print (train_generator.class_indices) 
    
    if model is None:
        reload_model()
        
    if model is None:
        model = default_model(train_generator.num_classes)
    
    steps_per_epoch = np.ceil(train_generator.samples/train_generator.batch_size)
    val_steps_per_epoch = np.ceil(valid_generator.samples/valid_generator.batch_size)
    hist = model.fit(
     train_generator,
     epochs=epochs,
     verbose=1,
     steps_per_epoch=steps_per_epoch,
     validation_data=valid_generator,
     validation_steps=val_steps_per_epoch).history

    final_loss, final_accuracy = model.evaluate(valid_generator, steps = val_steps_per_epoch)
    print("Final loss: {:.2f}".format(final_loss))
    print("Final accuracy: {:.2f}%".format(final_accuracy * 100))
    
    # Save the weights
    model.save(model_dir())
     
    plt.figure()
    plt.ylabel("Loss (training and validation)")
    plt.xlabel("Training Steps")
    plt.ylim([0,50])
    plt.plot(hist["loss"])
    plt.plot(hist["val_loss"])
    plt.figure()
    plt.ylabel("Accuracy (training and validation)")
    plt.xlabel("Training Steps")
    plt.ylim([0,1])
    plt.plot(hist["acc"])
    plt.plot(hist["val_acc"])

    val_image_batch, val_label_batch = next(iter(train_generator))
    true_label_ids = np.argmax(val_label_batch, axis=-1)
    print("Validation batch shape:", val_image_batch.shape)

    dataset_labels = sorted(train_generator.class_indices.items(), key=lambda pair:pair[1])
    dataset_labels = np.array([key.title() for key, value in dataset_labels])
    print(dataset_labels)

    tf_model_predictions = model.predict(val_image_batch)
    print("Prediction results shape:", tf_model_predictions.shape)
    print(tf_model_predictions)
    predicted_ids = np.argmax(tf_model_predictions, axis=-1)
    predicted_labels = dataset_labels[predicted_ids]
    print(predicted_labels)

    plt.figure(figsize=(10,9))
    plt.subplots_adjust(hspace=0.5)
    for n in range((len(predicted_labels)-2)):
      plt.subplot(6,5,n+1)
      #plt.imshow((val_image_batch[n]).astype(np.uint8))
      plt.imshow(val_image_batch[n])
      # color = "green" if predicted_ids[n] == true_label_ids[n] else "red"
      plt.title("{} {}".format(predicted_labels[n].title(), true_label_ids[n]))
      plt.axis('off')
    _ = plt.suptitle("Model predictions (green: correct, red: incorrect)")

    plt.show()
        