from FMCV.UI.QCV import cv_to_pixmap,validate
from PySide6.QtCore import Qt,Slot
from PySide6.QtWidgets import QWidget,QGraphicsScene,QGraphicsView
from FMCV.UI.SliderWidget import Ui_SliderWidget
from PySide6 import QtCore

class SliderWidget(QWidget,Ui_SliderWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.horizontalSlider.setMaximum(255)
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.valueChanged.connect(self.slider_change)
        
    def slider_change(self,*args, **kwargs):
        v = self.horizontalSlider.value()
        self.label_value.setText(f"Value {v}")
        
    def set_min_max(self,minimum,maximum):
        self.horizontalSlider.setMaximum(maximum)
        self.horizontalSlider.setMinimum(minimum)