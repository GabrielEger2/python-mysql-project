import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow
import sqlite3
import datetime

# Creating the class for the main window
class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.create_table()

    def create_table(self):
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, Name TEXT, Sex TEXT, Birthday TEXT, Salary TEXT, Date TEXT)")
        conn.commit()
        conn.close()
        self.ui.StatusLine.setText("<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; color:#ffffff;\">Status: Connected</span></p></body></html>")

# Creating the main window and showing it
app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())