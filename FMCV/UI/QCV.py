import cv2
from PySide6.QtGui import QImage, QPixmap
import shiboken6

#https://qiita.com/mktshhr/items/f2871b749c8df5b7e0cb
def cv_to_pixmap(cv_img):
    if len(cv_img.shape)<3:
        frame = cv2.cvtColor(cv_img, cv2.COLOR_GRAY2RGB)
    else:
        frame = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
    h, w = cv_img.shape[:2]
    #qimg = QImage(img.tobytes(), width, height, bytePerLine, QImage.Format.Format_RGB888)
    bytesPerLine = 3 * w
    qimage = QImage(frame.data, w, h, bytesPerLine, QImage.Format.Format_RGB888) 
    #qimage = QImage(frame.flatten(), w, h, QImage.Format_RGB888) # cv::Mat -> Qt(numpy.array)
    pixmap = QPixmap.fromImage(qimage)
    return pixmap
    
def validate(*args):
    valid_count = 0
    for e in args:
        if e is not None and shiboken6.isValid(e):
            valid_count+=1            
            
    return valid_count == len(args)
        