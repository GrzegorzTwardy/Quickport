# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mapper-list.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_MapperListMain(object):
    def setupUi(self, MapperListMain):
        if not MapperListMain.objectName():
            MapperListMain.setObjectName(u"MapperListMain")
        MapperListMain.resize(350, 364)
        self.gridLayout_2 = QGridLayout(MapperListMain)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, -1, 9, -1)
        self.label = QLabel(MapperListMain)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.mapperList = QListWidget(MapperListMain)
        self.mapperList.setObjectName(u"mapperList")

        self.gridLayout_2.addWidget(self.mapperList, 1, 0, 1, 1)

        self.buttonsFrame = QFrame(MapperListMain)
        self.buttonsFrame.setObjectName(u"buttonsFrame")
        self.buttonsFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.buttonsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.buttonsFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, 0, 0, 0)
        self.addButton = QPushButton(self.buttonsFrame)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setEnabled(False)

        self.gridLayout.addWidget(self.addButton, 0, 0, 1, 1)

        self.editButton = QPushButton(self.buttonsFrame)
        self.editButton.setObjectName(u"editButton")
        self.editButton.setEnabled(False)

        self.gridLayout.addWidget(self.editButton, 1, 0, 1, 1)

        self.removeButton = QPushButton(self.buttonsFrame)
        self.removeButton.setObjectName(u"removeButton")
        self.removeButton.setEnabled(False)

        self.gridLayout.addWidget(self.removeButton, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 193, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.backButton = QPushButton(self.buttonsFrame)
        self.backButton.setObjectName(u"backButton")

        self.gridLayout.addWidget(self.backButton, 4, 0, 1, 1)


        self.gridLayout_2.addWidget(self.buttonsFrame, 1, 1, 1, 1)


        self.retranslateUi(MapperListMain)

        QMetaObject.connectSlotsByName(MapperListMain)
    # setupUi

    def retranslateUi(self, MapperListMain):
        MapperListMain.setWindowTitle(QCoreApplication.translate("MapperListMain", u"Available Mappers", None))
        self.label.setText(QCoreApplication.translate("MapperListMain", u"Choose mapper:", None))
        self.addButton.setText(QCoreApplication.translate("MapperListMain", u"Add", None))
        self.editButton.setText(QCoreApplication.translate("MapperListMain", u"Edit", None))
        self.removeButton.setText(QCoreApplication.translate("MapperListMain", u"Remove", None))
        self.backButton.setText(QCoreApplication.translate("MapperListMain", u"Back", None))
    # retranslateUi

