from PySide6.QtCore import Slot, Qt, QRect, QSize
from PySide6.QtGui import QColor, QFont, QFontDatabase, QPainter, QTextFormat, QSyntaxHighlighter, QTextCharFormat
from PySide6.QtWidgets import QPlainTextEdit, QWidget, QTextEdit
from PySide6 import QtCore, QtWidgets, QtGui

from FMCV.UI.CodeEditor import Ui_TextEditor
import re

#from FMCV import Handle #cython cannot accept recrusive import

class Editor(QPlainTextEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def keyPressEvent(self, oEvent):
        if oEvent.key() == Qt.Key_Tab:
            oEvent = QtGui.QKeyEvent (QtCore.QEvent.KeyPress
                , Qt.Key_Space
                , Qt.KeyboardModifiers(oEvent.nativeModifiers())
                , "    ")
        super().keyPressEvent(oEvent)
        
class Highlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        QSyntaxHighlighter.__init__(self, parent)

        self._mappings = {}

    def add_mapping(self, pattern, format):
        self._mappings[pattern] = format

    def highlightBlock(self, text):
        for pattern, format in self._mappings.items():
            for match in re.finditer(pattern, text):
                start, end = match.span()
                self.setFormat(start, end - start, format)
                
class LineNumberArea(QtWidgets.QWidget):
    def __init__(self, editor):
        QtWidgets.QWidget.__init__(self, editor)
        self._code_editor = editor

    def sizeHint(self):
        return QSize(self._code_editor.line_number_area_width(), 0)

    def paintEvent(self, event):
        self._code_editor.lineNumberAreaPaintEvent(event)

class CodeEditor(QtWidgets.QWidget,Ui_TextEditor):
    def __init__(self, Handle,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self) 
        self.Handle = Handle
        
        #Replacement of keyPressEvent, Patch for not working if put keyPressEvent here
        temporary_editor = Editor(self) ### Going to learn what happen to self mechanism 
        self.horizontalLayout.replaceWidget(self.textEdit,temporary_editor)
        del self.textEdit
        self.textEdit = temporary_editor

        self.saveButton.clicked.connect(self.save_file_pth)        
        self.textEdit.line_number_area = LineNumberArea(self)
        
        self.textEdit.blockCountChanged[int].connect(self.update_line_number_area_width)
        self.textEdit.updateRequest[QRect, int].connect(self.update_line_number_area)
        self.textEdit.cursorPositionChanged.connect(self.highlight_current_line)
        #self.textEdit.keyPressEvent = self.key_event
        self.update_line_number_area_width(0)
        self.highlight_current_line()
        
        self._highlighter = Highlighter()
        self.setup_editor()

        self.run_stepButton.clicked.connect(self.Handle.run_step)
        self.run_allButton.clicked.connect(self.Handle.run_all_step)
        
        
    def set_file_pth(self,pth):
        self.pth = pth
        with open(pth) as f:
             self.textEdit.setPlainText(f.read())
             
    def save_file_pth(self):
        with open(self.pth,"w") as f:
            f.write(self.textEdit.toPlainText())
        self.Handle.refresh_step()
    
            
    def setup_editor(self):
        class_format = QTextCharFormat()
        class_format.setFontWeight(QFont.Bold)
        class_format.setForeground(Qt.blue)
        pattern = r'^\s*class\s+\w+\(.*$'
        self._highlighter.add_mapping(pattern, class_format)

        function_format = QTextCharFormat()
        function_format.setFontItalic(True)
        function_format.setForeground(Qt.blue)
        pattern = r'^\s*def\s+\w+\s*\(.*\)\s*:\s*$'
        self._highlighter.add_mapping(pattern, function_format)

        comment_format = QTextCharFormat()
        comment_format.setBackground(QColor("#77ff77"))
        self._highlighter.add_mapping(r'^\s*#.*$', comment_format)

        font = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        #self._editor = QPlainTextEdit()
        self.textEdit.setFont(font)
        self._highlighter.setDocument(self.textEdit.document()) 
    
    
    def line_number_area_width(self):
        digits = 1
        max_num = max(1, self.textEdit.blockCount())
        while max_num >= 10:
            max_num *= 0.1
            digits += 1

        space = 3 + self.textEdit.fontMetrics().horizontalAdvance('9') * digits
        return space

    def resizeEvent(self, e):
        super().resizeEvent(e)
        cr = self.textEdit.contentsRect()
        width = self.line_number_area_width()
        rect = QRect(cr.left(), cr.top(), width, cr.height())
        self.textEdit.line_number_area.setGeometry(rect)
        
    def lineNumberAreaPaintEvent(self, event):
        painter = QPainter(self.textEdit.line_number_area)
        painter.fillRect(event.rect(), Qt.lightGray)
        block = self.textEdit.firstVisibleBlock()
        block_number = block.blockNumber()
        offset = self.textEdit.contentOffset()
        top = self.textEdit.blockBoundingGeometry(block).translated(offset).top()
        bottom = top + self.textEdit.blockBoundingRect(block).height()

        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                number = str(block_number + 1)
                painter.setPen(Qt.black)
                width = self.textEdit.line_number_area.width()
                height = self.textEdit.fontMetrics().height()
                painter.drawText(0, top, width, height, Qt.AlignRight, number)

            block = block.next()
            top = bottom
            bottom = top + self.textEdit.blockBoundingRect(block).height()
            block_number += 1

    @Slot()
    def update_line_number_area_width(self, newBlockCount):
        self.textEdit.setViewportMargins(self.line_number_area_width(), 0, 0, 0)

    @Slot()
    def update_line_number_area(self, rect, dy):
        if dy:
            self.textEdit.line_number_area.scroll(0, dy)
        else:
            width = self.textEdit.line_number_area.width()
            self.textEdit.line_number_area.update(0, rect.y(), width, rect.height())

        if rect.contains(self.textEdit.viewport().rect()):
            self.update_line_number_area_width(0)

    @Slot()
    def highlight_current_line(self):
        extra_selections = []

        if not self.textEdit.isReadOnly():
            selection = QTextEdit.ExtraSelection()

            line_color = QColor(Qt.yellow).lighter(160)
            selection.format.setBackground(line_color)

            selection.format.setProperty(QTextFormat.FullWidthSelection, True)

            selection.cursor = self.textEdit.textCursor()
            selection.cursor.clearSelection()

            extra_selections.append(selection)

        self.textEdit.setExtraSelections(extra_selections)