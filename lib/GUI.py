import sys
import Constants
import CoreModule
from PySide2 import QtCore, QtWidgets
from DroppableListBox import DroppableListBox
from SuperFileDialog import SuperFileDialog

class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setMinimumSize(800, 450)
        self.setAcceptDrops(True)
        self.list_box = DroppableListBox(self)
        self.connect(self.list_box, QtCore.SIGNAL("dropped(object)"), self, QtCore.SLOT("list_box_dropped(object)"))
        self.browse_button = QtWidgets.QPushButton()
        self.browse_button.setText("Browse..")
        self.browse_button.clicked.connect(self.browse_button_click)

        self.layout = QtWidgets.QGridLayout()
        self.layout.setMargin(50)
        self.layout.addWidget(self.list_box, 0, 0, alignment=QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        self.layout.addWidget(self.browse_button, 0, 1, alignment=QtCore.Qt.AlignTop | QtCore.Qt.AlignRight)
        self.layout.setHorizontalSpacing(100)

        self.setLayout(self.layout)
    

    def browse_button_click(self):
        filenames = self.open_file_dialog()
        if (filenames is not None):
            self.list_box.clear()
            for i in range(len(filenames)):
                self.list_box.insertItem(i, filenames[i])
    
    def list_box_dropped(self, paths):
        CoreModule.rename_directories(Constants.default_format, *paths).get()

    def open_file_dialog(self):
        dialog = SuperFileDialog(self)
        if dialog.exec_():
            filenames = dialog.selectedFiles()
            return filenames

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())
