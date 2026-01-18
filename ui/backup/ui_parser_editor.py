# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'parser-editor.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHeaderView, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QTabWidget, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_ParserEditor(object):
    
    def setupUi(self, ParserEditor):
        if not ParserEditor.objectName():
            ParserEditor.setObjectName(u"ParserEditor")
        ParserEditor.resize(1477, 819)
        ParserEditor.setWindowOpacity(1.000000000000000)
        self.gridLayout_13 = QGridLayout(ParserEditor)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.parser_name_frame = QFrame(ParserEditor)
        self.parser_name_frame.setObjectName(u"parser_name_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parser_name_frame.sizePolicy().hasHeightForWidth())
        self.parser_name_frame.setSizePolicy(sizePolicy)
        self.parser_name_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.parser_name_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.parser_name_frame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalSpacer_4 = QSpacerItem(566, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.parser_name_label = QLabel(self.parser_name_frame)
        self.parser_name_label.setObjectName(u"parser_name_label")
        font = QFont()
        font.setPointSize(11)
        self.parser_name_label.setFont(font)

        self.gridLayout_6.addWidget(self.parser_name_label, 0, 0, 1, 1)

        # ----- PARSER NAME (line edit)
        self.parser_name_line_edit = QLineEdit(self.parser_name_frame)
        self.parser_name_line_edit.setObjectName(u"parser_name_line_edit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.parser_name_line_edit.sizePolicy().hasHeightForWidth())
        self.parser_name_line_edit.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.parser_name_line_edit.setFont(font1)
        self.parser_name_line_edit.setFrame(True)
        self.parser_name_line_edit.setClearButtonEnabled(False)

        self.gridLayout_6.addWidget(self.parser_name_line_edit, 0, 1, 1, 1)


        self.gridLayout_13.addWidget(self.parser_name_frame, 0, 0, 1, 1)

        self.main_frame = QFrame(ParserEditor)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.main_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.main_frame)
        self.gridLayout_7.setSpacing(16)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.pricebooks_groupbox = QGroupBox(self.main_frame)
        self.pricebooks_groupbox.setObjectName(u"pricebooks_groupbox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pricebooks_groupbox.sizePolicy().hasHeightForWidth())
        self.pricebooks_groupbox.setSizePolicy(sizePolicy2)
        self.pricebooks_groupbox.setAutoFillBackground(False)
        self.pricebooks_groupbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pricebooks_groupbox.setFlat(True)
        self.pricebooks_groupbox.setCheckable(False)
        self.pricebooks_groupbox.setChecked(False)
        self.gridLayout_3 = QGridLayout(self.pricebooks_groupbox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, -1, -1, 0)

        # ------ PRICEBOOK SEARCHBAR (line edit)
        self.pb_searchbar_line_edit = QLineEdit(self.pricebooks_groupbox)
        self.pb_searchbar_line_edit.setObjectName(u"pb_searchbar_line_edit")
        self.pb_searchbar_line_edit.setMinimumSize(QSize(0, 0))

        self.gridLayout_3.addWidget(self.pb_searchbar_line_edit, 0, 1, 1, 1)

        # ------ PRICEBOOKS LIST (list widget)
        self.pricebooks_list = QListWidget(self.pricebooks_groupbox)
        self.pricebooks_list.setObjectName(u"pricebooks_list")
        self.pricebooks_list.setSpacing(0)
        self.pricebooks_list.setSortingEnabled(False)

        self.gridLayout_3.addWidget(self.pricebooks_list, 1, 0, 1, 3)

        # ----- SORT  PRICEBOOKS BUTTON
        self.sort_button = QPushButton(self.pricebooks_groupbox)
        self.sort_button.setObjectName(u"sort_button")

        self.gridLayout_3.addWidget(self.sort_button, 0, 2, 1, 1)


        self.gridLayout_7.addWidget(self.pricebooks_groupbox, 0, 0, 1, 1)

        self.product_fields_frame = QGroupBox(self.main_frame)
        self.product_fields_frame.setObjectName(u"product_fields_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.product_fields_frame.sizePolicy().hasHeightForWidth())
        self.product_fields_frame.setSizePolicy(sizePolicy3)
        self.product_fields_frame.setMinimumSize(QSize(370, 0))
        self.product_fields_frame.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.product_fields_frame.setFlat(False)
        self.product_fields_frame.setCheckable(False)
        self.gridLayout_4 = QGridLayout(self.product_fields_frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.functions_label = QLabel(self.product_fields_frame)
        self.functions_label.setObjectName(u"functions_label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.functions_label.sizePolicy().hasHeightForWidth())
        self.functions_label.setSizePolicy(sizePolicy4)
        self.functions_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.functions_label, 0, 2, 1, 1)

        self.separation_line = QFrame(self.product_fields_frame)
        self.separation_line.setObjectName(u"separation_line")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.separation_line.sizePolicy().hasHeightForWidth())
        self.separation_line.setSizePolicy(sizePolicy5)
        self.separation_line.setFrameShape(QFrame.Shape.HLine)
        self.separation_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.separation_line, 2, 0, 1, 4)

        self.source_label = QLabel(self.product_fields_frame)
        self.source_label.setObjectName(u"source_label")
        sizePolicy4.setHeightForWidth(self.source_label.sizePolicy().hasHeightForWidth())
        self.source_label.setSizePolicy(sizePolicy4)
        self.source_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.source_label, 0, 1, 1, 1)

        self.allow_empty_label = QLabel(self.product_fields_frame)
        self.allow_empty_label.setObjectName(u"allow_empty_label")
        sizePolicy4.setHeightForWidth(self.allow_empty_label.sizePolicy().hasHeightForWidth())
        self.allow_empty_label.setSizePolicy(sizePolicy4)
        self.allow_empty_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.allow_empty_label, 0, 3, 1, 1)

        self.product_fields_scroll_area = QScrollArea(self.product_fields_frame)
        self.product_fields_scroll_area.setObjectName(u"product_fields_scroll_area")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.product_fields_scroll_area.sizePolicy().hasHeightForWidth())
        self.product_fields_scroll_area.setSizePolicy(sizePolicy6)
        self.product_fields_scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.product_fields_scroll_area.setWidgetResizable(True)
        self.product_fields_scroll_area_contents = QWidget()
        self.product_fields_scroll_area_contents.setObjectName(u"product_fields_scroll_area_contents")
        self.product_fields_scroll_area_contents.setGeometry(QRect(0, 0, 380, 610))
        self.gridLayout_2 = QGridLayout(self.product_fields_scroll_area_contents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 0, 1, 2)

        self.product_fields_scroll_area.setWidget(self.product_fields_scroll_area_contents)

        self.gridLayout_4.addWidget(self.product_fields_scroll_area, 3, 0, 1, 4)

        self.product_fields_label = QLabel(self.product_fields_frame)
        self.product_fields_label.setObjectName(u"product_fields_label")
        sizePolicy4.setHeightForWidth(self.product_fields_label.sizePolicy().hasHeightForWidth())
        self.product_fields_label.setSizePolicy(sizePolicy4)
        self.product_fields_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.product_fields_label, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.product_fields_frame, 0, 1, 2, 1)

        self.xlsx_tabs = QTabWidget(self.main_frame)
        self.xlsx_tabs.setObjectName(u"xlsx_tabs")
        self.xlsx_tabs.setTabPosition(QTabWidget.TabPosition.North)
        self.xlsx_tabs.setTabShape(QTabWidget.TabShape.Rounded)
        self.xlsx_tabs.setElideMode(Qt.TextElideMode.ElideNone)
        self.xlsx_tabs.setDocumentMode(False)
        self.xlsx_tabs.setTabsClosable(False)
        self.xlsx_tabs.setMovable(False)
        self.xlsx_tabs.setTabBarAutoHide(False)
        self.xlsx_tab_0 = QWidget()
        self.xlsx_tab_0.setObjectName(u"xlsx_tab_0")
        self.gridLayout_11 = QGridLayout(self.xlsx_tab_0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.xlsx_table_0 = QTableWidget(self.xlsx_tab_0)
        self.xlsx_table_0.setObjectName(u"xlsx_table_0")
        self.xlsx_table_0.setRowCount(0)

        self.gridLayout_11.addWidget(self.xlsx_table_0, 0, 0, 1, 1)

        self.xlsx_tabs.addTab(self.xlsx_tab_0, "")

        self.gridLayout_7.addWidget(self.xlsx_tabs, 0, 2, 2, 1)

        self.currency_tabs = QTabWidget(self.main_frame)
        self.currency_tabs.setObjectName(u"currency_tabs")
        self.currency_tabs.setMinimumSize(QSize(371, 0))
        # self.currency_tab_0 = QWidget()
        # self.currency_tab_0.setObjectName(u"currency_tab_0")
        # self.gridLayout_9 = QGridLayout(self.currency_tab_0)
        # self.gridLayout_9.setObjectName(u"gridLayout_9")
        # self.remove_curr_button_0 = QPushButton(self.currency_tab_0)
        # self.remove_curr_button_0.setObjectName(u"remove_curr_button_0")

        # self.gridLayout_9.addWidget(self.remove_curr_button_0, 1, 1, 1, 1)

        # self.add_curr_button_0 = QPushButton(self.currency_tab_0)
        # self.add_curr_button_0.setObjectName(u"add_curr_button_0")

        # self.gridLayout_9.addWidget(self.add_curr_button_0, 1, 2, 1, 1)

        # self.horizontalSpacer_11 = QSpacerItem(133, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        # self.gridLayout_9.addItem(self.horizontalSpacer_11, 1, 0, 1, 1)

        # self.curr_scroll_area_0 = QScrollArea(self.currency_tab_0)
        # self.curr_scroll_area_0.setObjectName(u"curr_scroll_area_0")
        # sizePolicy3.setHeightForWidth(self.curr_scroll_area_0.sizePolicy().hasHeightForWidth())
        # self.curr_scroll_area_0.setSizePolicy(sizePolicy3)
        # self.curr_scroll_area_0.setFrameShape(QFrame.Shape.NoFrame)
        # self.curr_scroll_area_0.setWidgetResizable(True)
        # self.curr_scroll_area_contents_0 = QWidget()
        # self.curr_scroll_area_contents_0.setObjectName(u"curr_scroll_area_contents_0")
        # self.curr_scroll_area_contents_0.setGeometry(QRect(0, 0, 379, 186))
        # self.gridLayout_10 = QGridLayout(self.curr_scroll_area_contents_0)
        # self.gridLayout_10.setObjectName(u"gridLayout_10")
        # self.curr_frame_0 = QFrame(self.curr_scroll_area_contents_0)
        # self.curr_frame_0.setObjectName(u"curr_frame_0")
        # sizePolicy3.setHeightForWidth(self.curr_frame_0.sizePolicy().hasHeightForWidth())
        # self.curr_frame_0.setSizePolicy(sizePolicy3)
        # self.curr_frame_0.setAutoFillBackground(False)
        # self.curr_frame_0.setFrameShape(QFrame.Shape.StyledPanel)
        # self.curr_frame_0.setFrameShadow(QFrame.Shadow.Raised)
        # self.gridLayout_17 = QGridLayout(self.curr_frame_0)
        # self.gridLayout_17.setObjectName(u"gridLayout_17")
        # self.header_cf_label_0 = QLabel(self.curr_frame_0)
        # self.header_cf_label_0.setObjectName(u"header_cf_label_0")
        # sizePolicy5.setHeightForWidth(self.header_cf_label_0.sizePolicy().hasHeightForWidth())
        # self.header_cf_label_0.setSizePolicy(sizePolicy5)
        # self.header_cf_label_0.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # self.gridLayout_17.addWidget(self.header_cf_label_0, 0, 3, 1, 2)

        # self.curr_split_line_0 = QFrame(self.curr_frame_0)
        # self.curr_split_line_0.setObjectName(u"curr_split_line_0")
        # sizePolicy5.setHeightForWidth(self.curr_split_line_0.sizePolicy().hasHeightForWidth())
        # self.curr_split_line_0.setSizePolicy(sizePolicy5)
        # self.curr_split_line_0.setFrameShape(QFrame.Shape.HLine)
        # self.curr_split_line_0.setFrameShadow(QFrame.Shadow.Sunken)

        # self.gridLayout_17.addWidget(self.curr_split_line_0, 1, 0, 1, 5)

        # self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        # self.gridLayout_17.addItem(self.verticalSpacer_2, 2, 2, 1, 1)

        # self.header_curr_label_0 = QLabel(self.curr_frame_0)
        # self.header_curr_label_0.setObjectName(u"header_curr_label_0")
        # sizePolicy5.setHeightForWidth(self.header_curr_label_0.sizePolicy().hasHeightForWidth())
        # self.header_curr_label_0.setSizePolicy(sizePolicy5)
        # self.header_curr_label_0.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # self.gridLayout_17.addWidget(self.header_curr_label_0, 0, 0, 1, 2)

        # self.header_input_label_0 = QLabel(self.curr_frame_0)
        # self.header_input_label_0.setObjectName(u"header_input_label_0")
        # sizePolicy5.setHeightForWidth(self.header_input_label_0.sizePolicy().hasHeightForWidth())
        # self.header_input_label_0.setSizePolicy(sizePolicy5)
        # self.header_input_label_0.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # self.gridLayout_17.addWidget(self.header_input_label_0, 0, 2, 1, 1)


        # self.gridLayout_10.addWidget(self.curr_frame_0, 0, 0, 1, 1)

        # self.curr_scroll_area_0.setWidget(self.curr_scroll_area_contents_0)

        # self.gridLayout_9.addWidget(self.curr_scroll_area_0, 0, 0, 1, 3)

        # self.currency_tabs.addTab(self.currency_tab_0, "")

        self.gridLayout_7.addWidget(self.currency_tabs, 1, 0, 1, 1)

        self.gridLayout_7.setRowStretch(0, 3)
        self.gridLayout_7.setRowStretch(1, 2)
        self.gridLayout_7.setColumnStretch(0, 2)
        self.gridLayout_7.setColumnStretch(1, 2)
        self.gridLayout_7.setColumnStretch(2, 3)

        self.gridLayout_13.addWidget(self.main_frame, 1, 0, 1, 1)

        self.input_file_frame = QFrame(ParserEditor)
        self.input_file_frame.setObjectName(u"input_file_frame")
        self.input_file_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.input_file_frame.setFrameShadow(QFrame.Shadow.Plain)
        self.gridLayout_5 = QGridLayout(self.input_file_frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.input_file_label = QLabel(self.input_file_frame)
        self.input_file_label.setObjectName(u"input_file_label")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.input_file_label.sizePolicy().hasHeightForWidth())
        self.input_file_label.setSizePolicy(sizePolicy7)

        self.gridLayout_5.addWidget(self.input_file_label, 0, 1, 1, 1)

        self.choose_file_button = QPushButton(self.input_file_frame)
        self.choose_file_button.setObjectName(u"choose_file_button")

        self.gridLayout_5.addWidget(self.choose_file_button, 0, 0, 1, 1)

        self.cancel_editing_button = QPushButton(self.input_file_frame)
        self.cancel_editing_button.setObjectName(u"cancel_editing_button")

        self.gridLayout_5.addWidget(self.cancel_editing_button, 0, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(1018, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.save_parser_button = QPushButton(self.input_file_frame)
        self.save_parser_button.setObjectName(u"save_parser_button")

        self.gridLayout_5.addWidget(self.save_parser_button, 0, 4, 1, 1)


        self.gridLayout_13.addWidget(self.input_file_frame, 2, 0, 1, 1)


        self.retranslateUi(ParserEditor)

        # self.pricebooks_list.setCurrentRow(-1)
        self.xlsx_tabs.setCurrentIndex(0)
        self.currency_tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ParserEditor)
    # setupUi

    def retranslateUi(self, ParserEditor):
        ParserEditor.setWindowTitle(QCoreApplication.translate("ParserEditor", u"Form", None))
        self.parser_name_label.setText(QCoreApplication.translate("ParserEditor", u"Name:", None))
        self.parser_name_line_edit.setPlaceholderText(QCoreApplication.translate("ParserEditor", u"new-parser", None))
        self.pricebooks_groupbox.setTitle(QCoreApplication.translate("ParserEditor", u"Pricebooks", None))
        self.pb_searchbar_line_edit.setInputMask("")
        self.pb_searchbar_line_edit.setText("")
        self.pb_searchbar_line_edit.setPlaceholderText(QCoreApplication.translate("ParserEditor", u"Search for pricebooks...", None))
        self.sort_button.setText(QCoreApplication.translate("ParserEditor", u"Sort", None))
        self.product_fields_frame.setTitle(QCoreApplication.translate("ParserEditor", u"Product2 Fields", None))
        self.functions_label.setText(QCoreApplication.translate("ParserEditor", u"Functions", None))
        self.source_label.setText(QCoreApplication.translate("ParserEditor", u"Source", None))
        self.allow_empty_label.setText(QCoreApplication.translate("ParserEditor", u"Allow Empty", None))
        self.product_fields_label.setText(QCoreApplication.translate("ParserEditor", u"Product Fields", None))
        self.xlsx_tabs.setTabText(self.xlsx_tabs.indexOf(self.xlsx_tab_0), QCoreApplication.translate("ParserEditor", u"Sheet1", None))
        # self.remove_curr_button_0.setText(QCoreApplication.translate("ParserEditor", u"Remove Currency", None))
        # self.add_curr_button_0.setText(QCoreApplication.translate("ParserEditor", u"Add Currency", None))
        # self.header_cf_label_0.setText(QCoreApplication.translate("ParserEditor", u"Conversion Factor", None))
        # self.header_curr_label_0.setText(QCoreApplication.translate("ParserEditor", u"Currency", None))
        # self.header_input_label_0.setText(QCoreApplication.translate("ParserEditor", u"Input Field", None))
        # self.currency_tabs.setTabText(self.currency_tabs.indexOf(self.currency_tab_0), QCoreApplication.translate("ParserEditor", u"new-pricebook", None))
        self.input_file_label.setText(QCoreApplication.translate("ParserEditor", u"Preview: - no file selected -", None))
        self.choose_file_button.setText(QCoreApplication.translate("ParserEditor", u"Choose file", None))
        self.cancel_editing_button.setText(QCoreApplication.translate("ParserEditor", u"Cancel", None))
        self.save_parser_button.setText(QCoreApplication.translate("ParserEditor", u"Save", None))
    # retranslateUi



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    widget = QWidget()
    ui = Ui_ParserEditor()
    ui.setupUi(widget)
    widget.show()

    sys.exit(app.exec())
    