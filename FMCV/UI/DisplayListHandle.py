from os.path import join
from datetime import datetime, timezone

from PySide6 import QtCore, QtWidgets, QtGui
from FMCV.UI import DisplayList

from FMCV import Program, Setting, RunStep
from FMCV.UI import DrawRect

class DisplayListWidget(QtWidgets.QWidget,DisplayList.Ui_DisplayList):
    def __init__(self,Handle, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.Handle = Handle
        self.roiButton.clicked.connect(self.Handle.roi_pressed)
        self.first_dircomboBox.currentTextChanged.connect(self.first_dir_selected)

        self.model = QtGui.QStandardItemModel()
        self.listView.setModel(self.model)
        self.listView.clicked[QtCore.QModelIndex].connect(self.on_clicked)
        
        self.itemOldIndex = None
        self.itemOld = QtGui.QStandardItem("text")
        
        self.file_typecomboBox.clear()
        self.file_typecomboBox.addItem("jpg")
        self.file_typecomboBox.addItem("png")
        self.file_typecomboBox.addItem("bmp")
        self.file_typecomboBox.addItem("webp")
        
        self.update_dirButton.clicked.connect(self.update_first_dir)
        self.saveButton.clicked.connect(self.save_image_AI)
        self.save_roiButton.clicked.connect(self.save_roi_image_AI)
        self.file_explorerButton.clicked.connect(self.open_directory)
        self.update_first_dir()
        
        self.images_name_list = [] 
        self.refresh()
        
    def refresh(self):
        self.update_display_list()
    
    def open_directory(self):   
        self.Handle.open_file_explorer(self.get_selected_dir())
        
    def get_selected(self):
        return self.itemOld.text()
        
    def get_selected_dir(self):
        dir = join(Setting.prog_dir(),self.first_dircomboBox.currentText())
        second_dir = self.second_dircomboBox.currentText()
        if second_dir != "":
            dir = join(dir,second_dir)
        return dir
        
    #https://stackoverflow.com/questions/4563272/how-to-convert-a-utc-datetime-to-a-local-datetime-using-only-standard-library
    def utc_to_local(self,utc_dt):
        return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)
    
    def save_image_AI(self):
        filename = self.lineEdit.text()
        print(filename)

        if filename == "":
            filename = self.utc_to_local(datetime.utcnow()).strftime('%Y-%m-%d_%H%M%S_%f')[:-3]
            print(filename)
        filename = filename+"."+self.file_typecomboBox.currentText()
        pth = join(self.get_selected_dir(),filename)
        DrawRect.save_image_AI(pth)
        
    def save_roi_image_AI(self):
        filename = self.lineEdit.text()
        print(filename)
        if filename == "":
            filename = self.utc_to_local(datetime.utcnow()).strftime('%Y-%m-%d_%H%M%S_%f')[:-3]
            print(filename)
        filename = filename+"."+self.file_typecomboBox.currentText()
        pth = join(self.get_selected_dir(),filename)
        DrawRect.save_roi_image_AI(pth)
        
    def update_display_list(self):
        name_list = RunStep.displays.keys()    
        if self.images_name_list != name_list:
            self.images_name_list = name_list
            self.model.clear()
        
            for name in name_list:
                item = QtGui.QStandardItem(name)
                self.model.appendRow(item)
           
        # print(self.itemOldIndex )
        # if len(images_name_list) > 0 and self.itemOldIndex is not None:
           # item = self.model.itemFromIndex(self.itemOldIndex) 
           # item.setForeground(QtGui.QBrush(QtGui.QColor(0, 0, 255))) 
    
    #https://stackoverflow.com/questions/52040538/get-selected-index-in-qlistview-using-qstandarditemmodel
    def on_clicked(self, index):
        self.itemOldIndex = index
        item = self.model.itemFromIndex(index)
        #self.label.setText("on_clicked: itemIndex=`{}`, itemText=`{}`"
        #                   "".format(item.index().row(), item.text()))
        item.setForeground(QtGui.QBrush(QtGui.QColor(0, 0, 255))) 
        self.itemOld.setForeground(QtGui.QBrush(QtGui.QColor(0, 0, 0))) 
        self.itemOld = item
        img = RunStep.displays.get(item.text())        
        if img is not None:
            DrawRect.set_image(img)
            #self.Handle.view()
            
    def update_first_dir(self):
        self.label.setText(Setting.prog_name())
        self.first_dircomboBox.clear()
        self.first_dircomboBox.addItems(Setting.list_prog_dir())
    
    def first_dir_selected(self, text):
        #print(self.first_dircomboBox.count())
        self.second_dircomboBox.clear()
        self.second_dircomboBox.addItems(Setting.list_dir(Setting.prog_dir(),self.first_dircomboBox.currentText()))
        
        