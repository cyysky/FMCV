import cv2
import copy
import traceback
from datetime import datetime

from PySide6 import QtCore
from FMCV.UI.QCV import cv_to_pixmap,validate
from PySide6.QtCore import Qt,Slot

from shiboken6 import isValid

from FMCV import Setting
import os

roi = None
image = None


_zoom = 0

Program = None
Handle = None

import pyperclip3
import webbrowser

def set_widget(widget,program,handle):
    global roi,Program,Handle
    roi = widget
    Program = program
    Handle = handle
    #roi.graphicsView.mousePressEvent = mouse_click_event
    # roi.graphicsView.mouseMoveEvent = mouse_move_event
    # roi.graphicsView.mouseReleaseEvent = mouse_release_event 
    # roi.graphicsView.wheelEvent = wheelEvent
    #roi.image.mousePressEvent = scene_press_event
    roi.resizeEvent = update_image
    roi.changeEvent = changeEvent
    
    roi.save_imageButton.clicked.connect(save_image)
    roi.save_roiButton.clicked.connect(save_roi_image)
    roi.clipboardButton.clicked.connect(get_points)
    roi.cameraButton.clicked.connect(get_camera_image)
    roi.file_explorerButton.clicked.connect(open_file_explorer)
    roi.comboBox.clear()
    for i,cam in enumerate(Program.Camera.cams):
        roi.comboBox.addItems(str(i))

def changeEvent(event):
    if event.type() == QtCore.QEvent.WindowStateChange:
        if event.oldState() and Qt.WindowMinimized:
            update_image(event)
        elif event.oldState() == Qt.WindowNoState or roi.windowState() == Qt.WindowMaximized:
            update_image(event)

def open_file_explorer():
    dir = Setting.global_setting['prog_dir']    
    os.makedirs(os.path.join(dir,"images"), exist_ok=True)
    webbrowser.open(os.path.join(dir,"images"))
    
#https://stackoverflow.com/questions/4563272/how-to-convert-a-utc-datetime-to-a-local-datetime-using-only-standard-library
#def utc_to_local(utc_dt):
#    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)   
    
def get_camera_image():
    try:
        set_image(Program.Camera.get_images()[int(roi.comboBox.currentText())])
    except:
        traceback.print_exc()
    
def get_points():
    global roi,image
    x1,y1,x2,y2 = roi.image.get_points()
    roi.label.setText("ROI x1={} y2={} x2={} y={}".format(x1,y1,x2,y2))
    pyperclip3.copy("({},{},{},{})".format(x1,y1,x2,y2))
    
def set_image(cv_img=None):
    global roi,image
    if cv_img is not None:
        image = cv_img
    if isValid(roi) and roi is not None:
        roi.image.clear()
        roi.image.addPixmap(cv_to_pixmap(cv_img))
        roi.graphicsView.fitInView(roi.image.sceneRect(), Qt.KeepAspectRatio) 

def save_image_AI(pth):
    global roi,image,Handle
    try:
        print(pth)
        dir = Setting.global_setting['prog_dir']    
        os.makedirs(os.path.join(dir,"AI"), exist_ok=True)
        val = cv2.imwrite(pth,image)
        print(val)
        Handle.msg(str(val))
    except:
        traceback.print_exc() 
        Handle.msg(traceback.format_exc())
        
def save_roi_image_AI(pth):
    global roi,image,Handle
    try:
        print(pth)
        im = copy.deepcopy(image)
        x1,y1,x2,y2 = roi.image.get_points()
        im_crop = im[y1:y2, x1:x2] 
        dir = Setting.global_setting['prog_dir']        
        val = cv2.imwrite(pth,im_crop)
        print(val)
        Handle.msg(str(val))        
    except:
        traceback.print_exc() 
        Handle.msg(traceback.format_exc())
        
def save_image():
    global roi,image,Handle
    try:
        dir = Setting.global_setting['prog_dir']    
        os.makedirs(os.path.join(dir,"images"), exist_ok=True)
        val = cv2.imwrite(os.path.join(dir,"images",roi.lineEdit.text()),image)
        print(val)
        Handle.msg(str(val))
    except:
        traceback.print_exc() 
        Handle.msg(traceback.format_exc())

def save_roi_image():
    global roi,image,Handle
    try:
        im = copy.deepcopy(image)
        x1,y1,x2,y2 = roi.image.get_points()
        im_crop = im[y1:y2, x1:x2] 
        dir = Setting.global_setting['prog_dir']    
        os.makedirs(os.path.join(dir,"images"), exist_ok=True)
        val = cv2.imwrite(os.path.join(dir,"images",roi.lineEdit.text()),im_crop)
        print(val)
        Handle.msg(str(val))
    except:
        traceback.print_exc() 
        Handle.msg(traceback.format_exc())
    # result = re.match('[a-zA-Z][_a-zA-Z0-9]+$', window.lineEdit.text())

@Slot()
def wheelEvent(event):
    global roi,image,_zoom
    print(event)
    print(event.angleDelta().y())
    if event.angleDelta().y() > 0:
        factor = 1.05
        _zoom += 1
    else:
        factor = 0.95
        _zoom -= 1
    if _zoom > 0:
        roi.graphicsView.scale(factor, factor)
    elif _zoom == 0:
        roi.graphicsView.self.fitInView()
    else:
        if _zoom > -10:
            roi.graphicsView.scale(factor, factor)
        else:
            roi.graphicsView._zoom = -10
            
@Slot()
def scene_press_event(event):
    print(event.scenePos())
   
@Slot()   
def update_image(event):
    #print(event.size())
    global roi,image    
    if validate(image,roi):
        roi.image.clear()
        roi.image.addPixmap(cv_to_pixmap(image))
        roi.graphicsView.fitInView(roi.image.sceneRect(), Qt.KeepAspectRatio)     
    
@Slot()       
def mouse_click_event(event):
    print(event.type())
    print(event)  
    print(vars(event))
    print(event.x())
    print(event.y())
    print(event.localPos())
    print(event.screenPos())
    
@Slot()  
def mouse_move_event(event):
    print(event.type())
    print(event)  
    print(vars(event))
    print(event.x())
    print(event.y())
    print(event.localPos())
    print(event.screenPos())
       
@Slot()  
def mouse_release_event(event):
    print(event.type())
    print(event)
    print(vars(event))
    print(event.x())
    print(event.y())
    print(event.localPos())
    print(event.screenPos())
                