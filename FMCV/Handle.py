import ctypes

from ctypes import wintypes
lpBuffer = wintypes.LPWSTR()
AppUserModelID = ctypes.windll.shell32.GetCurrentProcessExplicitAppUserModelID
AppUserModelID(ctypes.cast(ctypes.byref(lpBuffer), wintypes.LPWSTR))
appid = lpBuffer.value
ctypes.windll.kernel32.LocalFree(lpBuffer)
if appid is not None:
    print(appid)
    
import os
import sys
self = sys.modules[__name__]

import importlib

import re

import webbrowser

from FMCV.UI.QCV import cv_to_pixmap,validate
from FMCV.UI.Component import ROISelector,MainWindow
from FMCV.UI import DrawRect,ImageViewerHandle,CodeEditorHandle,DisplayListHandle

from PySide6 import QtWidgets
from PySide6 import QtCore
from PySide6 import QtGui
from PySide6.QtCore import Qt

from shiboken6 import isValid

from FMCV import Program
from FMCV import Setting
from FMCV import RunStep
from FMCV.Setting import get_icon_pth

roi = None
editor = None
display = None


from FMCV.UI.FMCV import FMCV_SPLASH_LOGO

def run():    
    app = QtWidgets.QApplication(sys.argv)  
    image_QImage = QtGui.QImage()
    image_QByteArr = QtCore.QByteArray.fromBase64(FMCV_SPLASH_LOGO)
    image_QImage.loadFromData(image_QByteArr, 'PNG' )
    image_QPixmap = QtGui.QPixmap.fromImage(image_QImage)
    splash = QtWidgets.QSplashScreen(QtGui.QPixmap(image_QPixmap),QtCore.Qt.WindowStaysOnTopHint)
    splash.show()      
    window = MainWindow()   
    window_setup_handle(window)
    
    Program.Handle = self
    RunStep.Message = window.plainTextEdit
    RunStep.prog_dir = Setting.prog_dir()
    Program.refresh() # Start FMCV
    
    window.show()
    splash.close()
    window.activateWindow()
    window.raise_()
    sys.exit(app.exec())
  
def window_setup_handle(win):
    global window
    window = win
    
    #Menubar
    window.actionExit.triggered.connect(window.close)
    window.actionRun_Single_Step.triggered.connect(run_step)
    window.actionRun_All_Step.triggered.connect(run_all_step)
    window.actionReload_Program.triggered.connect(refresh_step)
    window.actionEdit_Step.triggered.connect(edit_step)
    window.actionView_Images.triggered.connect(view)
    window.actionOpen_Program_Folder.triggered.connect(lambda x : open_file_explorer(None,x))
    
    #Action toolbar
    window.actionToolBar.playAction.triggered.connect(run_step)
    window.actionToolBar.playAllAction.triggered.connect(run_all_step)
    window.actionToolBar.viewImageAction.triggered.connect(view)
    window.actionToolBar.roiAction.triggered.connect(roi_pressed)
    window.actionToolBar.displayListAction.triggered.connect(display_list)
    window.actionToolBar.reloadAction.triggered.connect(refresh_step)
    window.actionToolBar.reloadAndRunOnceAction.triggered.connect(reload_run_step)
    window.actionToolBar.reloadAndRunAllAction.triggered.connect(reload_run_all_step)


    #Buttons
    window.addButton.clicked.connect(add_prog)
    #window.horizontalSlider.valueChanged[int].connect(slider_value) #valueChanged signal    
    window.refresh_stepButton.clicked.connect(refresh_step)   
    window.clear_msgButton.clicked.connect(window.plainTextEdit.clear)
    
    #Combobox
    window.prog_nameComboBox.clear()
    window.prog_nameComboBox.addItems(Setting.get_prog_list())    
    i = window.prog_nameComboBox.findText(Setting.prog_name())
    window.prog_nameComboBox.setCurrentIndex(i)    
    
    #Label
    window.label.setText("Selected Program: {}".format(Setting.global_setting['prog_name']))
    
    #Window
    window.setWindowIcon(QtGui.QIcon(get_icon_pth('camera.png')))
    window.statusbar.showMessage("Hello World!")
    
    #Timer
    display_timer()
    
def open_file_explorer(dir, *args, **kwargs):
    if dir is not None:
        webbrowser.open(dir)
    else:
        dir = Setting.prog_dir()
        print(dir)
        os.makedirs(os.path.join(dir), exist_ok=True)
        webbrowser.open(os.path.join(dir))
    
def msg(txt):
    window.plainTextEdit.appendPlainText(txt)

def print_selected(event):
    print(event)

def display_frame():
    global window
    frames = Program.Camera.get_images()
    if len(frames)>0:
        #https://qiita.com/mktshhr/items/f2871b749c8df5b7e0cb
        #bytePerLine = frame.strides[0] # ⇒ 3*width相当
        window.image_1.clear()
        window.image_1.addPixmap(cv_to_pixmap(frames[0]))
        window.graphicsView.fitInView(window.image_1.sceneRect(), Qt.KeepAspectRatio) 
        
def display_timer():
    global timer
    timer = QtCore.QTimer()
    timer.timeout.connect(display_frame)
    #timer.start(60)

