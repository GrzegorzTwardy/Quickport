# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile-config.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QFrame, QGridLayout, QLabel,
    QLineEdit, QSizePolicy, QTextEdit, QWidget)

class Ui_ProfileConfig(object):
    def setupUi(self, ProfileConfig):
        if not ProfileConfig.objectName():
            ProfileConfig.setObjectName(u"ProfileConfig")
        ProfileConfig.resize(412, 265)
        self.gridLayout_4 = QGridLayout(ProfileConfig)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.mainFrame = QFrame(ProfileConfig)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.mainFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.mainFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.mainFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.prodCidLe = QLineEdit(self.mainFrame)
        self.prodCidLe.setObjectName(u"prodCidLe")

        self.gridLayout_3.addWidget(self.prodCidLe, 1, 1, 1, 1)

        self.sandboxCidLe = QLineEdit(self.mainFrame)
        self.sandboxCidLe.setObjectName(u"sandboxCidLe")

        self.gridLayout_3.addWidget(self.sandboxCidLe, 2, 1, 1, 1)

        self.descLabel = QLabel(self.mainFrame)
        self.descLabel.setObjectName(u"descLabel")
        self.descLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)

        self.gridLayout_3.addWidget(self.descLabel, 3, 0, 1, 1)

        self.sandboxCidFrame = QFrame(self.mainFrame)
        self.sandboxCidFrame.setObjectName(u"sandboxCidFrame")
        self.sandboxCidFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.sandboxCidFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.sandboxCidFrame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.sandboxCidLabel = QLabel(self.sandboxCidFrame)
        self.sandboxCidLabel.setObjectName(u"sandboxCidLabel")
        self.sandboxCidLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.sandboxCidLabel, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.sandboxCidFrame, 2, 0, 1, 1)

        self.nameLabel = QLabel(self.mainFrame)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.nameLabel, 0, 0, 1, 1)

        self.prodCidFrame = QFrame(self.mainFrame)
        self.prodCidFrame.setObjectName(u"prodCidFrame")
        self.prodCidFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.prodCidFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.prodCidFrame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.prodCidLabel = QLabel(self.prodCidFrame)
        self.prodCidLabel.setObjectName(u"prodCidLabel")
        self.prodCidLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.prodCidLabel, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.prodCidFrame, 1, 0, 1, 1)

        self.sandboxCidCheckBox = QCheckBox(self.mainFrame)
        self.sandboxCidCheckBox.setObjectName(u"sandboxCidCheckBox")
        self.sandboxCidCheckBox.setChecked(True)

        self.gridLayout_3.addWidget(self.sandboxCidCheckBox, 2, 2, 1, 1)

        self.prodCidCheckBox = QCheckBox(self.mainFrame)
        self.prodCidCheckBox.setObjectName(u"prodCidCheckBox")
        self.prodCidCheckBox.setChecked(True)

        self.gridLayout_3.addWidget(self.prodCidCheckBox, 1, 2, 1, 1)

        self.descTe = QTextEdit(self.mainFrame)
        self.descTe.setObjectName(u"descTe")

        self.gridLayout_3.addWidget(self.descTe, 3, 1, 1, 2)

        self.nameLe = QLineEdit(self.mainFrame)
        self.nameLe.setObjectName(u"nameLe")

        self.gridLayout_3.addWidget(self.nameLe, 0, 1, 1, 2)

        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 2)

        self.gridLayout_4.addWidget(self.mainFrame, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(ProfileConfig)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout_4.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(ProfileConfig)
        self.buttonBox.accepted.connect(ProfileConfig.accept)
        self.buttonBox.rejected.connect(ProfileConfig.reject)

        QMetaObject.connectSlotsByName(ProfileConfig)
    # setupUi

    def retranslateUi(self, ProfileConfig):
        ProfileConfig.setWindowTitle(QCoreApplication.translate("ProfileConfig", u"Profile Configuration", None))
        self.descLabel.setText(QCoreApplication.translate("ProfileConfig", u"Description:", None))
#if QT_CONFIG(tooltip)
        self.sandboxCidLabel.setToolTip(QCoreApplication.translate("ProfileConfig", u"<html><head/><body><p>Consumer Key corresponding to the ECA/Connected App in your test environment.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.sandboxCidLabel.setText(QCoreApplication.translate("ProfileConfig", u"Sandbox Client ID:", None))
        self.nameLabel.setText(QCoreApplication.translate("ProfileConfig", u"Profile Name:", None))
#if QT_CONFIG(tooltip)
        self.prodCidLabel.setToolTip(QCoreApplication.translate("ProfileConfig", u"<html><head/><body><p>Consumer Key corresponding to the ECA/Connected App in your production environment</p><p>(with exception to Playgrounds on Trailhead).</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.prodCidLabel.setText(QCoreApplication.translate("ProfileConfig", u"Production Client ID:", None))
        self.sandboxCidCheckBox.setText("")
        self.prodCidCheckBox.setText("")
        self.nameLe.setFocus()
    # retranslateUi