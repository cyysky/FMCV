from FMCV.UI.Main import Ui_MainWindow
from FMCV.UI.ROISelector import Ui_ROISelector
from FMCV.UI.ActionBar import Ui_ActionBar

from PySide6.QtWidgets import QWidget,QMainWindow,QGraphicsScene

from PySide6.QtCore import QSettings
from PySide6 import QtCore, QtWidgets, QtGui

class ROISelector(QWidget,Ui_ROISelector):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.rubberBand = QtWidgets.QRubberBand(QtWidgets.QRubberBand.Rectangle, self)
        self.image = ROIScene()
        self.graphicsView.setScene(self.image)
        

class ROIScene(QtWidgets.QGraphicsScene):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.begin = QtCore.QPointF()
        self.end = QtCore.QPointF()
        
    def get_points(self):
        x1,y1 = self.begin.toTuple()
        x2,y2 = self.end.toTuple()
        return int(x1),int(y1),int(x2),int(y2)
    
    def drawForeground(self, painter, rect):
        #print(painter)
        #print(rect)

        qp = painter
        br = QtGui.QBrush(QtGui.QColor(100, 10, 10, 0))  
        qp.setBrush(br)   
        
        qp.drawRect(QtCore.QRect(self.begin.toPoint(), self.end.toPoint()))  
   
    def mousePressEvent(self, event):
        self.begin = event.scenePos()
        self.end = event.scenePos()
        print(event.scenePos())
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.scenePos()
        self.update()

    # def mouseReleaseEvent(self, event):
        # self.begin = event.scenePos()
        # self.end = event.scenePos()
        # self.update()
        
class Scene(QGraphicsScene):
    mScene = None
    def __init__(self, parent=None):
        super(Scene, self).__init__()

    def mousePressEvent(self, event):
        #print(event.type())
        p = event.scenePos() # relative to widget
        #print(p)
 
class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.image_1 = Scene("Camera")        
        
        #self.graphicsView.setScene(self.image_1) # 纪念，第一个功能 哈哈哈
        
        self.settings = QSettings('Fortune Machine Computer', 'FMCV')
        self.restoreGeometry(self.settings.value('geometry'))       
        self.restoreState(self.settings.value('state'))
        self.splitter.restoreState(self.settings.value("splitter"))
        self.actionTile_Windows.triggered.connect(self.tile_sub_windows)
        
        self.actionToolBar = ActionBar()
        #self.actionToolBar.exitAction.triggered.connect(self.close)
        toolbar = self.addToolBar(self.actionToolBar)
        
    def tile_sub_windows(self,event):
        self.mdiArea.tileSubWindows()
    
    def closeEvent(self, event):       
        self.settings.setValue('geometry', self.saveGeometry())
        self.settings.setValue('state', self.saveState())
        self.settings.setValue("splitter", self.splitter.saveState())
        super(MainWindow, self).closeEvent(event)  

class ActionBar(QtWidgets.QToolBar,Ui_ActionBar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        