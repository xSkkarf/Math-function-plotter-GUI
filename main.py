from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QAction, QMessageBox, QVBoxLayout
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python plotter")
        self.setGeometry(600, 200, 500, 500)
        self.setMinimumHeight(600)
        self.setMinimumWidth(900)
        self.show()

        self.createMenu()


    def createMenu(self):
        menuBar = self.menuBar()
        fileOption = menuBar.addMenu("File")

        new_action = QAction("New", self)
        open_action = QAction("Open", self)
        save_action = QAction("Save", self)
        exit_action = QAction("Exit", self)
        exit_action.setShortcut('ctrl+w')
        exit_action.triggered.connect(self.exitApp)

        fileOption.addAction(new_action)
        fileOption.addAction(open_action)
        fileOption.addAction(save_action)
        fileOption.addAction(exit_action)

    def exitApp(self):
        reply = self.createQuestionBox("Exit", "Are you sure you want to exit?")
        if reply:
            self.close()
        else:
            print("Exit cancelled.")
    

    def createQuestionBox(self, title, message):
        reply = QMessageBox.question(self, title, message,
                                    QMessageBox.Yes | QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            print("Yes clicked.")
            return True
        else:
            print("No clicked.")
            return False
        



myApp = QApplication(sys.argv)
window = Window()

myApp.exec_()
sys.exit(0)