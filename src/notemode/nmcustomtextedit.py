from PyQt5 import QtWidgets, QtGui, QtCore

class CustomTextEdit(QtWidgets.QTextEdit):
    editingFinished = QtCore.pyqtSignal()  # Custom signal

    def __init__(self, parent=None):
        super().__init__(parent)

    def focusOutEvent(self, event):
        self.editingFinished.emit()  # Emit the signal when the text edit loses focus
        super().focusOutEvent(event)  # Call the base class method