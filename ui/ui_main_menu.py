# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainMenu.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QWidget)

class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        if not MainMenu.objectName():
            MainMenu.setObjectName(u"MainMenu")
        MainMenu.resize(422, 458)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainMenu.sizePolicy().hasHeightForWidth())
        MainMenu.setSizePolicy(sizePolicy)
        self.actionShowInfo = QAction(MainMenu)
        self.actionShowInfo.setObjectName(u"actionShowInfo")
        self.actionLanguage = QAction(MainMenu)
        self.actionLanguage.setObjectName(u"actionLanguage")
        self.centralwidget = QWidget(MainMenu)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(36)
        self.configFrame = QFrame(self.centralwidget)
        self.configFrame.setObjectName(u"configFrame")
        self.configFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.configFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.configFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.profilesButton = QPushButton(self.configFrame)
        self.profilesButton.setObjectName(u"profilesButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.profilesButton.sizePolicy().hasHeightForWidth())
        self.profilesButton.setSizePolicy(sizePolicy1)
        self.profilesButton.setMinimumSize(QSize(81, 25))
        self.profilesButton.setMaximumSize(QSize(16777215, 16777215))
        self.profilesButton.setFlat(False)

        self.gridLayout_2.addWidget(self.profilesButton, 1, 0, 1, 1)

        self.mappersButton = QPushButton(self.configFrame)
        self.mappersButton.setObjectName(u"mappersButton")
        self.mappersButton.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.mappersButton.sizePolicy().hasHeightForWidth())
        self.mappersButton.setSizePolicy(sizePolicy1)
        self.mappersButton.setMinimumSize(QSize(81, 25))
        self.mappersButton.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.mappersButton, 1, 1, 1, 1)

        self.activeProfileFrame = QFrame(self.configFrame)
        self.activeProfileFrame.setObjectName(u"activeProfileFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.activeProfileFrame.sizePolicy().hasHeightForWidth())
        self.activeProfileFrame.setSizePolicy(sizePolicy2)
        self.activeProfileFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.activeProfileFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.activeProfileFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 9, -1, 9)
        self.currentUserLabel = QLabel(self.activeProfileFrame)
        self.currentUserLabel.setObjectName(u"currentUserLabel")

        self.horizontalLayout.addWidget(self.currentUserLabel)

        self.currentUsernameLabel = QLabel(self.activeProfileFrame)
        self.currentUsernameLabel.setObjectName(u"currentUsernameLabel")

        self.horizontalLayout.addWidget(self.currentUsernameLabel)

        self.horizontalSpacer = QSpacerItem(138, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout_2.addWidget(self.activeProfileFrame, 0, 0, 1, 2)


        self.gridLayout_3.addWidget(self.configFrame, 0, 0, 1, 1)

        self.exportPricebookGroupBox = QGroupBox(self.centralwidget)
        self.exportPricebookGroupBox.setObjectName(u"exportPricebookGroupBox")
        self.exportPricebookGroupBox.setEnabled(False)
        self.exportPricebookGroupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.exportPricebookGroupBox.setFlat(True)
        self.gridLayout = QGridLayout(self.exportPricebookGroupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 9, -1, -1)
        self.selectMapperLabel = QLabel(self.exportPricebookGroupBox)
        self.selectMapperLabel.setObjectName(u"selectMapperLabel")

        self.gridLayout.addWidget(self.selectMapperLabel, 0, 0, 1, 1)

        self.fileLabel = QLabel(self.exportPricebookGroupBox)
        self.fileLabel.setObjectName(u"fileLabel")

        self.gridLayout.addWidget(self.fileLabel, 0, 1, 1, 1)

        self.mapperList = QListWidget(self.exportPricebookGroupBox)
        self.mapperList.setObjectName(u"mapperList")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.mapperList.sizePolicy().hasHeightForWidth())
        self.mapperList.setSizePolicy(sizePolicy3)
        self.mapperList.setMinimumSize(QSize(0, 1))
        self.mapperList.setMaximumSize(QSize(400, 16777215))

        self.gridLayout.addWidget(self.mapperList, 1, 0, 4, 1)

        self.chooseFileButton = QPushButton(self.exportPricebookGroupBox)
        self.chooseFileButton.setObjectName(u"chooseFileButton")

        self.gridLayout.addWidget(self.chooseFileButton, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 99, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.exportCsvButton = QPushButton(self.exportPricebookGroupBox)
        self.exportCsvButton.setObjectName(u"exportCsvButton")
        self.exportCsvButton.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.exportCsvButton.sizePolicy().hasHeightForWidth())
        self.exportCsvButton.setSizePolicy(sizePolicy1)
        self.exportCsvButton.setMinimumSize(QSize(81, 21))
        self.exportCsvButton.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.exportCsvButton, 3, 1, 1, 1)

        self.loadToSfButton = QPushButton(self.exportPricebookGroupBox)
        self.loadToSfButton.setObjectName(u"loadToSfButton")
        self.loadToSfButton.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.loadToSfButton.sizePolicy().hasHeightForWidth())
        self.loadToSfButton.setSizePolicy(sizePolicy1)
        self.loadToSfButton.setMinimumSize(QSize(81, 21))
        self.loadToSfButton.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.loadToSfButton, 4, 1, 1, 1)


        self.gridLayout_3.addWidget(self.exportPricebookGroupBox, 1, 0, 1, 1)

        MainMenu.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainMenu)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 422, 33))
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        self.menuInfo = QMenu(self.menubar)
        self.menuInfo.setObjectName(u"menuInfo")
        MainMenu.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainMenu)
        self.statusbar.setObjectName(u"statusbar")
        MainMenu.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())
        self.menuOptions.addAction(self.actionLanguage)
        self.menuInfo.addAction(self.actionShowInfo)

        self.retranslateUi(MainMenu)

        QMetaObject.connectSlotsByName(MainMenu)
    # setupUi

    def retranslateUi(self, MainMenu):
        MainMenu.setWindowTitle(QCoreApplication.translate("MainMenu", u"Quickport", None))
        self.actionShowInfo.setText(QCoreApplication.translate("MainMenu", u"Show Info", None))
        self.actionLanguage.setText(QCoreApplication.translate("MainMenu", u"Language", None))
        self.profilesButton.setText(QCoreApplication.translate("MainMenu", u"Profiles", None))
        self.mappersButton.setText(QCoreApplication.translate("MainMenu", u"Mappers", None))
        self.currentUserLabel.setText(QCoreApplication.translate("MainMenu", u"Profile: ", None))
        self.currentUsernameLabel.setText(QCoreApplication.translate("MainMenu", u"-none-", None))
        self.exportPricebookGroupBox.setTitle(QCoreApplication.translate("MainMenu", u"Export Data", None))
        self.selectMapperLabel.setText(QCoreApplication.translate("MainMenu", u"Select mapper:", None))
        self.fileLabel.setText(QCoreApplication.translate("MainMenu", u"Choose pricebook file:", None))
        self.chooseFileButton.setText(QCoreApplication.translate("MainMenu", u"Choose File", None))
        self.exportCsvButton.setText(QCoreApplication.translate("MainMenu", u"Export CSV", None))
        self.loadToSfButton.setText(QCoreApplication.translate("MainMenu", u"Load to SF", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainMenu", u"Options", None))
        self.menuInfo.setTitle(QCoreApplication.translate("MainMenu", u"Info", None))
    # retranslateUi

