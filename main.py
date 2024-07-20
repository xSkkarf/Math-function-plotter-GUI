from PySide2.QtWidgets import QApplication
import sys
from ui.mainWindow import MainWindow


myApp = QApplication(sys.argv)
window = MainWindow()
sys.exit(myApp.exec_())