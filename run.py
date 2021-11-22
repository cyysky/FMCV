import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
from FMCV import App
if __name__ == '__main__' :
    App.run()