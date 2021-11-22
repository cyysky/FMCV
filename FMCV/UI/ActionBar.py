from PySide6 import QtCore
from PySide6 import QtGui 
from PySide6 import QtWidgets

from FMCV.Setting import get_icon_pth

#https://zetcode.com/gui/pysidetutorial/menusandtoolbars/
class Ui_ActionBar(object):
    def setupUi(self, ActionBar):
        if not ActionBar.objectName():
            ActionBar.setObjectName(u"ActionBar")
        
        # self.exitAction = QtGui.QAction('Exit', self)
        # self.exitAction.setShortcut('Ctrl+Q')
        # self.exitAction.setStatusTip('Exit application')
        
        # self.addAction(self.exitAction) 
        
        # self.saveStepAction = QtGui.QAction(QtGui.QIcon(get_icon_pth('disk.png')), 'Save Step') #setIcon
        # self.saveStepAction.setStatusTip('Save Program Steps')
        
        # self.addAction(self.saveStepAction)
        
        # self.editStepAction = QtGui.QAction(QtGui.QIcon(get_icon_pth('computer--pencil.png')), 'Edit Step') #setIcon
        # self.editStepAction.setStatusTip('Edit Program Steps')
        
        # self.addAction(self.editStepAction)
        
        self.displayListAction = QtGui.QAction(QtGui.QIcon(get_icon_pth('images-stack.png')), 'Display List') #setIcon
        self.displayListAction.setStatusTip('Steps Images Display List')
        
        self.addAction(self.displayListAction)
        
        self.viewImageAction = QtGui.QAction(QtGui.QIcon(get_icon_pth('picture.png')), 'View Images') #setIcon
        self.viewImageAction.setStatusTip('View Steps Images')
        
        self.addAction(self.viewImageAction)
        
        self.roiAction = QtGui.QAction(QtGui.QIcon(get_icon_pth('image-select.png')), 'ROI') #setIcon
        self.roiAction.setStatusTip('ROI Tool')
        
        self.addAction(self.roiAction)
        
        self.reloadAction = QtGui.QAction(QtGui.QIcon(get_icon_pth('arrow-circle-045-left.png')), 'Reload Program') #setIcon
        self.reloadAction.setStatusTip('Reload Program Steps')
        
        self.addAction(self.reloadAction)
        
        self.reloadAndRunOnceAction = QtGui.QAction(QtGui.QIcon(get_icon_pth('arrow-curve-000-left.png')), 'Reload and Run 1 step') 
        self.reloadAndRunOnceAction.setStatusTip('Reload Program Steps and Run Single Step')
        
        self.addAction(self.reloadAndRunOnceAction)
        
        self.reloadAndRunAllAction = QtGui.QAction(QtGui.QIcon(get_icon_pth('arrow-curve-000-double.png')), 'Reload and Run ALL') 
        self.reloadAndRunAllAction.setStatusTip('Reload Program Steps and Run All Steps')
        
        self.addAction(self.reloadAndRunAllAction)
        
        self.playAction = QtGui.QAction(QtGui.QIcon(get_icon_pth('control.png')), 'Single') #setIcon
        self.playAction.setStatusTip('Single Step')
        
        self.addAction(self.playAction)
        
        self.playAllAction = QtGui.QAction(QtGui.QIcon(get_icon_pth('control-double.png')), 'Run All') #setIcon
        self.playAllAction.setStatusTip('Run All Steps')
        
        self.addAction(self.playAllAction)        
        
        self.retranslateUi(ActionBar)

        QtCore.QMetaObject.connectSlotsByName(ActionBar)
    # setupUi

    def retranslateUi(self, ActionBar):
        ActionBar.setWindowTitle(QtCore.QCoreApplication.translate("ActionBar", u"Title", None))
    # retranslateUi