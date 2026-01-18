# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sheet-frame.ui'
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

class Ui_SheetFrame(object):
    def setupUi(self, SheetFrame):
        if not SheetFrame.objectName():
            SheetFrame.setObjectName(u"SheetFrame")
        SheetFrame.resize(1458, 760)
        self.gridLayout_5 = QGridLayout(SheetFrame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.sheet_frame = QFrame(SheetFrame)
        self.sheet_frame.setObjectName(u"sheet_frame")
        self.sheet_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.sheet_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.sheet_frame)
        self.gridLayout_7.setSpacing(16)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.pricebooks_groupbox = QGroupBox(self.sheet_frame)
        self.pricebooks_groupbox.setObjectName(u"pricebooks_groupbox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pricebooks_groupbox.sizePolicy().hasHeightForWidth())
        self.pricebooks_groupbox.setSizePolicy(sizePolicy)
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
        self.pricebooks_list.setObjectName(u"pricebooks_list")
        self.pricebooks_list.setSpacing(0)
        self.pricebooks_list.setSortingEnabled(False)

        self.gridLayout_3.addWidget(self.pricebooks_list, 1, 0, 1, 3)

        self.sort_button = QPushButton(self.pricebooks_groupbox)
        self.sort_button.setObjectName(u"sort_button")

        self.gridLayout_3.addWidget(self.sort_button, 0, 2, 1, 1)


        self.gridLayout_7.addWidget(self.pricebooks_groupbox, 0, 0, 1, 1)

        self.product_fields_frame = QGroupBox(self.sheet_frame)
        self.product_fields_frame.setObjectName(u"product_fields_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.product_fields_frame.sizePolicy().hasHeightForWidth())
        self.product_fields_frame.setSizePolicy(sizePolicy1)
        self.product_fields_frame.setMinimumSize(QSize(370, 0))
        self.product_fields_frame.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.product_fields_frame.setFlat(False)
        self.product_fields_frame.setCheckable(False)
        self.gridLayout_4 = QGridLayout(self.product_fields_frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.functions_label = QLabel(self.product_fields_frame)
        self.functions_label.setObjectName(u"functions_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.functions_label.sizePolicy().hasHeightForWidth())
        self.functions_label.setSizePolicy(sizePolicy2)
        self.functions_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.functions_label, 0, 2, 1, 1)

        self.separation_line = QFrame(self.product_fields_frame)
        self.separation_line.setObjectName(u"separation_line")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.separation_line.sizePolicy().hasHeightForWidth())
        self.separation_line.setSizePolicy(sizePolicy3)
        self.separation_line.setFrameShape(QFrame.Shape.HLine)
        self.separation_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.separation_line, 2, 0, 1, 4)

        self.source_label = QLabel(self.product_fields_frame)
        self.source_label.setObjectName(u"source_label")
        sizePolicy2.setHeightForWidth(self.source_label.sizePolicy().hasHeightForWidth())
        self.source_label.setSizePolicy(sizePolicy2)
        self.source_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.source_label, 0, 1, 1, 1)

        self.allow_empty_label = QLabel(self.product_fields_frame)
        self.allow_empty_label.setObjectName(u"allow_empty_label")
        sizePolicy2.setHeightForWidth(self.allow_empty_label.sizePolicy().hasHeightForWidth())
        self.allow_empty_label.setSizePolicy(sizePolicy2)
        self.allow_empty_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.allow_empty_label, 0, 3, 1, 1)

        self.product_fields_scroll_area = QScrollArea(self.product_fields_frame)
        self.product_fields_scroll_area.setObjectName(u"product_fields_scroll_area")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.product_fields_scroll_area.sizePolicy().hasHeightForWidth())
        self.product_fields_scroll_area.setSizePolicy(sizePolicy4)
        self.product_fields_scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.product_fields_scroll_area.setWidgetResizable(True)
        self.product_fields_scroll_area_contents = QWidget()
        self.product_fields_scroll_area_contents.setObjectName(u"product_fields_scroll_area_contents")
        self.product_fields_scroll_area_contents.setGeometry(QRect(0, 0, 375, 655))
        self.gridLayout_2 = QGridLayout(self.product_fields_scroll_area_contents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        # changed
        self.gridLayout_2.addItem(self.verticalSpacer, 200, 0, 1, 2)

        self.product_fields_scroll_area.setWidget(self.product_fields_scroll_area_contents)

        self.gridLayout_4.addWidget(self.product_fields_scroll_area, 3, 0, 1, 4)

        self.product_fields_label = QLabel(self.product_fields_frame)
        self.product_fields_label.setObjectName(u"product_fields_label")
        sizePolicy2.setHeightForWidth(self.product_fields_label.sizePolicy().hasHeightForWidth())
        self.product_fields_label.setSizePolicy(sizePolicy2)
        self.product_fields_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.product_fields_label, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.product_fields_frame, 0, 1, 2, 1)

        self.xlsx_tabs = QTabWidget(self.sheet_frame)
        self.xlsx_tabs.setObjectName(u"xlsx_tabs")
        self.xlsx_tabs.setTabPosition(QTabWidget.TabPosition.North)
        self.xlsx_tabs.setTabShape(QTabWidget.TabShape.Rounded)
        self.xlsx_tabs.setElideMode(Qt.TextElideMode.ElideNone)
        self.xlsx_tabs.setDocumentMode(False)
        self.xlsx_tabs.setTabsClosable(False)
        self.xlsx_tabs.setMovable(False)
        self.xlsx_tabs.setTabBarAutoHide(False)

        self.gridLayout_7.addWidget(self.xlsx_tabs, 0, 2, 2, 1)

        self.currency_tabs = QTabWidget(self.sheet_frame)
        self.currency_tabs.setObjectName(u"currency_tabs")
        self.currency_tabs.setMinimumSize(QSize(371, 0))
        # === added
        self.currency_tabs.setUsesScrollButtons(True)
        self.currency_tabs.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )
        # ===

        self.gridLayout_7.addWidget(self.currency_tabs, 1, 0, 1, 1)

        self.gridLayout_7.setRowStretch(0, 3)
        self.gridLayout_7.setRowStretch(1, 2)
        self.gridLayout_7.setColumnStretch(0, 2)
        self.gridLayout_7.setColumnStretch(1, 2)
        self.gridLayout_7.setColumnStretch(2, 3)

        self.gridLayout_5.addWidget(self.sheet_frame, 0, 0, 1, 1)


        self.retranslateUi(SheetFrame)

        self.pricebooks_list.setCurrentRow(-1)
        self.xlsx_tabs.setCurrentIndex(0)
        self.currency_tabs.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(SheetFrame)
    # setupUi

    def retranslateUi(self, SheetFrame):
        SheetFrame.setWindowTitle(QCoreApplication.translate("SheetFrame", u"Form", None))
        self.pricebooks_groupbox.setTitle(QCoreApplication.translate("SheetFrame", u"Pricebooks", None))
        self.pb_searchbar_line_edit.setInputMask("")
        self.pb_searchbar_line_edit.setText("")
        self.pb_searchbar_line_edit.setPlaceholderText(QCoreApplication.translate("SheetFrame", u"Search for pricebooks...", None))
        self.sort_button.setText(QCoreApplication.translate("SheetFrame", u"Sort", None))
        self.product_fields_frame.setTitle(QCoreApplication.translate("SheetFrame", u"Product2 Fields", None))
        self.functions_label.setText(QCoreApplication.translate("SheetFrame", u"Functions", None))
        self.source_label.setText(QCoreApplication.translate("SheetFrame", u"Source", None))
        self.allow_empty_label.setText(QCoreApplication.translate("SheetFrame", u"Allow Empty", None))
        self.product_fields_label.setText(QCoreApplication.translate("SheetFrame", u"Product Fields", None))
        # self.xlsx_tabs.setTabText(self.xlsx_tabs.indexOf(self.output_tab), QCoreApplication.translate("SheetFrame", u"OUTPUT", None))
    # retranslateUi


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    widget = QWidget()
    ui = Ui_SheetFrame()
    ui.setupUi(widget)
    widget.show()

    sys.exit(app.exec())