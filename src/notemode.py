# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NoteMode.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(835, 586)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.column1Splitter = QtWidgets.QSplitter(self.centralwidget)
        self.column1Splitter.setGeometry(QtCore.QRect(10, 20, 276, 481))
        self.column1Splitter.setOrientation(QtCore.Qt.Vertical)
        self.column1Splitter.setObjectName("column1Splitter")
        self.tableGroupBox = QtWidgets.QGroupBox(self.column1Splitter)
        self.tableGroupBox.setObjectName("tableGroupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tableGroupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.questionsTableWidget = QtWidgets.QTableWidget(self.tableGroupBox)
        self.questionsTableWidget.setRowCount(1)
        self.questionsTableWidget.setColumnCount(2)
        self.questionsTableWidget.setObjectName("questionsTableWidget")
        self.questionsTableWidget.horizontalHeader().setDefaultSectionSize(75)
        self.questionsTableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_4.addWidget(self.questionsTableWidget, 0, 0, 1, 1)
        self.addQPushButton = QtWidgets.QPushButton(self.column1Splitter)
        self.addQPushButton.setObjectName("addQPushButton")
        self.widget = QtWidgets.QWidget(self.column1Splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.numIDLineEdit = QtWidgets.QLineEdit(self.widget)
        self.numIDLineEdit.setObjectName("numIDLineEdit")
        self.verticalLayout.addWidget(self.numIDLineEdit)
        self.sortLineEdit = QtWidgets.QLineEdit(self.widget)
        self.sortLineEdit.setObjectName("sortLineEdit")
        self.verticalLayout.addWidget(self.sortLineEdit)
        self.column2Splitter = QtWidgets.QSplitter(self.centralwidget)
        self.column2Splitter.setGeometry(QtCore.QRect(300, 20, 361, 401))
        self.column2Splitter.setOrientation(QtCore.Qt.Vertical)
        self.column2Splitter.setObjectName("column2Splitter")
        self.titleGroupBox = QtWidgets.QGroupBox(self.column2Splitter)
        self.titleGroupBox.setObjectName("titleGroupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.titleGroupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.titleTextEdit = QtWidgets.QTextEdit(self.titleGroupBox)
        self.titleTextEdit.setObjectName("titleTextEdit")
        self.gridLayout_3.addWidget(self.titleTextEdit, 0, 0, 1, 1)
        self.notesGroupBox = QtWidgets.QGroupBox(self.column2Splitter)
        self.notesGroupBox.setObjectName("notesGroupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.notesGroupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.notesTextEdit = QtWidgets.QTextEdit(self.notesGroupBox)
        self.notesTextEdit.setObjectName("notesTextEdit")
        self.gridLayout_2.addWidget(self.notesTextEdit, 0, 0, 1, 1)
        self.column3Splitter = QtWidgets.QSplitter(self.centralwidget)
        self.column3Splitter.setGeometry(QtCore.QRect(670, 20, 151, 400))
        self.column3Splitter.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.column3Splitter.setOrientation(QtCore.Qt.Vertical)
        self.column3Splitter.setObjectName("column3Splitter")
        self.allNotesGroupBox = QtWidgets.QGroupBox(self.column3Splitter)
        self.allNotesGroupBox.setObjectName("allNotesGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.allNotesGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.allNotesScrollArea = QtWidgets.QScrollArea(self.allNotesGroupBox)
        self.allNotesScrollArea.setWidgetResizable(True)
        self.allNotesScrollArea.setObjectName("allNotesScrollArea")
        self.allNotesScrollAreaWidgetContents = QtWidgets.QWidget()
        self.allNotesScrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 129, 129))
        self.allNotesScrollAreaWidgetContents.setObjectName("allNotesScrollAreaWidgetContents")
        self.allNoteListView = QtWidgets.QListView(self.allNotesScrollAreaWidgetContents)
        self.allNoteListView.setGeometry(QtCore.QRect(0, 0, 141, 211))
        self.allNoteListView.setObjectName("allNoteListView")
        self.allNotesScrollArea.setWidget(self.allNotesScrollAreaWidgetContents)
        self.gridLayout.addWidget(self.allNotesScrollArea, 0, 0, 1, 1)
        self.addNotesButton = QtWidgets.QPushButton(self.column3Splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.addNotesButton.sizePolicy().hasHeightForWidth())
        self.addNotesButton.setSizePolicy(sizePolicy)
        self.addNotesButton.setMaximumSize(QtCore.QSize(50, 50))
        self.addNotesButton.setObjectName("addNotesButton")
        self.topicGroupBox = QtWidgets.QGroupBox(self.column3Splitter)
        self.topicGroupBox.setObjectName("topicGroupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.topicGroupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.topicTextEdit = QtWidgets.QTextEdit(self.topicGroupBox)
        self.topicTextEdit.setObjectName("topicTextEdit")
        self.gridLayout_5.addWidget(self.topicTextEdit, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 835, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuNote = QtWidgets.QMenu(self.menubar)
        self.menuNote.setObjectName("menuNote")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionNew_Cloze = QtWidgets.QAction(MainWindow)
        self.actionNew_Cloze.setObjectName("actionNew_Cloze")
        self.actionSame_Cloze = QtWidgets.QAction(MainWindow)
        self.actionSame_Cloze.setObjectName("actionSame_Cloze")
        self.actionBold = QtWidgets.QAction(MainWindow)
        self.actionBold.setObjectName("actionBold")
        self.actionUnderline = QtWidgets.QAction(MainWindow)
        self.actionUnderline.setObjectName("actionUnderline")
        self.actionItalicize = QtWidgets.QAction(MainWindow)
        self.actionItalicize.setObjectName("actionItalicize")
        self.actionAdd_Note = QtWidgets.QAction(MainWindow)
        self.actionAdd_Note.setObjectName("actionAdd_Note")
        self.actionAdd_Card = QtWidgets.QAction(MainWindow)
        self.actionAdd_Card.setObjectName("actionAdd_Card")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExport)
        self.menuEdit.addAction(self.actionNew_Cloze)
        self.menuEdit.addAction(self.actionSame_Cloze)
        self.menuEdit.addAction(self.actionBold)
        self.menuEdit.addAction(self.actionUnderline)
        self.menuEdit.addAction(self.actionItalicize)
        self.menuNote.addAction(self.actionAdd_Note)
        self.menuNote.addAction(self.actionAdd_Card)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuNote.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tableGroupBox.setTitle(_translate("MainWindow", "Questions"))
        self.addQPushButton.setText(_translate("MainWindow", "+"))
        self.numIDLineEdit.setPlaceholderText(_translate("MainWindow", "Numerical Identifier"))
        self.sortLineEdit.setPlaceholderText(_translate("MainWindow", "Sort Identifier"))
        self.titleGroupBox.setTitle(_translate("MainWindow", "Title"))
        self.notesGroupBox.setTitle(_translate("MainWindow", "Notes"))
        self.allNotesGroupBox.setTitle(_translate("MainWindow", "All Notes"))
        self.addNotesButton.setText(_translate("MainWindow", "Add"))
        self.topicGroupBox.setTitle(_translate("MainWindow", "Topic"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuNote.setTitle(_translate("MainWindow", "Note"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionNew_Cloze.setText(_translate("MainWindow", "New Cloze"))
        self.actionSame_Cloze.setText(_translate("MainWindow", "Same Cloze"))
        self.actionBold.setText(_translate("MainWindow", "Bold"))
        self.actionUnderline.setText(_translate("MainWindow", "Underline"))
        self.actionItalicize.setText(_translate("MainWindow", "Italicize"))
        self.actionAdd_Note.setText(_translate("MainWindow", "Add Note"))
        self.actionAdd_Note.setShortcut(_translate("MainWindow", "Ctrl+M"))
        self.actionAdd_Card.setText(_translate("MainWindow", "Add Card"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
