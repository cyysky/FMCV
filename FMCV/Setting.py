import os
from os.path import join,isfile,exists,dirname
import importlib
import json
import traceback

cwd = os.getcwd()#;print(cwd)

resd = join(cwd,'FMCV','UI','Resource')

last_prog_name = ""

def compare_last_prog_name(in_prog_name):
    return last_prog_name == in_prog_name

def get_last_prog_name():
    return last_prog_name

def get_icon_pth(icon):
    return join(resd,icon)

def prog_name():
    global global_setting
    return global_setting["prog_name"]

def prog_dir():
    global global_setting
    return global_setting["prog_dir"]

def default_global_setting():
    global_setting = {
                        "prog_name":"STEPS001",
                        "prog_dir":join(cwd,"PROG","STEPS001"),
                        "prog_root":join(cwd,"PROG")
                    }
    return global_setting
    
def default_setting():
    setting = {"camera":"Camera","program":"Program"}
    return setting

def overwrite(pth,dtc):
    if exists(pth):
        os.remove(pth)
    os.makedirs(dirname(pth), exist_ok=True)
    if not isfile(pth):
        with open(pth, "w") as f:       
            f.write(json.dumps(dtc, indent = 4))

def update_setting(pth,dtc,act="r"):
    try:
        os.makedirs(dirname(pth), exist_ok=True)
        if not exists(pth):
            raise Exception('File Not Found') 
        if act == "r":
            with open(pth, "r") as f:
                dtc = json.load(f)
        elif act == "w":
            with open(pth, "w") as f:       
                f.write(json.dumps(dtc, indent = 4))
    except:
        #traceback.print_exc()  
        print("REWRITE SETTING")
        overwrite(pth,dtc)

    return dtc

def prog_update(in_prog_name):
    global global_setting, setting
    global global_setting_pth, setting_pth
    global last_prog_name
    
    last_prog_name = in_prog_name
    
    if global_setting['prog_name'] != in_prog_name:
        global_setting['prog_name'] = in_prog_name
        global_setting['prog_dir'] = join(global_setting['prog_root'],in_prog_name)  
        
        setting_pth = join(global_setting["prog_dir"],"setting.json")  

        update_setting(global_setting_pth, global_setting,"w")
        update_setting(setting_pth, setting,"w")

def get_prog_list():  
    #https://stackoverflow.com/questions/141291/how-to-list-only-top-level-directories-in-python
    return next(os.walk(global_setting["prog_root"]))[1]  

def list_dir(*args):  
    #print(join(*args))
    #https://stackoverflow.com/questions/141291/how-to-list-only-top-level-directories-in-python
    return next(os.walk(join(*args)))[1]  

def list_prog_dir():    
    return list_dir(prog_dir())

#Default Settings
global_setting = default_global_setting()
setting = default_setting()

#Get Global Setting
global_setting_pth = join(global_setting["prog_root"],"setting.json")
global_setting = update_setting(global_setting_pth,global_setting)
last_prog_name = prog_name()


#Get Program Setting
setting_pth = join(global_setting["prog_root"],prog_name(),"setting.json")
setting = update_setting(setting_pth,setting)

