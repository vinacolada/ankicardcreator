from nmimports import *
from ui_NoteMode import Ui_MainWindow
from nmmainwindow import MainWindow


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