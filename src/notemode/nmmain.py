from nmimports import *
from nmui import Ui_MainWindow
from nmmainwindow import MainWindow
from nmaccquestions import *

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.showMaximized()

    main_window = MainWindow()  # Use the MainWindow class
    main_window.showMaximized()
    sys.exit(app.exec_())