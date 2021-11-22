from os.path import join
import cv2

import traceback

Message = None
prog_dir = None

def get_image(filename,*args, **kwargs):
    print(join(prog_dir,"images",filename))
    return cv2.imread(join(prog_dir,"images",filename),*args, **kwargs)

def msg(text):
    if Message is not None:
        Message.appendPlainText(str(text))

def debug_msg():
    msg(traceback.format_exc())

step_count = 1
displays = {}
results = []
steper = ()

last_results = []

def reset():
    global step_count,displays,results,steper,last_results
    step_count = 1
    displays = {}
    results = []
    steper = ()
    last_results = []

def reset_step_count():
    global step_count
    step_count = 1

def refresh():
    global step_count,last_results,results
    if step_count > len(steper):
        step_count = 1
        last_results = results
        results = []