# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'import-progress-bar.ui'
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
    QProgressBar, QSizePolicy, QWidget)

class Ui_ImportProgressBar(object):
    def setupUi(self, ImportProgressBar):
        if not ImportProgressBar.objectName():
            ImportProgressBar.setObjectName(u"ImportProgressBar")
        ImportProgressBar.resize(327, 94)
        self.gridLayout = QGridLayout(ImportProgressBar)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setContentsMargins(18, 18, 18, 12)
        self.infoLabel = QLabel(ImportProgressBar)
        self.infoLabel.setObjectName(u"infoLabel")
        self.infoLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.infoLabel, 0, 0, 1, 1)

        self.progressBar = QProgressBar(ImportProgressBar)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximum(0)
        self.progressBar.setValue(-1)
        self.progressBar.setTextVisible(False)

        self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 1)


        self.retranslateUi(ImportProgressBar)

        QMetaObject.connectSlotsByName(ImportProgressBar)
    # setupUi

    def retranslateUi(self, ImportProgressBar):
        ImportProgressBar.setWindowTitle(QCoreApplication.translate("ImportProgressBar", u"Loading to Salesforce", None))
        self.infoLabel.setText(QCoreApplication.translate("ImportProgressBar", u"TextLabel", None))
    # retranslateUi

