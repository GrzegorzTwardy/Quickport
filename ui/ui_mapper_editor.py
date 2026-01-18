# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'parser-editor-3.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtGui import (QFont, QIcon)
from PySide6.QtWidgets import (QFrame, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget)

class Ui_MapperEditor(object):
    def setupUi(self, MapperEditor):
        if not MapperEditor.objectName():
            MapperEditor.setObjectName(u"MapperEditor")
        MapperEditor.resize(1452, 840)
        MapperEditor.setWindowOpacity(1.000000000000000)
        self.gridLayout_12 = QGridLayout(MapperEditor)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.mapper_name_frame = QFrame(MapperEditor)
        self.mapper_name_frame.setObjectName(u"mapper_name_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mapper_name_frame.sizePolicy().hasHeightForWidth())
        self.mapper_name_frame.setSizePolicy(sizePolicy)
        self.mapper_name_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.mapper_name_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.mapper_name_frame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.mapper_name_label = QLabel(self.mapper_name_frame)
        self.mapper_name_label.setObjectName(u"mapper_name_label")
        font = QFont()
        font.setPointSize(11)
        self.mapper_name_label.setFont(font)

        self.gridLayout_6.addWidget(self.mapper_name_label, 0, 0, 1, 1)

        self.choose_file_button = QPushButton(self.mapper_name_frame)
        self.choose_file_button.setObjectName(u"choose_file_button")

        self.gridLayout_6.addWidget(self.choose_file_button, 0, 4, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(566, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.mapper_name_line_edit = QLineEdit(self.mapper_name_frame)
        self.mapper_name_line_edit.setObjectName(u"mapper_name_line_edit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mapper_name_line_edit.sizePolicy().hasHeightForWidth())
        self.mapper_name_line_edit.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.mapper_name_line_edit.setFont(font1)
        self.mapper_name_line_edit.setFrame(True)
        self.mapper_name_line_edit.setClearButtonEnabled(False)

        self.gridLayout_6.addWidget(self.mapper_name_line_edit, 0, 1, 1, 1)

        self.input_file_label = QLabel(self.mapper_name_frame)
        self.input_file_label.setObjectName(u"input_file_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.input_file_label.sizePolicy().hasHeightForWidth())
        self.input_file_label.setSizePolicy(sizePolicy2)

        self.gridLayout_6.addWidget(self.input_file_label, 0, 3, 1, 1)


        self.gridLayout_12.addWidget(self.mapper_name_frame, 0, 0, 1, 1)

        self.sheet_tabs = QTabWidget(MapperEditor)
        self.sheet_tabs.setObjectName(u"sheet_tabs")
        self.sheet_tabs.setAutoFillBackground(False)
        self.sheet_tabs.setStyleSheet(u"QTabWidget::pane {\n"
"    background: transparent;\n"
"    border: 1px solid #4d4d4d;\n"
"	border-radius: 5px;\n"
"}\n"
"")

        self.gridLayout_12.addWidget(self.sheet_tabs, 1, 0, 1, 1)

        self.save_cancel_frame = QFrame(MapperEditor)
        self.save_cancel_frame.setObjectName(u"save_cancel_frame")
        self.save_cancel_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.save_cancel_frame.setFrameShadow(QFrame.Shadow.Plain)
        self.gridLayout_5 = QGridLayout(self.save_cancel_frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.cancel_editing_button = QPushButton(self.save_cancel_frame)
        self.cancel_editing_button.setObjectName(u"cancel_editing_button")

        self.gridLayout_5.addWidget(self.cancel_editing_button, 0, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(1018, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.save_mapper_button = QPushButton(self.save_cancel_frame)
        self.save_mapper_button.setObjectName(u"save_mapper_button")
        self.save_mapper_button.setEnabled(False)

        self.gridLayout_5.addWidget(self.save_mapper_button, 0, 4, 1, 1)


        self.gridLayout_12.addWidget(self.save_cancel_frame, 2, 0, 1, 1)


        self.retranslateUi(MapperEditor)

        self.sheet_tabs.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MapperEditor)
    # setupUi

    def retranslateUi(self, MapperEditor):
        MapperEditor.setWindowTitle(QCoreApplication.translate("MapperEditor", u"Mapper Editor", None))
        self.mapper_name_label.setText(QCoreApplication.translate("MapperEditor", u"Name:", None))
        self.choose_file_button.setText(QCoreApplication.translate("MapperEditor", u"Choose file", None))
        self.mapper_name_line_edit.setPlaceholderText(QCoreApplication.translate("MapperEditor", u"new-mapper", None))
        self.input_file_label.setText(QCoreApplication.translate("MapperEditor", u"Preview: - no file selected -", None))
        self.cancel_editing_button.setText(QCoreApplication.translate("MapperEditor", u"Cancel", None))
        self.save_mapper_button.setText(QCoreApplication.translate("MapperEditor", u"Save", None))
    # retranslateUi

