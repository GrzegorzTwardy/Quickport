# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile-manager.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QWidget)

class Ui_ProfileManager(object):
    def setupUi(self, profileManager):
        if not profileManager.objectName():
            profileManager.setObjectName(u"profileManager")
        profileManager.resize(422, 458)
        self.gridLayout = QGridLayout(profileManager)
        self.gridLayout.setObjectName(u"gridLayout")
        self.profilesLabel = QLabel(profileManager)
        self.profilesLabel.setObjectName(u"profilesLabel")

        self.gridLayout.addWidget(self.profilesLabel, 0, 0, 1, 1)

        self.profileList = QListWidget(profileManager)
        self.profileList.setObjectName(u"profileList")
        self.profileList.setMinimumSize(QSize(102, 0))

        self.gridLayout.addWidget(self.profileList, 1, 0, 7, 1)

        self.addProfileButton = QPushButton(profileManager)
        self.addProfileButton.setObjectName(u"addProfileButton")

        self.gridLayout.addWidget(self.addProfileButton, 1, 1, 1, 1)

        self.editProfileButton = QPushButton(profileManager)
        self.editProfileButton.setObjectName(u"editProfileButton")
        self.editProfileButton.setEnabled(False)

        self.gridLayout.addWidget(self.editProfileButton, 2, 1, 1, 1)

        self.deteleProfileButton = QPushButton(profileManager)
        self.deteleProfileButton.setObjectName(u"deteleProfileButton")
        self.deteleProfileButton.setEnabled(False)

        self.gridLayout.addWidget(self.deteleProfileButton, 3, 1, 1, 1)

        self.descTextEdit = QTextEdit(profileManager)
        self.descTextEdit.setObjectName(u"descTextEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.descTextEdit.sizePolicy().hasHeightForWidth())
        self.descTextEdit.setSizePolicy(sizePolicy)
        self.descTextEdit.setMinimumSize(QSize(0, 0))
        self.descTextEdit.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.descTextEdit.setFrameShape(QFrame.Shape.StyledPanel)
        self.descTextEdit.setReadOnly(True)
        self.descTextEdit.setOverwriteMode(False)

        self.gridLayout.addWidget(self.descTextEdit, 4, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 159, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 5, 1, 1, 1)

        self.logToSandbox = QCheckBox(profileManager)
        self.logToSandbox.setObjectName(u"logToSandbox")
        self.logToSandbox.setEnabled(False)

        self.gridLayout.addWidget(self.logToSandbox, 6, 1, 1, 1)

        self.loginButton = QPushButton(profileManager)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setEnabled(False)
        self.loginButton.setMinimumSize(QSize(0, 26))

        self.gridLayout.addWidget(self.loginButton, 7, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 3)
        self.gridLayout.setColumnStretch(1, 1)

        self.retranslateUi(profileManager)

        QMetaObject.connectSlotsByName(profileManager)
    # setupUi

    def retranslateUi(self, profileManager):
        profileManager.setWindowTitle(QCoreApplication.translate("profileManager", u"Profile Manager", None))
        self.profilesLabel.setText(QCoreApplication.translate("profileManager", u"Profiles:", None))
        self.addProfileButton.setText(QCoreApplication.translate("profileManager", u"Add", None))
        self.editProfileButton.setText(QCoreApplication.translate("profileManager", u"Edit", None))
        self.deteleProfileButton.setText(QCoreApplication.translate("profileManager", u"Delete", None))
        self.logToSandbox.setText(QCoreApplication.translate("profileManager", u"log in to sandbox", None))
        self.loginButton.setText(QCoreApplication.translate("profileManager", u"Log In", None))
    # retranslateUi

