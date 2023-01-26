import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow

# Creating the class for the main window
class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

# Creating the main window and showing it
app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())