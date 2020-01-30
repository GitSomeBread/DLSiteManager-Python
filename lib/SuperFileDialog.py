from PySide2 import QtWidgets

class SuperFileDialog(QtWidgets.QFileDialog):
    def __init__(self, parent=None):
        super(SuperFileDialog, self).__init__(parent)
        self.setFileMode(QtWidgets.QFileDialog.Directory)
        self.setViewMode(QtWidgets.QFileDialog.Detail)
        self.setOption(self.DontUseNativeDialog, True)
        for view in self.findChildren(QtWidgets.QListView) + self.findChildren(QtWidgets.QTreeView):
            if isinstance(view.model(), QtWidgets.QFileSystemModel):
                view.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)