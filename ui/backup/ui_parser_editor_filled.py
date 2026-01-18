# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'parser-filled-2.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHeaderView, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QTabWidget,
    QTableWidget, QTableWidgetItem, QWidget)

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

        self.pb_searchbar_line_edit = QLineEdit(self.pricebooks_groupbox)
        self.pb_searchbar_line_edit.setObjectName(u"pb_searchbar_line_edit")
        self.pb_searchbar_line_edit.setMinimumSize(QSize(0, 0))

        self.gridLayout_3.addWidget(self.pb_searchbar_line_edit, 0, 1, 1, 1)

        self.pricebooks_list = QListWidget(self.pricebooks_groupbox)
        __qlistwidgetitem = QListWidgetItem(self.pricebooks_list)
        __qlistwidgetitem.setCheckState(Qt.Checked);
        __qlistwidgetitem1 = QListWidgetItem(self.pricebooks_list)
        __qlistwidgetitem1.setCheckState(Qt.Checked);
        __qlistwidgetitem2 = QListWidgetItem(self.pricebooks_list)
        __qlistwidgetitem2.setCheckState(Qt.Unchecked);
        self.pricebooks_list.setObjectName(u"pricebooks_list")
        self.pricebooks_list.setSpacing(0)
        self.pricebooks_list.setSortingEnabled(False)

        self.gridLayout_3.addWidget(self.pricebooks_list, 1, 0, 1, 3)

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
        self._4_include_field = QCheckBox(self.product_fields_scroll_area_contents)
        self._4_include_field.setObjectName(u"_4_include_field")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self._4_include_field.sizePolicy().hasHeightForWidth())
        self._4_include_field.setSizePolicy(sizePolicy7)
        self._4_include_field.setMinimumSize(QSize(16, 0))
        font2 = QFont()
        font2.setStrikeOut(False)
        self._4_include_field.setFont(font2)
        self._4_include_field.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self._4_include_field.setChecked(False)

        self.gridLayout_2.addWidget(self._4_include_field, 4, 0, 1, 1)

        self._2_include_field = QCheckBox(self.product_fields_scroll_area_contents)
        self._2_include_field.setObjectName(u"_2_include_field")
        sizePolicy7.setHeightForWidth(self._2_include_field.sizePolicy().hasHeightForWidth())
        self._2_include_field.setSizePolicy(sizePolicy7)
        self._2_include_field.setMinimumSize(QSize(16, 0))
        self._2_include_field.setFont(font2)
        self._2_include_field.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self._2_include_field.setChecked(True)

        self.gridLayout_2.addWidget(self._2_include_field, 2, 0, 1, 1)

        self._3_allow_empty = QCheckBox(self.product_fields_scroll_area_contents)
        self._3_allow_empty.setObjectName(u"_3_allow_empty")
        sizePolicy7.setHeightForWidth(self._3_allow_empty.sizePolicy().hasHeightForWidth())
        self._3_allow_empty.setSizePolicy(sizePolicy7)
        self._3_allow_empty.setMinimumSize(QSize(16, 0))
        self._3_allow_empty.setFont(font2)
        self._3_allow_empty.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout_2.addWidget(self._3_allow_empty, 3, 4, 1, 1)

        self._3_prod_field = QLabel(self.product_fields_scroll_area_contents)
        self._3_prod_field.setObjectName(u"_3_prod_field")
        sizePolicy7.setHeightForWidth(self._3_prod_field.sizePolicy().hasHeightForWidth())
        self._3_prod_field.setSizePolicy(sizePolicy7)
        self._3_prod_field.setMinimumSize(QSize(0, 0))
        self._3_prod_field.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self._3_prod_field, 3, 1, 1, 1)

        self._0_prod_field = QLabel(self.product_fields_scroll_area_contents)
        self._0_prod_field.setObjectName(u"_0_prod_field")
        sizePolicy7.setHeightForWidth(self._0_prod_field.sizePolicy().hasHeightForWidth())
        self._0_prod_field.setSizePolicy(sizePolicy7)
        self._0_prod_field.setMinimumSize(QSize(0, 0))
        self._0_prod_field.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self._0_prod_field, 0, 1, 1, 1)

        self._2_function_combo = QComboBox(self.product_fields_scroll_area_contents)
        self._2_function_combo.setObjectName(u"_2_function_combo")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self._2_function_combo.sizePolicy().hasHeightForWidth())
        self._2_function_combo.setSizePolicy(sizePolicy8)
        self._2_function_combo.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_2.addWidget(self._2_function_combo, 2, 3, 1, 1)

        self._4_prod_field = QLabel(self.product_fields_scroll_area_contents)
        self._4_prod_field.setObjectName(u"_4_prod_field")
        self._4_prod_field.setEnabled(False)
        sizePolicy7.setHeightForWidth(self._4_prod_field.sizePolicy().hasHeightForWidth())
        self._4_prod_field.setSizePolicy(sizePolicy7)
        self._4_prod_field.setMinimumSize(QSize(0, 0))
        self._4_prod_field.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self._4_prod_field, 4, 1, 1, 1)

        self._1_function_combo = QComboBox(self.product_fields_scroll_area_contents)
        self._1_function_combo.addItem("")
        self._1_function_combo.setObjectName(u"_1_function_combo")
        sizePolicy8.setHeightForWidth(self._1_function_combo.sizePolicy().hasHeightForWidth())
        self._1_function_combo.setSizePolicy(sizePolicy8)
        self._1_function_combo.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_2.addWidget(self._1_function_combo, 1, 3, 1, 1)

        self._3_source_combo = QComboBox(self.product_fields_scroll_area_contents)
        self._3_source_combo.setObjectName(u"_3_source_combo")
        sizePolicy8.setHeightForWidth(self._3_source_combo.sizePolicy().hasHeightForWidth())
        self._3_source_combo.setSizePolicy(sizePolicy8)
        self._3_source_combo.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_2.addWidget(self._3_source_combo, 3, 2, 1, 1)

        self._2_allow_empty = QCheckBox(self.product_fields_scroll_area_contents)
        self._2_allow_empty.setObjectName(u"_2_allow_empty")
        sizePolicy7.setHeightForWidth(self._2_allow_empty.sizePolicy().hasHeightForWidth())
        self._2_allow_empty.setSizePolicy(sizePolicy7)
        self._2_allow_empty.setMinimumSize(QSize(16, 0))
        self._2_allow_empty.setFont(font2)
        self._2_allow_empty.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout_2.addWidget(self._2_allow_empty, 2, 4, 1, 1)

        self._4_source_combo = QComboBox(self.product_fields_scroll_area_contents)
        self._4_source_combo.setObjectName(u"_4_source_combo")
        self._4_source_combo.setEnabled(False)
        sizePolicy8.setHeightForWidth(self._4_source_combo.sizePolicy().hasHeightForWidth())
        self._4_source_combo.setSizePolicy(sizePolicy8)
        self._4_source_combo.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_2.addWidget(self._4_source_combo, 4, 2, 1, 1)

        self._1_prod_field = QLabel(self.product_fields_scroll_area_contents)
        self._1_prod_field.setObjectName(u"_1_prod_field")
        sizePolicy7.setHeightForWidth(self._1_prod_field.sizePolicy().hasHeightForWidth())
        self._1_prod_field.setSizePolicy(sizePolicy7)
        self._1_prod_field.setMinimumSize(QSize(0, 0))
        self._1_prod_field.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self._1_prod_field, 1, 1, 1, 1)

        self._2_prod_field = QLabel(self.product_fields_scroll_area_contents)
        self._2_prod_field.setObjectName(u"_2_prod_field")
        sizePolicy7.setHeightForWidth(self._2_prod_field.sizePolicy().hasHeightForWidth())
        self._2_prod_field.setSizePolicy(sizePolicy7)
        self._2_prod_field.setMinimumSize(QSize(0, 0))
        self._2_prod_field.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self._2_prod_field, 2, 1, 1, 1)

        self._1_include_field = QCheckBox(self.product_fields_scroll_area_contents)
        self._1_include_field.setObjectName(u"_1_include_field")
        sizePolicy7.setHeightForWidth(self._1_include_field.sizePolicy().hasHeightForWidth())
        self._1_include_field.setSizePolicy(sizePolicy7)
        self._1_include_field.setMinimumSize(QSize(16, 0))
        self._1_include_field.setFont(font2)
        self._1_include_field.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self._1_include_field.setChecked(True)

        self.gridLayout_2.addWidget(self._1_include_field, 1, 0, 1, 1)

        self._2_source_combo = QComboBox(self.product_fields_scroll_area_contents)
        self._2_source_combo.setObjectName(u"_2_source_combo")
        sizePolicy8.setHeightForWidth(self._2_source_combo.sizePolicy().hasHeightForWidth())
        self._2_source_combo.setSizePolicy(sizePolicy8)
        self._2_source_combo.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_2.addWidget(self._2_source_combo, 2, 2, 1, 1)

        self._0_function_combo = QComboBox(self.product_fields_scroll_area_contents)
        self._0_function_combo.addItem("")
        self._0_function_combo.setObjectName(u"_0_function_combo")
        self._0_function_combo.setEnabled(False)
        sizePolicy8.setHeightForWidth(self._0_function_combo.sizePolicy().hasHeightForWidth())
        self._0_function_combo.setSizePolicy(sizePolicy8)
        self._0_function_combo.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_2.addWidget(self._0_function_combo, 0, 3, 1, 1)

        self._1_source_combo = QComboBox(self.product_fields_scroll_area_contents)
        self._1_source_combo.addItem("")
        self._1_source_combo.setObjectName(u"_1_source_combo")
        self._1_source_combo.setEnabled(False)
        sizePolicy8.setHeightForWidth(self._1_source_combo.sizePolicy().hasHeightForWidth())
        self._1_source_combo.setSizePolicy(sizePolicy8)
        self._1_source_combo.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_2.addWidget(self._1_source_combo, 1, 2, 1, 1)

        self._0_source_combo = QComboBox(self.product_fields_scroll_area_contents)
        self._0_source_combo.addItem("")
        self._0_source_combo.addItem("")
        self._0_source_combo.setObjectName(u"_0_source_combo")
        sizePolicy8.setHeightForWidth(self._0_source_combo.sizePolicy().hasHeightForWidth())
        self._0_source_combo.setSizePolicy(sizePolicy8)
        self._0_source_combo.setMaximumSize(QSize(200, 16777215))
        self._0_source_combo.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self._0_source_combo.setFrame(True)
        self._0_source_combo.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.gridLayout_2.addWidget(self._0_source_combo, 0, 2, 1, 1)

        self._4_allow_empty = QCheckBox(self.product_fields_scroll_area_contents)
        self._4_allow_empty.setObjectName(u"_4_allow_empty")
        self._4_allow_empty.setEnabled(False)
        sizePolicy7.setHeightForWidth(self._4_allow_empty.sizePolicy().hasHeightForWidth())
        self._4_allow_empty.setSizePolicy(sizePolicy7)
        self._4_allow_empty.setMinimumSize(QSize(16, 0))
        self._4_allow_empty.setFont(font2)
        self._4_allow_empty.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout_2.addWidget(self._4_allow_empty, 4, 4, 1, 1)

        self._3_include_field = QCheckBox(self.product_fields_scroll_area_contents)
        self._3_include_field.setObjectName(u"_3_include_field")
        sizePolicy7.setHeightForWidth(self._3_include_field.sizePolicy().hasHeightForWidth())
        self._3_include_field.setSizePolicy(sizePolicy7)
        self._3_include_field.setMinimumSize(QSize(16, 0))
        self._3_include_field.setFont(font2)
        self._3_include_field.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self._3_include_field.setChecked(True)

        self.gridLayout_2.addWidget(self._3_include_field, 3, 0, 1, 1)

        self._4_function_combo = QComboBox(self.product_fields_scroll_area_contents)
        self._4_function_combo.setObjectName(u"_4_function_combo")
        self._4_function_combo.setEnabled(False)
        sizePolicy8.setHeightForWidth(self._4_function_combo.sizePolicy().hasHeightForWidth())
        self._4_function_combo.setSizePolicy(sizePolicy8)
        self._4_function_combo.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_2.addWidget(self._4_function_combo, 4, 3, 1, 1)

        self._0_allow_empty = QCheckBox(self.product_fields_scroll_area_contents)
        self._0_allow_empty.setObjectName(u"_0_allow_empty")
        sizePolicy7.setHeightForWidth(self._0_allow_empty.sizePolicy().hasHeightForWidth())
        self._0_allow_empty.setSizePolicy(sizePolicy7)
        self._0_allow_empty.setMinimumSize(QSize(16, 0))
        self._0_allow_empty.setMaximumSize(QSize(16777215, 16777215))
        self._0_allow_empty.setFont(font2)
        self._0_allow_empty.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self._0_allow_empty.setChecked(True)

        self.gridLayout_2.addWidget(self._0_allow_empty, 0, 4, 1, 1)

        self._1_allow_empty = QCheckBox(self.product_fields_scroll_area_contents)
        self._1_allow_empty.setObjectName(u"_1_allow_empty")
        sizePolicy7.setHeightForWidth(self._1_allow_empty.sizePolicy().hasHeightForWidth())
        self._1_allow_empty.setSizePolicy(sizePolicy7)
        self._1_allow_empty.setMinimumSize(QSize(16, 0))
        self._1_allow_empty.setFont(font2)
        self._1_allow_empty.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self._1_allow_empty.setChecked(True)

        self.gridLayout_2.addWidget(self._1_allow_empty, 1, 4, 1, 1)

        self._0_include_field = QCheckBox(self.product_fields_scroll_area_contents)
        self._0_include_field.setObjectName(u"_0_include_field")
        sizePolicy7.setHeightForWidth(self._0_include_field.sizePolicy().hasHeightForWidth())
        self._0_include_field.setSizePolicy(sizePolicy7)
        self._0_include_field.setMinimumSize(QSize(16, 0))
        self._0_include_field.setMaximumSize(QSize(16777215, 16777215))
        self._0_include_field.setFont(font2)
        self._0_include_field.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self._0_include_field.setChecked(True)

        self.gridLayout_2.addWidget(self._0_include_field, 0, 0, 1, 1)

        self._3_function_combo = QComboBox(self.product_fields_scroll_area_contents)
        self._3_function_combo.setObjectName(u"_3_function_combo")
        sizePolicy8.setHeightForWidth(self._3_function_combo.sizePolicy().hasHeightForWidth())
        self._3_function_combo.setSizePolicy(sizePolicy8)
        self._3_function_combo.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_2.addWidget(self._3_function_combo, 3, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 5, 0, 1, 4)

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
        if (self.xlsx_table_0.columnCount() < 6):
            self.xlsx_table_0.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.xlsx_table_0.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.xlsx_table_0.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.xlsx_table_0.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.xlsx_table_0.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.xlsx_table_0.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.xlsx_table_0.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.xlsx_table_0.rowCount() < 5):
            self.xlsx_table_0.setRowCount(5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.xlsx_table_0.setVerticalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.xlsx_table_0.setVerticalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.xlsx_table_0.setVerticalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.xlsx_table_0.setVerticalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.xlsx_table_0.setVerticalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.xlsx_table_0.setItem(0, 0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.xlsx_table_0.setItem(0, 1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.xlsx_table_0.setItem(0, 2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.xlsx_table_0.setItem(0, 3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.xlsx_table_0.setItem(0, 4, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.xlsx_table_0.setItem(0, 5, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.xlsx_table_0.setItem(1, 0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.xlsx_table_0.setItem(1, 1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.xlsx_table_0.setItem(1, 2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.xlsx_table_0.setItem(1, 3, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.xlsx_table_0.setItem(1, 4, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.xlsx_table_0.setItem(1, 5, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.xlsx_table_0.setItem(2, 0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.xlsx_table_0.setItem(2, 1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.xlsx_table_0.setItem(2, 2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.xlsx_table_0.setItem(2, 3, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.xlsx_table_0.setItem(2, 4, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.xlsx_table_0.setItem(2, 5, __qtablewidgetitem28)
        self.xlsx_table_0.setObjectName(u"xlsx_table_0")
        self.xlsx_table_0.setRowCount(5)

        self.gridLayout_11.addWidget(self.xlsx_table_0, 0, 0, 1, 1)

        self.xlsx_tabs.addTab(self.xlsx_tab_0, "")
        self.xlsx_tab_1 = QWidget()
        self.xlsx_tab_1.setObjectName(u"xlsx_tab_1")
        self.gridLayout_12 = QGridLayout(self.xlsx_tab_1)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.xlsx_table_1 = QTableWidget(self.xlsx_tab_1)
        if (self.xlsx_table_1.columnCount() < 5):
            self.xlsx_table_1.setColumnCount(5)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.xlsx_table_1.setHorizontalHeaderItem(0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.xlsx_table_1.setHorizontalHeaderItem(1, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.xlsx_table_1.setHorizontalHeaderItem(2, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.xlsx_table_1.setHorizontalHeaderItem(3, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.xlsx_table_1.setHorizontalHeaderItem(4, __qtablewidgetitem33)
        if (self.xlsx_table_1.rowCount() < 5):
            self.xlsx_table_1.setRowCount(5)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.xlsx_table_1.setVerticalHeaderItem(0, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.xlsx_table_1.setVerticalHeaderItem(1, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.xlsx_table_1.setVerticalHeaderItem(2, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.xlsx_table_1.setVerticalHeaderItem(3, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.xlsx_table_1.setVerticalHeaderItem(4, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.xlsx_table_1.setItem(0, 0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.xlsx_table_1.setItem(0, 1, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.xlsx_table_1.setItem(0, 2, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.xlsx_table_1.setItem(0, 3, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.xlsx_table_1.setItem(0, 4, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.xlsx_table_1.setItem(1, 0, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.xlsx_table_1.setItem(1, 1, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.xlsx_table_1.setItem(1, 2, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.xlsx_table_1.setItem(1, 3, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.xlsx_table_1.setItem(1, 4, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.xlsx_table_1.setItem(2, 0, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.xlsx_table_1.setItem(2, 1, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.xlsx_table_1.setItem(2, 2, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.xlsx_table_1.setItem(2, 3, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.xlsx_table_1.setItem(2, 4, __qtablewidgetitem53)
        self.xlsx_table_1.setObjectName(u"xlsx_table_1")
        self.xlsx_table_1.setRowCount(5)

        self.gridLayout_12.addWidget(self.xlsx_table_1, 0, 0, 1, 1)

        self.xlsx_tabs.addTab(self.xlsx_tab_1, "")

        self.gridLayout_7.addWidget(self.xlsx_tabs, 0, 2, 2, 1)

        self.currecy_tabs = QTabWidget(self.main_frame)
        self.currecy_tabs.setObjectName(u"currecy_tabs")
        self.currecy_tabs.setMinimumSize(QSize(371, 0))
        self.currency_tab_0 = QWidget()
        self.currency_tab_0.setObjectName(u"currency_tab_0")
        self.gridLayout_9 = QGridLayout(self.currency_tab_0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.remove_curr_button_0 = QPushButton(self.currency_tab_0)
        self.remove_curr_button_0.setObjectName(u"remove_curr_button_0")

        self.gridLayout_9.addWidget(self.remove_curr_button_0, 1, 1, 1, 1)

        self.add_curr_button_0 = QPushButton(self.currency_tab_0)
        self.add_curr_button_0.setObjectName(u"add_curr_button_0")

        self.gridLayout_9.addWidget(self.add_curr_button_0, 1, 2, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(133, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_11, 1, 0, 1, 1)

        self.curr_scroll_area_0 = QScrollArea(self.currency_tab_0)
        self.curr_scroll_area_0.setObjectName(u"curr_scroll_area_0")
        sizePolicy3.setHeightForWidth(self.curr_scroll_area_0.sizePolicy().hasHeightForWidth())
        self.curr_scroll_area_0.setSizePolicy(sizePolicy3)
        self.curr_scroll_area_0.setFrameShape(QFrame.Shape.NoFrame)
        self.curr_scroll_area_0.setWidgetResizable(True)
        self.curr_scroll_area_contents_0 = QWidget()
        self.curr_scroll_area_contents_0.setObjectName(u"curr_scroll_area_contents_0")
        self.curr_scroll_area_contents_0.setGeometry(QRect(0, 0, 379, 186))
        self.gridLayout_10 = QGridLayout(self.curr_scroll_area_contents_0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.curr_frame_0 = QFrame(self.curr_scroll_area_contents_0)
        self.curr_frame_0.setObjectName(u"curr_frame_0")
        sizePolicy3.setHeightForWidth(self.curr_frame_0.sizePolicy().hasHeightForWidth())
        self.curr_frame_0.setSizePolicy(sizePolicy3)
        self.curr_frame_0.setAutoFillBackground(False)
        self.curr_frame_0.setFrameShape(QFrame.Shape.StyledPanel)
        self.curr_frame_0.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_17 = QGridLayout(self.curr_frame_0)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.inluce_currency_10 = QCheckBox(self.curr_frame_0)
        self.inluce_currency_10.setObjectName(u"inluce_currency_10")

        self.gridLayout_17.addWidget(self.inluce_currency_10, 3, 0, 1, 1)

        self.header_input_label_0 = QLabel(self.curr_frame_0)
        self.header_input_label_0.setObjectName(u"header_input_label_0")
        sizePolicy5.setHeightForWidth(self.header_input_label_0.sizePolicy().hasHeightForWidth())
        self.header_input_label_0.setSizePolicy(sizePolicy5)
        self.header_input_label_0.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_17.addWidget(self.header_input_label_0, 0, 2, 1, 1)

        self.curr_field_combo_01 = QComboBox(self.curr_frame_0)
        self.curr_field_combo_01.addItem("")
        self.curr_field_combo_01.addItem("")
        self.curr_field_combo_01.setObjectName(u"curr_field_combo_01")
        sizePolicy8.setHeightForWidth(self.curr_field_combo_01.sizePolicy().hasHeightForWidth())
        self.curr_field_combo_01.setSizePolicy(sizePolicy8)
        self.curr_field_combo_01.setMaximumSize(QSize(200, 16777215))
        self.curr_field_combo_01.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.curr_field_combo_01.setFrame(True)
        self.curr_field_combo_01.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.gridLayout_17.addWidget(self.curr_field_combo_01, 3, 2, 1, 2)

        self.curr_split_line_0 = QFrame(self.curr_frame_0)
        self.curr_split_line_0.setObjectName(u"curr_split_line_0")
        sizePolicy5.setHeightForWidth(self.curr_split_line_0.sizePolicy().hasHeightForWidth())
        self.curr_split_line_0.setSizePolicy(sizePolicy5)
        self.curr_split_line_0.setFrameShape(QFrame.Shape.HLine)
        self.curr_split_line_0.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_17.addWidget(self.curr_split_line_0, 1, 0, 1, 5)

        self.curr_label_01 = QLabel(self.curr_frame_0)
        self.curr_label_01.setObjectName(u"curr_label_01")
        sizePolicy5.setHeightForWidth(self.curr_label_01.sizePolicy().hasHeightForWidth())
        self.curr_label_01.setSizePolicy(sizePolicy5)
        self.curr_label_01.setMinimumSize(QSize(50, 0))
        self.curr_label_01.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_17.addWidget(self.curr_label_01, 3, 1, 1, 1)

        self.header_cf_label_0 = QLabel(self.curr_frame_0)
        self.header_cf_label_0.setObjectName(u"header_cf_label_0")
        sizePolicy5.setHeightForWidth(self.header_cf_label_0.sizePolicy().hasHeightForWidth())
        self.header_cf_label_0.setSizePolicy(sizePolicy5)
        self.header_cf_label_0.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_17.addWidget(self.header_cf_label_0, 0, 3, 1, 2)

        self.curr_label_00 = QLabel(self.curr_frame_0)
        self.curr_label_00.setObjectName(u"curr_label_00")
        sizePolicy5.setHeightForWidth(self.curr_label_00.sizePolicy().hasHeightForWidth())
        self.curr_label_00.setSizePolicy(sizePolicy5)
        self.curr_label_00.setMinimumSize(QSize(50, 0))
        self.curr_label_00.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_17.addWidget(self.curr_label_00, 2, 1, 1, 1)

        self.c_factor_ledit_00 = QLineEdit(self.curr_frame_0)
        self.c_factor_ledit_00.setObjectName(u"c_factor_ledit_00")

        self.gridLayout_17.addWidget(self.c_factor_ledit_00, 2, 4, 1, 1)

        self.header_curr_label_0 = QLabel(self.curr_frame_0)
        self.header_curr_label_0.setObjectName(u"header_curr_label_0")
        sizePolicy5.setHeightForWidth(self.header_curr_label_0.sizePolicy().hasHeightForWidth())
        self.header_curr_label_0.setSizePolicy(sizePolicy5)
        self.header_curr_label_0.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_17.addWidget(self.header_curr_label_0, 0, 0, 1, 2)

        self.c_factor_ledit_01 = QLineEdit(self.curr_frame_0)
        self.c_factor_ledit_01.setObjectName(u"c_factor_ledit_01")

        self.gridLayout_17.addWidget(self.c_factor_ledit_01, 3, 4, 1, 1)

        self.include_currency_00 = QCheckBox(self.curr_frame_0)
        self.include_currency_00.setObjectName(u"include_currency_00")
        sizePolicy5.setHeightForWidth(self.include_currency_00.sizePolicy().hasHeightForWidth())
        self.include_currency_00.setSizePolicy(sizePolicy5)
        self.include_currency_00.setChecked(True)

        self.gridLayout_17.addWidget(self.include_currency_00, 2, 0, 1, 1)

        self.curr_field_combo_00 = QComboBox(self.curr_frame_0)
        self.curr_field_combo_00.addItem("")
        self.curr_field_combo_00.addItem("")
        self.curr_field_combo_00.setObjectName(u"curr_field_combo_00")
        sizePolicy8.setHeightForWidth(self.curr_field_combo_00.sizePolicy().hasHeightForWidth())
        self.curr_field_combo_00.setSizePolicy(sizePolicy8)
        self.curr_field_combo_00.setMaximumSize(QSize(200, 16777215))
        self.curr_field_combo_00.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.curr_field_combo_00.setFrame(True)
        self.curr_field_combo_00.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.gridLayout_17.addWidget(self.curr_field_combo_00, 2, 2, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_17.addItem(self.verticalSpacer_2, 4, 2, 1, 1)


        self.gridLayout_10.addWidget(self.curr_frame_0, 0, 0, 1, 1)

        self.curr_scroll_area_0.setWidget(self.curr_scroll_area_contents_0)

        self.gridLayout_9.addWidget(self.curr_scroll_area_0, 0, 0, 1, 3)

        self.currecy_tabs.addTab(self.currency_tab_0, "")
        self.currency_tab_1 = QWidget()
        self.currency_tab_1.setObjectName(u"currency_tab_1")
        self.gridLayout_8 = QGridLayout(self.currency_tab_1)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.curr_scroll_area_1 = QScrollArea(self.currency_tab_1)
        self.curr_scroll_area_1.setObjectName(u"curr_scroll_area_1")
        sizePolicy3.setHeightForWidth(self.curr_scroll_area_1.sizePolicy().hasHeightForWidth())
        self.curr_scroll_area_1.setSizePolicy(sizePolicy3)
        self.curr_scroll_area_1.setFrameShape(QFrame.Shape.NoFrame)
        self.curr_scroll_area_1.setWidgetResizable(True)
        self.curr_scroll_area_contents_1 = QWidget()
        self.curr_scroll_area_contents_1.setObjectName(u"curr_scroll_area_contents_1")
        self.curr_scroll_area_contents_1.setGeometry(QRect(0, 0, 379, 186))
        self.gridLayout = QGridLayout(self.curr_scroll_area_contents_1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.curr_frame_1 = QFrame(self.curr_scroll_area_contents_1)
        self.curr_frame_1.setObjectName(u"curr_frame_1")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.curr_frame_1.sizePolicy().hasHeightForWidth())
        self.curr_frame_1.setSizePolicy(sizePolicy9)
        self.curr_frame_1.setAutoFillBackground(False)
        self.curr_frame_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.curr_frame_1.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_18 = QGridLayout(self.curr_frame_1)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.include_curr_10 = QCheckBox(self.curr_frame_1)
        self.include_curr_10.setObjectName(u"include_curr_10")
        sizePolicy5.setHeightForWidth(self.include_curr_10.sizePolicy().hasHeightForWidth())
        self.include_curr_10.setSizePolicy(sizePolicy5)
        self.include_curr_10.setChecked(True)

        self.gridLayout_18.addWidget(self.include_curr_10, 2, 0, 1, 1)

        self.curr_label_12 = QLabel(self.curr_frame_1)
        self.curr_label_12.setObjectName(u"curr_label_12")
        sizePolicy5.setHeightForWidth(self.curr_label_12.sizePolicy().hasHeightForWidth())
        self.curr_label_12.setSizePolicy(sizePolicy5)
        self.curr_label_12.setMinimumSize(QSize(50, 0))
        self.curr_label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_18.addWidget(self.curr_label_12, 4, 1, 1, 1)

        self.curr_label_10 = QLabel(self.curr_frame_1)
        self.curr_label_10.setObjectName(u"curr_label_10")
        sizePolicy5.setHeightForWidth(self.curr_label_10.sizePolicy().hasHeightForWidth())
        self.curr_label_10.setSizePolicy(sizePolicy5)
        self.curr_label_10.setMinimumSize(QSize(50, 0))
        self.curr_label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_18.addWidget(self.curr_label_10, 2, 1, 1, 1)

        self.c_factor_ledit_12 = QLineEdit(self.curr_frame_1)
        self.c_factor_ledit_12.setObjectName(u"c_factor_ledit_12")

        self.gridLayout_18.addWidget(self.c_factor_ledit_12, 4, 4, 1, 1)

        self.include_curr_12 = QCheckBox(self.curr_frame_1)
        self.include_curr_12.setObjectName(u"include_curr_12")

        self.gridLayout_18.addWidget(self.include_curr_12, 4, 0, 1, 1)

        self.c_factor_ledit_10 = QLineEdit(self.curr_frame_1)
        self.c_factor_ledit_10.setObjectName(u"c_factor_ledit_10")

        self.gridLayout_18.addWidget(self.c_factor_ledit_10, 2, 4, 1, 1)

        self.header_cf_label_1 = QLabel(self.curr_frame_1)
        self.header_cf_label_1.setObjectName(u"header_cf_label_1")
        sizePolicy5.setHeightForWidth(self.header_cf_label_1.sizePolicy().hasHeightForWidth())
        self.header_cf_label_1.setSizePolicy(sizePolicy5)
        self.header_cf_label_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_18.addWidget(self.header_cf_label_1, 0, 3, 1, 2)

        self.include_curr_11 = QCheckBox(self.curr_frame_1)
        self.include_curr_11.setObjectName(u"include_curr_11")

        self.gridLayout_18.addWidget(self.include_curr_11, 3, 0, 1, 1)

        self.header_input_label_1 = QLabel(self.curr_frame_1)
        self.header_input_label_1.setObjectName(u"header_input_label_1")
        sizePolicy5.setHeightForWidth(self.header_input_label_1.sizePolicy().hasHeightForWidth())
        self.header_input_label_1.setSizePolicy(sizePolicy5)
        self.header_input_label_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_18.addWidget(self.header_input_label_1, 0, 2, 1, 1)

        self.c_factor_ledit_11 = QLineEdit(self.curr_frame_1)
        self.c_factor_ledit_11.setObjectName(u"c_factor_ledit_11")

        self.gridLayout_18.addWidget(self.c_factor_ledit_11, 3, 4, 1, 1)

        self.curr_label_11 = QLabel(self.curr_frame_1)
        self.curr_label_11.setObjectName(u"curr_label_11")
        sizePolicy5.setHeightForWidth(self.curr_label_11.sizePolicy().hasHeightForWidth())
        self.curr_label_11.setSizePolicy(sizePolicy5)
        self.curr_label_11.setMinimumSize(QSize(50, 0))
        self.curr_label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_18.addWidget(self.curr_label_11, 3, 1, 1, 1)

        self.curr_field_combo_11 = QComboBox(self.curr_frame_1)
        self.curr_field_combo_11.addItem("")
        self.curr_field_combo_11.addItem("")
        self.curr_field_combo_11.setObjectName(u"curr_field_combo_11")
        sizePolicy8.setHeightForWidth(self.curr_field_combo_11.sizePolicy().hasHeightForWidth())
        self.curr_field_combo_11.setSizePolicy(sizePolicy8)
        self.curr_field_combo_11.setMaximumSize(QSize(200, 16777215))
        self.curr_field_combo_11.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.curr_field_combo_11.setFrame(True)
        self.curr_field_combo_11.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.gridLayout_18.addWidget(self.curr_field_combo_11, 3, 2, 1, 2)

        self.header_curr_label_1 = QLabel(self.curr_frame_1)
        self.header_curr_label_1.setObjectName(u"header_curr_label_1")
        sizePolicy5.setHeightForWidth(self.header_curr_label_1.sizePolicy().hasHeightForWidth())
        self.header_curr_label_1.setSizePolicy(sizePolicy5)
        self.header_curr_label_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_18.addWidget(self.header_curr_label_1, 0, 0, 1, 2)

        self.curr_field_combo_10 = QComboBox(self.curr_frame_1)
        self.curr_field_combo_10.addItem("")
        self.curr_field_combo_10.addItem("")
        self.curr_field_combo_10.setObjectName(u"curr_field_combo_10")
        sizePolicy8.setHeightForWidth(self.curr_field_combo_10.sizePolicy().hasHeightForWidth())
        self.curr_field_combo_10.setSizePolicy(sizePolicy8)
        self.curr_field_combo_10.setMaximumSize(QSize(200, 16777215))
        self.curr_field_combo_10.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.curr_field_combo_10.setFrame(True)
        self.curr_field_combo_10.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.gridLayout_18.addWidget(self.curr_field_combo_10, 2, 2, 1, 2)

        self.curr_split_line_1 = QFrame(self.curr_frame_1)
        self.curr_split_line_1.setObjectName(u"curr_split_line_1")
        sizePolicy5.setHeightForWidth(self.curr_split_line_1.sizePolicy().hasHeightForWidth())
        self.curr_split_line_1.setSizePolicy(sizePolicy5)
        self.curr_split_line_1.setFrameShape(QFrame.Shape.HLine)
        self.curr_split_line_1.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_18.addWidget(self.curr_split_line_1, 1, 0, 1, 5)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_18.addItem(self.verticalSpacer_3, 5, 2, 1, 1)

        self.curr_field_combo_12 = QComboBox(self.curr_frame_1)
        self.curr_field_combo_12.addItem("")
        self.curr_field_combo_12.addItem("")
        self.curr_field_combo_12.setObjectName(u"curr_field_combo_12")
        sizePolicy8.setHeightForWidth(self.curr_field_combo_12.sizePolicy().hasHeightForWidth())
        self.curr_field_combo_12.setSizePolicy(sizePolicy8)
        self.curr_field_combo_12.setMaximumSize(QSize(200, 16777215))
        self.curr_field_combo_12.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.curr_field_combo_12.setFrame(True)
        self.curr_field_combo_12.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.gridLayout_18.addWidget(self.curr_field_combo_12, 4, 2, 1, 2)


        self.gridLayout.addWidget(self.curr_frame_1, 0, 0, 1, 1)

        self.curr_scroll_area_1.setWidget(self.curr_scroll_area_contents_1)

        self.gridLayout_8.addWidget(self.curr_scroll_area_1, 0, 0, 1, 3)

        self.horizontalSpacer_10 = QSpacerItem(133, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_10, 1, 0, 1, 1)

        self.remove_curr_button_1 = QPushButton(self.currency_tab_1)
        self.remove_curr_button_1.setObjectName(u"remove_curr_button_1")
        self.remove_curr_button_1.setEnabled(False)

        self.gridLayout_8.addWidget(self.remove_curr_button_1, 1, 1, 1, 1)

        self.add_curr_button_1 = QPushButton(self.currency_tab_1)
        self.add_curr_button_1.setObjectName(u"add_curr_button_1")

        self.gridLayout_8.addWidget(self.add_curr_button_1, 1, 2, 1, 1)

        self.currecy_tabs.addTab(self.currency_tab_1, "")

        self.gridLayout_7.addWidget(self.currecy_tabs, 1, 0, 1, 1)

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
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.input_file_label.sizePolicy().hasHeightForWidth())
        self.input_file_label.setSizePolicy(sizePolicy10)

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

        self.pricebooks_list.setCurrentRow(0)
        self.xlsx_tabs.setCurrentIndex(1)
        self.currecy_tabs.setCurrentIndex(1)


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

        __sortingEnabled = self.pricebooks_list.isSortingEnabled()
        self.pricebooks_list.setSortingEnabled(False)
        ___qlistwidgetitem = self.pricebooks_list.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("ParserEditor", u"pb-01", None));
        ___qlistwidgetitem1 = self.pricebooks_list.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("ParserEditor", u"pb-02", None));
        ___qlistwidgetitem2 = self.pricebooks_list.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("ParserEditor", u"pb-03", None));
        self.pricebooks_list.setSortingEnabled(__sortingEnabled)

        self.sort_button.setText(QCoreApplication.translate("ParserEditor", u"Sort", None))
        self.product_fields_frame.setTitle(QCoreApplication.translate("ParserEditor", u"Product2 Fields", None))
        self.functions_label.setText(QCoreApplication.translate("ParserEditor", u"Functions", None))
        self.source_label.setText(QCoreApplication.translate("ParserEditor", u"Source", None))
        self.allow_empty_label.setText(QCoreApplication.translate("ParserEditor", u"Allow Empty", None))
        self._4_include_field.setText("")
        self._2_include_field.setText("")
        self._3_allow_empty.setText("")
        self._3_prod_field.setText(QCoreApplication.translate("ParserEditor", u"sf_manu:", None))
        self._0_prod_field.setText(QCoreApplication.translate("ParserEditor", u"sf_id:", None))
        self._4_prod_field.setText(QCoreApplication.translate("ParserEditor", u"sf_desc:", None))
        self._1_function_combo.setItemText(0, QCoreApplication.translate("ParserEditor", u"SPLIT", None))

        self._2_allow_empty.setText("")
        self._1_prod_field.setText(QCoreApplication.translate("ParserEditor", u"sf_name:", None))
        self._2_prod_field.setText(QCoreApplication.translate("ParserEditor", u"sf_SKU:", None))
        self._1_include_field.setText("")
        self._0_function_combo.setItemText(0, QCoreApplication.translate("ParserEditor", u"-none-", None))

        self._1_source_combo.setItemText(0, QCoreApplication.translate("ParserEditor", u"-none-", None))

        self._0_source_combo.setItemText(0, QCoreApplication.translate("ParserEditor", u"id (sheet1)", None))
        self._0_source_combo.setItemText(1, QCoreApplication.translate("ParserEditor", u"name (sheet2)", None))

        self._4_allow_empty.setText("")
        self._3_include_field.setText("")
        self._0_allow_empty.setText("")
        self._1_allow_empty.setText("")
        self._0_include_field.setText("")
        self.product_fields_label.setText(QCoreApplication.translate("ParserEditor", u"Product Fields", None))
        ___qtablewidgetitem = self.xlsx_table_0.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ParserEditor", u"id", None));
        ___qtablewidgetitem1 = self.xlsx_table_0.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ParserEditor", u"name", None));
        ___qtablewidgetitem2 = self.xlsx_table_0.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ParserEditor", u"SKU", None));
        ___qtablewidgetitem3 = self.xlsx_table_0.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ParserEditor", u"manu", None));
        ___qtablewidgetitem4 = self.xlsx_table_0.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("ParserEditor", u"category", None));
        ___qtablewidgetitem5 = self.xlsx_table_0.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("ParserEditor", u"desc", None));
        ___qtablewidgetitem6 = self.xlsx_table_0.verticalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("ParserEditor", u"0", None));
        ___qtablewidgetitem7 = self.xlsx_table_0.verticalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("ParserEditor", u"1", None));
        ___qtablewidgetitem8 = self.xlsx_table_0.verticalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("ParserEditor", u"2", None));
        ___qtablewidgetitem9 = self.xlsx_table_0.verticalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("ParserEditor", u"3", None));
        ___qtablewidgetitem10 = self.xlsx_table_0.verticalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("ParserEditor", u"...", None));

        __sortingEnabled1 = self.xlsx_table_0.isSortingEnabled()
        self.xlsx_table_0.setSortingEnabled(False)
        ___qtablewidgetitem11 = self.xlsx_table_0.item(0, 0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("ParserEditor", u"g54ng459", None));
        ___qtablewidgetitem12 = self.xlsx_table_0.item(0, 1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("ParserEditor", u"prod1-abcd", None));
        ___qtablewidgetitem13 = self.xlsx_table_0.item(0, 2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("ParserEditor", u"4235GH435", None));
        ___qtablewidgetitem14 = self.xlsx_table_0.item(0, 3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("ParserEditor", u"manu1", None));
        ___qtablewidgetitem15 = self.xlsx_table_0.item(0, 4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("ParserEditor", u"x", None));
        ___qtablewidgetitem16 = self.xlsx_table_0.item(0, 5)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("ParserEditor", u"x", None));
        ___qtablewidgetitem17 = self.xlsx_table_0.item(1, 0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("ParserEditor", u"43d34gi8g3", None));
        ___qtablewidgetitem18 = self.xlsx_table_0.item(1, 1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("ParserEditor", u"prod2-abcde", None));
        ___qtablewidgetitem19 = self.xlsx_table_0.item(1, 2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("ParserEditor", u"3Y8GH83", None));
        ___qtablewidgetitem20 = self.xlsx_table_0.item(1, 3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("ParserEditor", u"manu1", None));
        ___qtablewidgetitem21 = self.xlsx_table_0.item(1, 4)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("ParserEditor", u"x", None));
        ___qtablewidgetitem22 = self.xlsx_table_0.item(1, 5)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("ParserEditor", u"y", None));
        ___qtablewidgetitem23 = self.xlsx_table_0.item(2, 0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("ParserEditor", u"6tgrb43h9h", None));
        ___qtablewidgetitem24 = self.xlsx_table_0.item(2, 1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("ParserEditor", u"prod3-ab", None));
        ___qtablewidgetitem25 = self.xlsx_table_0.item(2, 2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("ParserEditor", u"8RFTC6U8", None));
        ___qtablewidgetitem26 = self.xlsx_table_0.item(2, 3)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("ParserEditor", u"manu2", None));
        ___qtablewidgetitem27 = self.xlsx_table_0.item(2, 4)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("ParserEditor", u"y", None));
        ___qtablewidgetitem28 = self.xlsx_table_0.item(2, 5)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("ParserEditor", u"z", None));
        self.xlsx_table_0.setSortingEnabled(__sortingEnabled1)

        self.xlsx_tabs.setTabText(self.xlsx_tabs.indexOf(self.xlsx_tab_0), QCoreApplication.translate("ParserEditor", u"Sheet1", None))
        ___qtablewidgetitem29 = self.xlsx_table_1.horizontalHeaderItem(0)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("ParserEditor", u"id", None));
        ___qtablewidgetitem30 = self.xlsx_table_1.horizontalHeaderItem(1)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("ParserEditor", u"SKU", None));
        ___qtablewidgetitem31 = self.xlsx_table_1.horizontalHeaderItem(2)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("ParserEditor", u"manu", None));
        ___qtablewidgetitem32 = self.xlsx_table_1.horizontalHeaderItem(3)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("ParserEditor", u"category", None));
        ___qtablewidgetitem33 = self.xlsx_table_1.horizontalHeaderItem(4)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("ParserEditor", u"desc", None));
        ___qtablewidgetitem34 = self.xlsx_table_1.verticalHeaderItem(0)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("ParserEditor", u"0", None));
        ___qtablewidgetitem35 = self.xlsx_table_1.verticalHeaderItem(1)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("ParserEditor", u"1", None));
        ___qtablewidgetitem36 = self.xlsx_table_1.verticalHeaderItem(2)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("ParserEditor", u"2", None));
        ___qtablewidgetitem37 = self.xlsx_table_1.verticalHeaderItem(3)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("ParserEditor", u"3", None));
        ___qtablewidgetitem38 = self.xlsx_table_1.verticalHeaderItem(4)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("ParserEditor", u"...", None));

        __sortingEnabled2 = self.xlsx_table_1.isSortingEnabled()
        self.xlsx_table_1.setSortingEnabled(False)
        ___qtablewidgetitem39 = self.xlsx_table_1.item(0, 0)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("ParserEditor", u"g54ng459", None));
        ___qtablewidgetitem40 = self.xlsx_table_1.item(0, 1)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("ParserEditor", u"4235GH435", None));
        ___qtablewidgetitem41 = self.xlsx_table_1.item(0, 2)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("ParserEditor", u"manu1", None));
        ___qtablewidgetitem42 = self.xlsx_table_1.item(0, 3)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("ParserEditor", u"x", None));
        ___qtablewidgetitem43 = self.xlsx_table_1.item(0, 4)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("ParserEditor", u"x", None));
        ___qtablewidgetitem44 = self.xlsx_table_1.item(1, 0)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("ParserEditor", u"43d34gi8g3", None));
        ___qtablewidgetitem45 = self.xlsx_table_1.item(1, 1)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("ParserEditor", u"3Y8GH83", None));
        ___qtablewidgetitem46 = self.xlsx_table_1.item(1, 2)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("ParserEditor", u"manu1", None));
        ___qtablewidgetitem47 = self.xlsx_table_1.item(1, 3)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("ParserEditor", u"x", None));
        ___qtablewidgetitem48 = self.xlsx_table_1.item(1, 4)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("ParserEditor", u"y", None));
        ___qtablewidgetitem49 = self.xlsx_table_1.item(2, 0)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("ParserEditor", u"6tgrb43h9h", None));
        ___qtablewidgetitem50 = self.xlsx_table_1.item(2, 1)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("ParserEditor", u"8RFTC6U8", None));
        ___qtablewidgetitem51 = self.xlsx_table_1.item(2, 2)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("ParserEditor", u"manu2", None));
        ___qtablewidgetitem52 = self.xlsx_table_1.item(2, 3)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("ParserEditor", u"y", None));
        ___qtablewidgetitem53 = self.xlsx_table_1.item(2, 4)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("ParserEditor", u"z", None));
        self.xlsx_table_1.setSortingEnabled(__sortingEnabled2)

        self.xlsx_tabs.setTabText(self.xlsx_tabs.indexOf(self.xlsx_tab_1), QCoreApplication.translate("ParserEditor", u"Sheet2", None))
        self.remove_curr_button_0.setText(QCoreApplication.translate("ParserEditor", u"Remove Currency", None))
        self.add_curr_button_0.setText(QCoreApplication.translate("ParserEditor", u"Add Currency", None))
        self.inluce_currency_10.setText("")
        self.header_input_label_0.setText(QCoreApplication.translate("ParserEditor", u"Input Field", None))
        self.curr_field_combo_01.setItemText(0, QCoreApplication.translate("ParserEditor", u"srp (sheet2)", None))
        self.curr_field_combo_01.setItemText(1, QCoreApplication.translate("ParserEditor", u"name (sheet2)", None))

        self.curr_label_01.setText(QCoreApplication.translate("ParserEditor", u"EUR", None))
        self.header_cf_label_0.setText(QCoreApplication.translate("ParserEditor", u"Conversion Factor", None))
        self.curr_label_00.setText(QCoreApplication.translate("ParserEditor", u"PLN", None))
        self.c_factor_ledit_00.setText(QCoreApplication.translate("ParserEditor", u"1.00", None))
        self.header_curr_label_0.setText(QCoreApplication.translate("ParserEditor", u"Currency", None))
        self.c_factor_ledit_01.setText(QCoreApplication.translate("ParserEditor", u"1.00", None))
        self.include_currency_00.setText("")
        self.curr_field_combo_00.setItemText(0, QCoreApplication.translate("ParserEditor", u"srp (sheet1)", None))
        self.curr_field_combo_00.setItemText(1, QCoreApplication.translate("ParserEditor", u"name (sheet2)", None))

        self.currecy_tabs.setTabText(self.currecy_tabs.indexOf(self.currency_tab_0), QCoreApplication.translate("ParserEditor", u"pb-01", None))
        self.include_curr_10.setText("")
        self.curr_label_12.setText(QCoreApplication.translate("ParserEditor", u"USD", None))
        self.curr_label_10.setText(QCoreApplication.translate("ParserEditor", u"PLN", None))
        self.c_factor_ledit_12.setText(QCoreApplication.translate("ParserEditor", u"1.00", None))
        self.include_curr_12.setText("")
        self.c_factor_ledit_10.setText(QCoreApplication.translate("ParserEditor", u"1.00", None))
        self.header_cf_label_1.setText(QCoreApplication.translate("ParserEditor", u"Conversion Factor", None))
        self.include_curr_11.setText("")
        self.header_input_label_1.setText(QCoreApplication.translate("ParserEditor", u"Input Field", None))
        self.c_factor_ledit_11.setText(QCoreApplication.translate("ParserEditor", u"1.00", None))
        self.curr_label_11.setText(QCoreApplication.translate("ParserEditor", u"EUR", None))
        self.curr_field_combo_11.setItemText(0, QCoreApplication.translate("ParserEditor", u"srp (sheet2)", None))
        self.curr_field_combo_11.setItemText(1, QCoreApplication.translate("ParserEditor", u"name (sheet2)", None))

        self.header_curr_label_1.setText(QCoreApplication.translate("ParserEditor", u"Currency", None))
        self.curr_field_combo_10.setItemText(0, QCoreApplication.translate("ParserEditor", u"srp (sheet1)", None))
        self.curr_field_combo_10.setItemText(1, QCoreApplication.translate("ParserEditor", u"name (sheet2)", None))

        self.curr_field_combo_12.setItemText(0, QCoreApplication.translate("ParserEditor", u"srp (sheet2)", None))
        self.curr_field_combo_12.setItemText(1, QCoreApplication.translate("ParserEditor", u"name (sheet2)", None))

        self.remove_curr_button_1.setText(QCoreApplication.translate("ParserEditor", u"Remove Currency", None))
        self.add_curr_button_1.setText(QCoreApplication.translate("ParserEditor", u"Add Currency", None))
        self.currecy_tabs.setTabText(self.currecy_tabs.indexOf(self.currency_tab_1), QCoreApplication.translate("ParserEditor", u"pb-02", None))
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
    