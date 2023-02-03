import sys

# Importing classes from PySide6 modules
from PySide6.QtCore import QDate
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow

# Importing user interface file
from ui_main import Ui_MainWindow

# Importing SQLite3 module for database operations
import sqlite3

import datetime

# Creating the class for the main window
class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.create_table()

        # Connecting "Add" button to the add_user method
        self.ui.AddButton.clicked.connect(self.add_user)

        # Loading data from the database to the table widget
        self.load_data()

        # Connecting table item selection to the load_user method
        self.ui.SQL_Table.clicked.connect(self.load_user)

        # Connecting "Disconnect" button to the delete_user method
        self.ui.DisconnectButton.clicked.connect(self.delete_user)

        # Connecting "Update" button to the update_user method
        self.ui.UpdateButton.clicked.connect(self.update_user)

        # Connecting text change in the search entry to the search_in_table method
        self.ui.SearchEntry.textChanged.connect(self.search_in_table)

    # Method to create the table in the database
    def create_table(self):
        try:
            # Connecting to the database
            conn = sqlite3.connect("database.db")
            c = conn.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS users (Name TEXT, Sex TEXT, Birthday TEXT, Salary TEXT, Date TEXT)")
            conn.commit()
            conn.close()

            # Setting the status line text to "Connected"
            self.ui.StatusLine.setText("<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; color:#ffffff;\">Status: Connected</span></p></body></html>")
        except:
            # Setting the status line text to "Disconnected" if an exception occurs
            self.ui.StatusLine.setText("<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; color:#ffffff;\">Status: Disconnected</span></p></body></html>")

    # Method to load data from the database to the table widget
    def load_data(self):
        # Clear any existing items in the table widget
        self.ui.SQL_Table.clearContents()

        conn = sqlite3.connect("database.db")
        cursor = conn.execute("SELECT COUNT(*) FROM users")
        number_of_rows = cursor.fetchone()[0]
        c = conn.cursor()
        sqlquery = f"SELECT * FROM users LIMIT {number_of_rows}"
        self.ui.SQL_Table.setRowCount(number_of_rows)
        tablerow = 0
        for row in c.execute(sqlquery):
            self.ui.SQL_Table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.SQL_Table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.SQL_Table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.SQL_Table.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.ui.SQL_Table.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            tablerow+=1
    
    # Method to erase the user information to the Qt entries
    def erase_entries(self):
        self.ui.NameEntry.setText("")
        self.ui.SexOption.setCurrentIndex(0)
        self.ui.BirthDayEntry.setDate(QDate(2000, 1, 1))
        self.ui.SalaryEntry.setText("")

    # Method to add a user to the database and table widget
    def add_user(self):
        name = str(self.ui.NameEntry.text()).capitalize()
        sex = str(self.ui.SexOption.currentText())
        birthday = self.ui.BirthDayEntry.date().toString("yyyy-MM-dd")
        salary = str(self.ui.SalaryEntry.text())
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("INSERT INTO users (Name, Sex, Birthday, Salary, Date) VALUES (?, ?, ?, ?, ?)", (name, sex, birthday, salary, date))
        conn.commit()
        conn.close()
        print("User Added")
        self.erase_entries()
        self.load_data()

    # Method to load the user information to the Qt entries
    def load_user(self, index):
        self.row = index.row()
        try:
            name = self.ui.SQL_Table.item(self.row, 0).text()
            sex = self.ui.SQL_Table.item(self.row, 1).text()
            birthday = self.ui.SQL_Table.item(self.row, 2).text()
            birthday_datetime = datetime.datetime.strptime(birthday, "%Y-%m-%d")
            birthday = QDate(birthday_datetime.year, birthday_datetime.month, birthday_datetime.day)
            salary = self.ui.SQL_Table.item(self.row, 3).text()
            date = self.ui.SQL_Table.item(self.row, 4).text()
            self.ui.NameEntry.setText(name)
            self.ui.SexOption.setCurrentText(sex)
            self.ui.BirthDayEntry.setDate(birthday)
            self.ui.SalaryEntry.setText(salary)
        except:
            self.erase_entries()

    # Method to delete a user from the database and table widget
    def delete_user(self, index):
        row = self.row
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM users WHERE ROWID = (SELECT ROWID FROM users LIMIT 1 OFFSET {row})")

        # clear existing items in the table widget
        self.ui.SQL_Table.clearContents()
        
        # reload data
        self.load_data()
        conn.commit()
        conn.close()
        
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM users WHERE ROWID = (SELECT ROWID FROM users LIMIT 1 OFFSET {row})")

        # clear existing items in the table widget
        self.ui.SQL_Table.clearContents()
        
        # reload data
        self.load_data()
        conn.commit()
        conn.close()

        self.erase_entries()

    # Method to update a user to the database and table widget
    def update_user(self, index):
        row = self.row
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        name = str(self.ui.NameEntry.text()).capitalize()
        sex = str(self.ui.SexOption.currentText())
        birthday = self.ui.BirthDayEntry.date().toString("yyyy-MM-dd")
        salary = str(self.ui.SalaryEntry.text())
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        conn.execute("UPDATE users SET Name=?, Sex=?, Birthday=?, Salary=?, Date=? WHERE ROWID = (SELECT ROWID FROM users LIMIT 1 OFFSET ?)", (name, sex, birthday, salary, date, row))
        conn.commit()
        conn.close()
        self.load_data()
        self.erase_entries()
        self.load_data()

    # Method to search a user to the database and table widget
    def search_in_table(self, text):
        for row in range(self.ui.SQL_Table.rowCount()):
            for col in range(self.ui.SQL_Table.columnCount()):
                item = self.ui.SQL_Table.item(row, col)
                if item and text in item.text():
                    self.ui.SQL_Table.scrollToItem(item)
                    break



# Creating the main window and showing it
app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())