from FMCV.TF import Model
import cv2

def inference(im):
    resized_im = cv2.resize(im, (224,224), interpolation = cv2.INTER_AREA)
    aim = cv2.cvtColor(resized_im, cv2.COLOR_BGR2RGB)
    aim = aim * (1./255)
    return Model.predict(aim)

def train(num):
    return Model.train(num)

def reset():
    Model.reload_model()