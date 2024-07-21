from PySide2.QtWidgets import QMainWindow, QHBoxLayout, QWidget
from PySide2.QtGui import QFont
from ui.inputSection import InputSection
from ui.menuBar import MenuBar

class MainWindow(QMainWindow, InputSection, MenuBar):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python plotter")
        self.setGeometry(400, 100, 500, 500)
        self.setMinimumHeight(800)
        self.setMinimumWidth(1000)
        self.font = QFont("roboto", 12)

        self.latestWidget = None

        self.createMenuBar()
        self.createMainLayout()

        self.show()

    
    def createMainLayout(self):
        MainWidget = QWidget()
        self.setCentralWidget(MainWidget)
        
        self.mainLayout = QHBoxLayout(MainWidget)
        
        self.createInputSection()
        
        self.plotArea = QWidget()
        self.plotArea.setStyleSheet("background-color: lightgray;")
        self.mainLayout.addWidget(self.plotArea, stretch=5)
        self.latestWidget = self.plotArea


    
