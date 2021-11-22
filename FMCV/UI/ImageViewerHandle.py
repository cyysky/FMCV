from FMCV.UI.QCV import cv_to_pixmap,validate
from PySide6.QtCore import Qt,Slot
from PySide6.QtWidgets import QWidget,QGraphicsScene,QGraphicsView
from FMCV.UI.ImageViewer import Ui_ImageViewer
from PySide6 import QtCore

class ImageViewer(QWidget,Ui_ImageViewer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.scene = QGraphicsScene()
        self.image = None
        self.graphicsView.setScene(self.scene)
        self.graphicsView.wheelEvent = self.wheelEvent
        self.zoom = 0
    
    def refresh(self):
        self.scene.clear()
        self.scene.addPixmap(cv_to_pixmap(self.image))
        self.graphicsView.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio) 
        
    def set_image(self,img):
        self.image = img
        self.scene.clear()
        self.scene.addPixmap(cv_to_pixmap(self.image))
        self.graphicsView.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio) 
        self.graphicsView.setDragMode(QGraphicsView.ScrollHandDrag)
        
    def wheelEvent(self,event):
        if event.angleDelta().y() > 0:
            factor = 1.05
            self.zoom += 1
        else:
            factor = 0.95
            self.zoom -= 1
        if self.zoom > 0:
            self.graphicsView.scale(factor, factor)
        elif self.zoom == 0:
            #self.graphicsView.fitInView() #When scoll image smaller then window frame,TypeError: PySide6.QtWidgets.QGraphicsView.fitInView(): not enough arguments
            pass
        else:
            if self.zoom > -10:
                self.graphicsView.scale(factor, factor)
            else:
                self.graphicsView.zoom = -10
                
    def resizeEvent(self,event):  
        self.refresh()
        
    def changeEvent(self,event):
        if event.type() == QtCore.QEvent.WindowStateChange:
            if event.oldState() and Qt.WindowMinimized:
                self.refresh()
            elif event.oldState() == Qt.WindowNoState or self.windowState() == Qt.WindowMaximized:
                self.refresh()