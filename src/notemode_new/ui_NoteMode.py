# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NoteModeRedesignuQDUOO.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(752, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.c1VerticalLayout = QVBoxLayout()
        self.c1VerticalLayout.setObjectName(u"c1VerticalLayout")
        self.c1VerticalLayout.setContentsMargins(-1, 5, -1, 5)
        self.questionLabel = QLabel(self.centralwidget)
        self.questionLabel.setObjectName(u"questionLabel")

        self.c1VerticalLayout.addWidget(self.questionLabel)

        self.quesTableWidget = QTableWidget(self.centralwidget)
        if (self.quesTableWidget.columnCount() < 2):
            self.quesTableWidget.setColumnCount(2)
        if (self.quesTableWidget.rowCount() < 20):
            self.quesTableWidget.setRowCount(20)
        self.quesTableWidget.setObjectName(u"quesTableWidget")
        self.quesTableWidget.setRowCount(20)
        self.quesTableWidget.setColumnCount(2)

        self.c1VerticalLayout.addWidget(self.quesTableWidget)

        self.c1VerticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.c1VerticalLayout.addItem(self.c1VerticalSpacer)

        self.nameHorizontalLayout = QHBoxLayout()
        self.nameHorizontalLayout.setObjectName(u"nameHorizontalLayout")
        self.nameLabel = QLabel(self.centralwidget)
        self.nameLabel.setObjectName(u"nameLabel")

        self.nameHorizontalLayout.addWidget(self.nameLabel)

        self.nameLineEdit = QLineEdit(self.centralwidget)
        self.nameLineEdit.setObjectName(u"nameLineEdit")

        self.nameHorizontalLayout.addWidget(self.nameLineEdit)


        self.c1VerticalLayout.addLayout(self.nameHorizontalLayout)

        self.numHorizontalLayout = QHBoxLayout()
        self.numHorizontalLayout.setObjectName(u"numHorizontalLayout")
        self.idLabel = QLabel(self.centralwidget)
        self.idLabel.setObjectName(u"idLabel")

        self.numHorizontalLayout.addWidget(self.idLabel)

        self.idLineEdit = QLineEdit(self.centralwidget)
        self.idLineEdit.setObjectName(u"idLineEdit")

        self.numHorizontalLayout.addWidget(self.idLineEdit)


        self.c1VerticalLayout.addLayout(self.numHorizontalLayout)


        self.horizontalLayout.addLayout(self.c1VerticalLayout)

        self.c2VerticalLayout = QVBoxLayout()
        self.c2VerticalLayout.setObjectName(u"c2VerticalLayout")
        self.c2VerticalLayout.setContentsMargins(-1, 5, -1, 5)
        self.titleLabel = QLabel(self.centralwidget)
        self.titleLabel.setObjectName(u"titleLabel")

        self.c2VerticalLayout.addWidget(self.titleLabel)

        self.titleTextEdit = QTextEdit(self.centralwidget)
        self.titleTextEdit.setObjectName(u"titleTextEdit")
        self.titleTextEdit.setMaximumSize(QSize(16777215, 30))

        self.c2VerticalLayout.addWidget(self.titleTextEdit)

        self.notesLabel = QLabel(self.centralwidget)
        self.notesLabel.setObjectName(u"notesLabel")

        self.c2VerticalLayout.addWidget(self.notesLabel)

        self.notesTextEdit = QTextEdit(self.centralwidget)
        self.notesTextEdit.setObjectName(u"notesTextEdit")
        self.notesTextEdit.setMaximumSize(QSize(16777215, 360))

        self.c2VerticalLayout.addWidget(self.notesTextEdit)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.c2VerticalLayout.addItem(self.verticalSpacer_3)

        self.c2VerticalLayout.setStretch(0, 1)
        self.c2VerticalLayout.setStretch(1, 1)
        self.c2VerticalLayout.setStretch(2, 1)
        self.c2VerticalLayout.setStretch(3, 50)
        self.c2VerticalLayout.setStretch(4, 5)

        self.horizontalLayout.addLayout(self.c2VerticalLayout)

        self.c3VerticalLayout = QVBoxLayout()
        self.c3VerticalLayout.setObjectName(u"c3VerticalLayout")
        self.c3VerticalLayout.setContentsMargins(-1, 5, -1, 5)
        self.allNLabel = QLabel(self.centralwidget)
        self.allNLabel.setObjectName(u"allNLabel")

        self.c3VerticalLayout.addWidget(self.allNLabel)

        self.allNoteListWidget = QListWidget(self.centralwidget)
        self.allNoteListWidget.setObjectName(u"allNoteListWidget")

        self.c3VerticalLayout.addWidget(self.allNoteListWidget)

        self.verticalSpacer_2 = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.c3VerticalLayout.addItem(self.verticalSpacer_2)

        self.topicLabel = QLabel(self.centralwidget)
        self.topicLabel.setObjectName(u"topicLabel")

        self.c3VerticalLayout.addWidget(self.topicLabel)

        self.topicTextEdit = QTextEdit(self.centralwidget)
        self.topicTextEdit.setObjectName(u"topicTextEdit")
        self.topicTextEdit.setMaximumSize(QSize(16777215, 30))

        self.c3VerticalLayout.addWidget(self.topicTextEdit)


        self.horizontalLayout.addLayout(self.c3VerticalLayout)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 4)
        self.horizontalLayout.setStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 752, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.questionLabel.setText(QCoreApplication.translate("MainWindow", u"Questions", None))
        self.nameLabel.setText(QCoreApplication.translate("MainWindow", u"Name ID", None))
        self.idLabel.setText(QCoreApplication.translate("MainWindow", u"Numb ID", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.notesLabel.setText(QCoreApplication.translate("MainWindow", u"Notes", None))
        self.allNLabel.setText(QCoreApplication.translate("MainWindow", u"All Notes", None))
        self.topicLabel.setText(QCoreApplication.translate("MainWindow", u"Topic", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

