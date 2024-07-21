from PySide2.QtWidgets import QMainWindow, QHBoxLayout, QWidget
from PySide2.QtGui import QFont
from ui.inputSection import InputSection
from ui.menuBar import MenuBar

# Define the MainWindow class that inherits from QMainWindow class and (InputSection, and MenuBar mixins)
class MainWindow(QMainWindow, InputSection, MenuBar):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python plotter")
        self.setGeometry(400, 100, 500, 500)
        self.setMinimumHeight(800)
        self.setMinimumWidth(1000)
        self.font = QFont("roboto", 12)

        # This variable is used to store the last widget added to the main layout (helpful for clear button function)
        self.latestWidget = None        

        self.createMenuBar()
        self.createMainLayout()

        self.show()

    
    def createMainLayout(self):
        # Main widget is the central widget of the main window
        MainWidget = QWidget()
        self.setCentralWidget(MainWidget)
        
        # Settin main layout to the main widget
        self.mainLayout = QHBoxLayout(MainWidget)
        
        # The input section is the left vertical part of  the GUI that takes the input from the user
        self.createInputSection()
        
        # The plot area is the right part of the GUI that displays the plot. Initially, it is left blank
        self.plotArea = QWidget()
        self.plotArea.setStyleSheet("background-color: lightgray;")
        self.mainLayout.addWidget(self.plotArea)

        # Tracking the latest added widget to the main layout
        self.latestWidget = self.plotArea


    
