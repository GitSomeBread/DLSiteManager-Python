from PySide2 import QtCore, QtWidgets
import CoreModule

class DroppableListBox(QtWidgets.QListWidget):
    def __init__(self, parent=None):
        super(DroppableListBox, self).__init__(parent)
        self.setMinimumWidth(400)
        self.setMinimumHeight(200)
        self.insertItem(0, "Please Drag & Drop your files here")
        self.setAcceptDrops(True)
    
    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.accept()
        else:
            e.ignore()

    def dragMoveEvent(self, e):
        if e.mimeData().hasUrls():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        e.accept()
        self.clear()
        paths = []
        for url in e.mimeData().urls():
            path = url.toLocalFile()
            paths.append(path)
            self.addItem(path)
        self.emit(QtCore.SIGNAL("dropped(object)"), paths)

