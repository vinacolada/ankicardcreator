from ACCImport import *
from MainWindowGUI import *

def main():
    app = QApplication(sys.argv)
    main_window = ClozeTable()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()