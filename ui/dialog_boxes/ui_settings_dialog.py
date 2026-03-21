# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings-dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QWidget)

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName(u"SettingsDialog")
        SettingsDialog.resize(406, 238)
        self.gridLayout_4 = QGridLayout(SettingsDialog)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame = QFrame(SettingsDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 26))
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(423, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.resetButton = QPushButton(self.frame)
        self.resetButton.setObjectName(u"resetButton")

        self.gridLayout_3.addWidget(self.resetButton, 0, 1, 1, 1)

        self.saveButton = QPushButton(self.frame)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setEnabled(False)

        self.gridLayout_3.addWidget(self.saveButton, 0, 2, 1, 1)


        self.gridLayout_4.addWidget(self.frame, 2, 0, 1, 1)

        self.frame_3 = QFrame(SettingsDialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.outputPathLineEdit = QLineEdit(self.frame_3)
        self.outputPathLineEdit.setObjectName(u"outputPathLineEdit")

        self.gridLayout_2.addWidget(self.outputPathLineEdit, 1, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(268, 34, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 2, 0, 1, 2)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)

        self.chooseFolderButton = QPushButton(self.frame_3)
        self.chooseFolderButton.setObjectName(u"chooseFolderButton")

        self.gridLayout_2.addWidget(self.chooseFolderButton, 1, 2, 1, 1)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 3)


        self.gridLayout_4.addWidget(self.frame_3, 1, 0, 1, 1)

        self.frame_2 = QFrame(SettingsDialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.maxRowsSpinBox = QSpinBox(self.frame_2)
        self.maxRowsSpinBox.setObjectName(u"maxRowsSpinBox")
        self.maxRowsSpinBox.setMinimum(1)
        self.maxRowsSpinBox.setMaximum(1000)
        self.maxRowsSpinBox.setValue(50)

        self.gridLayout.addWidget(self.maxRowsSpinBox, 2, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(268, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 2)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.languageComboBox = QComboBox(self.frame_2)
        self.languageComboBox.addItem("")
        self.languageComboBox.setObjectName(u"languageComboBox")

        self.gridLayout.addWidget(self.languageComboBox, 1, 1, 1, 1)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)


        self.gridLayout_4.addWidget(self.frame_2, 0, 0, 1, 1)
        
        self.resetButton.setAutoDefault(False)
        self.saveButton.setAutoDefault(False)
        self.chooseFolderButton.setAutoDefault(False)

        self.retranslateUi(SettingsDialog)

        QMetaObject.connectSlotsByName(SettingsDialog)
    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"Settings", None))
        self.resetButton.setText(QCoreApplication.translate("SettingsDialog", u"Reset", None))
        self.saveButton.setText(QCoreApplication.translate("SettingsDialog", u"Save", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("SettingsDialog", u"Output stores the files with records that couldn't be loaded to Salesforce", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("SettingsDialog", u"Output Path:", None))
        self.chooseFolderButton.setText(QCoreApplication.translate("SettingsDialog", u"Choose Folder", None))
        self.label_2.setText(QCoreApplication.translate("SettingsDialog", u"GLOBAL PATHS", None))
        self.label_3.setText(QCoreApplication.translate("SettingsDialog", u"Language:", None))
        self.label_4.setText(QCoreApplication.translate("SettingsDialog", u"Max records in table:", None))
        self.languageComboBox.setItemText(0, QCoreApplication.translate("SettingsDialog", u"English", None))

        self.label.setText(QCoreApplication.translate("SettingsDialog", u"DISPLAY", None))
    # retranslateUi

