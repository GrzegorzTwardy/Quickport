# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about-dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        if not AboutDialog.objectName():
            AboutDialog.setObjectName(u"AboutDialog")
        AboutDialog.resize(462, 370)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AboutDialog.sizePolicy().hasHeightForWidth())
        AboutDialog.setSizePolicy(sizePolicy)
        AboutDialog.setMinimumSize(QSize(462, 370))
        AboutDialog.setMaximumSize(QSize(462, 370))
        self.gridLayout = QGridLayout(AboutDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.image_label = QLabel(AboutDialog)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setEnabled(True)
        sizePolicy.setHeightForWidth(self.image_label.sizePolicy().hasHeightForWidth())
        self.image_label.setSizePolicy(sizePolicy)
        self.image_label.setMinimumSize(QSize(444, 250))
        self.image_label.setMaximumSize(QSize(444, 250))
        self.image_label.setPixmap(QPixmap(u"./img/quickport-dark-logo.png"))
        self.image_label.setScaledContents(True)

        self.gridLayout.addWidget(self.image_label, 0, 0, 1, 3)

        self.horizontalSpacer = QSpacerItem(297, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 5, 0, 1, 2)

        self.version_label = QLabel(AboutDialog)
        self.version_label.setObjectName(u"version_label")

        self.gridLayout.addWidget(self.version_label, 2, 0, 1, 1)

        self.pushButton = QPushButton(AboutDialog)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton, 5, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 1, 1, 1)

        self.info_value_label = QLabel(AboutDialog)
        self.info_value_label.setObjectName(u"info_value_label")
        self.info_value_label.setOpenExternalLinks(False)

        self.gridLayout.addWidget(self.info_value_label, 3, 1, 1, 2)

        self.info_label = QLabel(AboutDialog)
        self.info_label.setObjectName(u"info_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.info_label.sizePolicy().hasHeightForWidth())
        self.info_label.setSizePolicy(sizePolicy1)
        self.info_label.setMaximumSize(QSize(110, 16777215))

        self.gridLayout.addWidget(self.info_label, 3, 0, 1, 1)

        self.version_value_label = QLabel(AboutDialog)
        self.version_value_label.setObjectName(u"version_value_label")

        self.gridLayout.addWidget(self.version_value_label, 2, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 0, 1, 3)


        self.retranslateUi(AboutDialog)

        QMetaObject.connectSlotsByName(AboutDialog)
    # setupUi

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QCoreApplication.translate("AboutDialog", u"About Quickport", None))
        self.image_label.setText("")
        self.version_label.setText(QCoreApplication.translate("AboutDialog", u"Version:", None))
        self.pushButton.setText(QCoreApplication.translate("AboutDialog", u"Ok", None))
        self.info_value_label.setText(QCoreApplication.translate("AboutDialog", u"""<a href='https://github.com/GrzegorzTwardy/Quickport'>https://github.com/GrzegorzTwardy/Quickport</a>""", None))
        self.info_label.setText(QCoreApplication.translate("AboutDialog", u"More information:", None))
        self.version_value_label.setText(QCoreApplication.translate("AboutDialog", u"-", None))
    # retranslateUi

