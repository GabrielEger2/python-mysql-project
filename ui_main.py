from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1102, 825)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setSizeIncrement(QSize(0, 0))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: #181818;\n"
"\n"
"QLineEdit{\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    color: #d8d8d8;\n"
"    font-size: 14pt;\n"
"    background-color: #404040;\n"
"    padding: 5px;\n"
"}")
        self.horizontalLayout_8 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(16, 20, 16, 20)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(15, 20, 15, 20)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.NameEntry = QLineEdit(self.centralwidget)
        self.NameEntry.setObjectName(u"NameEntry")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.NameEntry.sizePolicy().hasHeightForWidth())
        self.NameEntry.setSizePolicy(sizePolicy1)
        self.NameEntry.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.NameEntry)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_8.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_7.addWidget(self.label_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.SexOption = QComboBox(self.centralwidget)
        self.SexOption.addItem("")
        self.SexOption.addItem("")
        self.SexOption.addItem("")
        self.SexOption.addItem("")
        self.SexOption.setObjectName(u"SexOption")
        self.SexOption.setStyleSheet(u"\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 5px;\n"
"    background-color: #2a2a2a;\n"
"    border-radius: 5px;\n"
"")

        self.horizontalLayout_7.addWidget(self.SexOption)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_6.addWidget(self.label_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.PhoneEntry = QLineEdit(self.centralwidget)
        self.PhoneEntry.setObjectName(u"PhoneEntry")
        sizePolicy1.setHeightForWidth(self.PhoneEntry.sizePolicy().hasHeightForWidth())
        self.PhoneEntry.setSizePolicy(sizePolicy1)
        self.PhoneEntry.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.PhoneEntry)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)


        self.verticalLayout_8.addLayout(self.verticalLayout_6)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_5.addWidget(self.label_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.BirthDayEntry = QDateEdit(self.centralwidget)
        self.BirthDayEntry.setObjectName(u"BirthDayEntry")
        self.BirthDayEntry.setStyleSheet(u"\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 5px;\n"
"    background-color: #2a2a2a;\n"
"    border-radius: 5px;\n"
"")

        self.horizontalLayout_5.addWidget(self.BirthDayEntry)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)


        self.verticalLayout_8.addLayout(self.verticalLayout_5)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer_4)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.SalaryEntry = QLineEdit(self.centralwidget)
        self.SalaryEntry.setObjectName(u"SalaryEntry")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.SalaryEntry.sizePolicy().hasHeightForWidth())
        self.SalaryEntry.setSizePolicy(sizePolicy2)
        self.SalaryEntry.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.SalaryEntry)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.verticalLayout_8.addLayout(self.verticalLayout_4)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer_5)

        self.AddButton = QPushButton(self.centralwidget)
        self.AddButton.setObjectName(u"AddButton")
        self.AddButton.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(12)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.AddButton.sizePolicy().hasHeightForWidth())
        self.AddButton.setSizePolicy(sizePolicy3)
        self.AddButton.setSizeIncrement(QSize(0, 3))
        self.AddButton.setStyleSheet(u"QPushButton{\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 5px;\n"
"    background-color: #2a2a2a;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"    background-color: #2d5bd4;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color: #2d5bd4;\n"
"}")

        self.verticalLayout_8.addWidget(self.AddButton, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_8 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_8)


        self.horizontalLayout_8.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.SearchEntry = QLineEdit(self.centralwidget)
        self.SearchEntry.setObjectName(u"SearchEntry")
        sizePolicy1.setHeightForWidth(self.SearchEntry.sizePolicy().hasHeightForWidth())
        self.SearchEntry.setSizePolicy(sizePolicy1)
        self.SearchEntry.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.SearchEntry)

        self.horizontalSpacer = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.Search = QPushButton(self.centralwidget)
        self.Search.setObjectName(u"Search")
        self.Search.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.Search.sizePolicy().hasHeightForWidth())
        self.Search.setSizePolicy(sizePolicy3)
        self.Search.setSizeIncrement(QSize(0, 3))
        self.Search.setStyleSheet(u"QPushButton{\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 5px;\n"
"    background-color: #2a2a2a;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"    background-color: #2d5bd4;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color: #2d5bd4;\n"
"}")

        self.horizontalLayout.addWidget(self.Search)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_7 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_7)

        self.SQL_Table = QTableWidget(self.centralwidget)
        if (self.SQL_Table.columnCount() < 5):
            self.SQL_Table.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.SQL_Table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.SQL_Table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.SQL_Table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.SQL_Table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.SQL_Table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.SQL_Table.setObjectName(u"SQL_Table")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.SQL_Table.sizePolicy().hasHeightForWidth())
        self.SQL_Table.setSizePolicy(sizePolicy4)
        self.SQL_Table.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")

        self.verticalLayout.addWidget(self.SQL_Table)

        self.verticalSpacer_6 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_6)


        self.verticalLayout_9.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.ConnectButton = QPushButton(self.centralwidget)
        self.ConnectButton.setObjectName(u"ConnectButton")
        self.ConnectButton.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.ConnectButton.sizePolicy().hasHeightForWidth())
        self.ConnectButton.setSizePolicy(sizePolicy3)
        self.ConnectButton.setSizeIncrement(QSize(0, 3))
        self.ConnectButton.setStyleSheet(u"QPushButton{\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 5px;\n"
"    background-color: #2a2a2a;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"    background-color: #2d5bd4;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color: #2d5bd4;\n"
"}")

        self.horizontalLayout_3.addWidget(self.ConnectButton)

        self.DisconnectButton = QPushButton(self.centralwidget)
        self.DisconnectButton.setObjectName(u"DisconnectButton")
        self.DisconnectButton.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.DisconnectButton.sizePolicy().hasHeightForWidth())
        self.DisconnectButton.setSizePolicy(sizePolicy3)
        self.DisconnectButton.setSizeIncrement(QSize(0, 3))
        self.DisconnectButton.setStyleSheet(u"QPushButton{\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 5px;\n"
"    background-color: #2a2a2a;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"    background-color: #2d5bd4;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color: #2d5bd4;\n"
"}")

        self.horizontalLayout_3.addWidget(self.DisconnectButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_10 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_10)

        self.StatusLine = QLabel(self.centralwidget)
        self.StatusLine.setObjectName(u"StatusLine")
        self.StatusLine.setMinimumSize(QSize(0, 26))
        self.StatusLine.setMaximumSize(QSize(16777215, 26))

        self.verticalLayout_3.addWidget(self.StatusLine)

        self.verticalSpacer_9 = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_9)


        self.verticalLayout_9.addLayout(self.verticalLayout_3)


        self.horizontalLayout_8.addLayout(self.verticalLayout_9)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; color:#ffffff;\">Name:</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; color:#ffffff;\">Sex:</span></p></body></html>", None))
        self.SexOption.setItemText(0, QCoreApplication.translate("MainWindow", u"Select an Option:", None))
        self.SexOption.setItemText(1, QCoreApplication.translate("MainWindow", u"Male", None))
        self.SexOption.setItemText(2, QCoreApplication.translate("MainWindow", u"Female", None))
        self.SexOption.setItemText(3, QCoreApplication.translate("MainWindow", u"Other", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; color:#ffffff;\">Phone Number:</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; color:#ffffff;\">Birthday:</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; color:#ffffff;\">Salary:</span></p></body></html>", None))
        self.AddButton.setText(QCoreApplication.translate("MainWindow", u"  Add  ", None))
        self.SearchEntry.setText("")
        self.Search.setText(QCoreApplication.translate("MainWindow", u"Search Name", None))
        ___qtablewidgetitem = self.SQL_Table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.SQL_Table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Sex", None));
        ___qtablewidgetitem2 = self.SQL_Table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Birthday", None));
        ___qtablewidgetitem3 = self.SQL_Table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Salary", None));
        ___qtablewidgetitem4 = self.SQL_Table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        self.ConnectButton.setText(QCoreApplication.translate("MainWindow", u"         Edit        ", None))
        self.DisconnectButton.setText(QCoreApplication.translate("MainWindow", u"       Remove       ", None))
        self.StatusLine.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; color:#ffffff;\">Status:</span></p></body></html>", None))
    # retranslateUi

