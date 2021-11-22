import traceback
import importlib
from os.path import join,isfile,dirname
import os
from FMCV import Setting
import cv2
import sys

Camera = None
Step = None
Handle = None

def refresh():
    global Step, Camera
    try:
        print("refreshing program: {}".format(Setting.prog_name())) 
        camera_handle_pth = join(Setting.global_setting['prog_root'],"CameraHandle.py")
        if not isfile(camera_handle_pth):
            os.makedirs(dirname(camera_handle_pth), exist_ok=True)
            f = open(camera_handle_pth, "w")
            with open(join(Setting.cwd,"FMCV","CameraHandle"),"r") as cf:
                content = cf.read()
            f.write(content)
            f.close() 
        
        camera_pth = join(Setting.global_setting['prog_dir'],"Camera.py")
        if not isfile(camera_pth):
            os.makedirs(dirname(camera_pth), exist_ok=True)
            f = open(camera_pth, "w")
            with open(join(Setting.cwd,"FMCV","Camera"),"r") as cf:
                content = cf.read()
            f.write(content)
            f.close() 
            
        step_pth = join(Setting.global_setting['prog_dir'],"Step.py")
        if not isfile(step_pth):
            os.makedirs(dirname(step_pth), exist_ok=True)
            f = open(step_pth, "w")
            with open(join(Setting.cwd,"FMCV","Step"),"r") as cf:
                content = cf.read()
            f.write(content)
            f.close()   
        
        exec("import PROG".format(Setting.prog_name()))
        if "PROG.{}.Camera".format(Setting.prog_name()) in sys.modules:            
            exec("importlib.reload(PROG.{}.Camera)".format(Setting.prog_name()))
        else:
            exec("import PROG.{}.Camera".format(Setting.prog_name()))
            
        if "PROG.{}.Step".format(Setting.prog_name()) in sys.modules:      
            exec("importlib.reload(PROG.{}.Step)".format(Setting.prog_name()))
        else:
            exec("import PROG.{}.Step".format(Setting.prog_name()))    
            
        Camera = eval("PROG.{}.Camera".format(Setting.prog_name()))
        Step = eval("PROG.{}.Step".format(Setting.prog_name())) 
        
    except:
        traceback.print_exc() 
        if Handle is not None:
            Handle.window.plainTextEdit.appendPlainText(traceback.format_exc())
        
        
def change_prog(prog_name):
    global Step, Camera
    Setting.prog_update(prog_name)
    refresh()

def add_prog(prog_name):
    Setting.prog_update(prog_name)
    change_prog(prog_name)
    
