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
        MainWindow.resize(1000, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Create the main horizontal layout
        self.mainSplitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal, self.centralwidget)

        # Create the vertical splitters without setting geometry
        self.column1Splitter = QtWidgets.QSplitter(QtCore.Qt.Vertical)
        self.column2Splitter = QtWidgets.QSplitter(QtCore.Qt.Vertical)
        self.column3Splitter = QtWidgets.QSplitter(QtCore.Qt.Vertical)

        # Add the columns to the main splitter
        self.setupFirstColumn()
        self.setupSecondColumn()
        self.setupThirdColumn()

        # Set up the menu bar before calling retranslateUi
        self.setupMenuBar(MainWindow)

        # Add the columns to the main splitter
        self.mainSplitter.addWidget(self.column1Splitter)
        self.mainSplitter.addWidget(self.column2Splitter)
        self.mainSplitter.addWidget(self.column3Splitter)

        # Set the initial sizes of the columns based on the proportions
        totalWidth = MainWindow.size().width()
        self.mainSplitter.setSizes([totalWidth*2//6, totalWidth*3//6, totalWidth*1//6])


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect widgets here
        self.addNotesButton.clicked.connect(self.add_note)

        MainWindow.setCentralWidget(self.mainSplitter)

    def setupMenuBar(self, MainWindow):
        # Set up the menu bar here
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

    def setupFirstColumn(self):
        # Set up the first column with a table and add button
        self.tableGroupBox = QtWidgets.QGroupBox("Questions")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tableGroupBox)
        self.questionsTableWidget = QtWidgets.QTableWidget(1, 2)
        self.questionsTableWidget.horizontalHeader().setDefaultSectionSize(75)
        self.questionsTableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_4.addWidget(self.questionsTableWidget, 0, 0, 1, 1)
        self.addQPushButton = QtWidgets.QPushButton("+")
        self.column1Splitter.addWidget(self.tableGroupBox)
        self.column1Splitter.addWidget(self.addQPushButton)
        
        # Create a new widget with a vertical layout for the line edits
        self.widget = QtWidgets.QWidget()
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.numIDLineEdit = QtWidgets.QLineEdit()
        self.numIDLineEdit.setPlaceholderText("Numerical Identifier")
        self.verticalLayout.addWidget(self.numIDLineEdit)
        self.sortLineEdit = QtWidgets.QLineEdit()
        self.sortLineEdit.setPlaceholderText("Sort Identifier")
        self.verticalLayout.addWidget(self.sortLineEdit)
        # Add the widget to the splitter
        self.column1Splitter.addWidget(self.widget)

    def setupSecondColumn(self):
        # Set up the second column with title and notes text edits
        self.titleGroupBox = QtWidgets.QGroupBox("Title")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.titleGroupBox)
        self.titleTextEdit = QtWidgets.QTextEdit()
        self.gridLayout_3.addWidget(self.titleTextEdit, 0, 0, 1, 1)
        self.notesGroupBox = QtWidgets.QGroupBox("Notes")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.notesGroupBox)
        self.notesTextEdit = QtWidgets.QTextEdit()
        self.gridLayout_2.addWidget(self.notesTextEdit, 0, 0, 1, 1)
        self.column2Splitter.addWidget(self.titleGroupBox)
        self.column2Splitter.addWidget(self.notesGroupBox)

    def setupThirdColumn(self):
        # Set up the third column with all notes list view, add notes button, and topic text edit
        self.allNotesGroupBox = QtWidgets.QGroupBox("All Notes")
        self.gridLayout = QtWidgets.QGridLayout(self.allNotesGroupBox)
        self.allNotesScrollArea = QtWidgets.QScrollArea()
        self.allNotesScrollArea.setWidgetResizable(True)
        self.allNotesScrollAreaWidgetContents = QtWidgets.QWidget()
        self.allNotesScrollArea.setWidget(self.allNotesScrollAreaWidgetContents)
        
        # Create the list view and add it to the scroll area's widget contents layout
        self.allNoteListView = QtWidgets.QListView(self.allNotesScrollAreaWidgetContents)
        layout = QtWidgets.QVBoxLayout(self.allNotesScrollAreaWidgetContents)
        layout.addWidget(self.allNoteListView)
        
        self.gridLayout.addWidget(self.allNotesScrollArea, 0, 0, 1, 1)
        self.addNotesButton = QtWidgets.QPushButton("Add")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.addNotesButton.setSizePolicy(sizePolicy)
        
        self.topicGroupBox = QtWidgets.QGroupBox("Topic")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.topicGroupBox)
        self.topicTextEdit = QtWidgets.QTextEdit()
        self.gridLayout_5.addWidget(self.topicTextEdit, 0, 0, 1, 1)
        self.column3Splitter.addWidget(self.allNotesGroupBox)   
        self.column3Splitter.addWidget(self.addNotesButton)
        self.column3Splitter.addWidget(self.topicGroupBox)

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

    # V: Add features here
    def add_note(self):
        model = self.allNoteListView.model()
        if model is None:
            model = QtGui.QStandardItemModel(self.allNoteListView)

        item = QtGui.QStandardItem("New Note")
        model.appendRow(item)
        self.allNoteListView.setModel(model)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())