def add_prog():
    global window
    result = re.match('[a-zA-Z][_a-zA-Z0-9]+$', window.lineEdit.text())
    if result is not None:
        Program.add_prog(result.group(0))
        window.prog_nameComboBox.clear()
        window.prog_nameComboBox.addItems(Setting.get_prog_list())
        i = window.prog_nameComboBox.findText(Setting.prog_name())
        window.prog_nameComboBox.setCurrentIndex(i)
        window.label.setText("Selected Program: {}".format(Setting.global_setting['prog_name']))
    else:
        print("Program name must start with Alphabet and follow with Underscore or Alphanumeric")

def slider_value(val):
    print(val)  

def reload_run_step():
    refresh_step()
    run_step()

def reload_run_all_step():
    refresh_step()
    run_all_step()   
    
def run_step():    
    Program.Step.run(Program.Camera.get_images())
    RunStep.refresh()
    view()
    if display is not None and isValid(display):
        display.refresh()   

def run_all_step(): 
    for i in range(RunStep.step_count, len(RunStep.steper) + 1):
        Program.Step.run(Program.Camera.get_images())
    RunStep.refresh()
    view()
    if display is not None and isValid(display):
        display.refresh()     
    
def roi_pressed():
    global window,roi,roi_win
  
    if not isValid(roi) or roi is None:
        
        roi = ROISelector(window) 
        
        DrawRect.set_widget(roi,Program,self)
        #DrawRect.set_image(Program.Camera.get_images()[0])
        roi_win = QtWidgets.QMdiSubWindow()
        roi_win.setWidget(roi)
        roi_win.setAttribute(Qt.WA_DeleteOnClose)
        roi_win.setWindowIcon(QtGui.QIcon(get_icon_pth('computer--pencil.png'))) #setIcon
        
        window.mdiArea.addSubWindow(roi_win)               
        roi_win.show()
        roi_win.resize(368,274)
  
def edit_step():
    global window, editor, editor_win

    if editor is None or not isValid(editor):
        editor_win = QtWidgets.QMdiSubWindow()
        editor = CodeEditorHandle.CodeEditor(self) 
        editor.Handle = self
        editor.set_file_pth(os.path.join(Setting.global_setting['prog_dir'],"Step.py"))
        editor_win.setWidget(editor)
        editor_win.setAttribute(Qt.WA_DeleteOnClose)
        editor_win.setWindowIcon(QtGui.QIcon(get_icon_pth('computer--pencil.png'))) #setIcon
        editor_win.resize(int(window.mdiArea.frameGeometry().width()/2),window.mdiArea.frameGeometry().height())
        window.mdiArea.addSubWindow(editor_win)   
        editor_win.show()

def display_list():
    global window, display_win, display
    
    if display is None or not isValid(display):    
        display = DisplayListHandle.DisplayListWidget(self,window)        
        display_win = QtWidgets.QMdiSubWindow()
        display_win.setWidget(display)
        display_win.setAttribute(Qt.WA_DeleteOnClose)
        display_win.setWindowIcon(QtGui.QIcon(get_icon_pth('images-stack.png')))
        
        window.mdiArea.addSubWindow(display_win)   
        display_win.show()
        display_win.resize(300,500)



def refresh_step():
    global window, editor, editor_win, display
    #Get selected prog_name
    selected_prog_name = window.prog_nameComboBox.currentText()
    #Compare is prog_name changed
    same = Setting.compare_last_prog_name(selected_prog_name)
    #reset run RunStep import by Program.Step
    RunStep.reset()

    #Refresh Program.Step and Program.Camera with new Setting
    Program.change_prog(selected_prog_name)
    RunStep.prog_dir = Setting.prog_dir()
    
    try:
        if not same:
            Program.Step.AI.reset()
    except:
        print("Step no loaded AI")
    
    if editor is not None and isValid(editor):
        editor.set_file_pth(os.path.join(Setting.global_setting['prog_dir'],"Step.py"))
    
    if display is not None and isValid(display):
        display.refresh()     
    
    window.prog_nameComboBox.clear()
    window.prog_nameComboBox.addItems(Setting.get_prog_list())
    i = window.prog_nameComboBox.findText(Setting.prog_name())
    window.prog_nameComboBox.setCurrentIndex(i)
    window.label.setText("Selected Program: {}".format(Setting.global_setting['prog_name']))

IVs = {}
def view(): 
    global window,IVs,display 
    window.statusbar.showMessage("{}".format(RunStep.step_count))
    for k,v in RunStep.displays.items():
        if IVs.get(k) is None or not isValid(IVs.get(k)):  
            IV = QtWidgets.QMdiSubWindow()
            IV.setWidget(ImageViewerHandle.ImageViewer(window))
            IV.setAttribute(Qt.WA_DeleteOnClose)
            IV.setWindowIcon(QtGui.QIcon(get_icon_pth('picture.png')))
            IV.resize(320,240)
            IV.setWindowTitle(k)
            IV.widget().set_image(v)
            IVs[k] = IV
            window.mdiArea.addSubWindow(IVs[k])
            IVs[k].show()
            IV.widget().refresh()
        else:
            IVs[k].widget().set_image(v)
            if display is not None and isValid(display):
                img = RunStep.displays.get(display.get_selected())        
                if img is not None:
                    DrawRect.set_image(img)

    
