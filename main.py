from PySide2.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QAction, QMessageBox, QVBoxLayout, QWidget, QLineEdit, QPushButton, QLabel, QGroupBox
from PySide2.QtGui import QFont
import sys
import plotCanvas


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python plotter")
        self.setGeometry(600, 200, 500, 500)
        self.setMinimumHeight(600)
        self.setMinimumWidth(900)
        self.font = QFont("roboto", 12)

        self.latestWidget = None

        self.createMenuBar()
        self.createMainLayout()

        self.show()

    def createMenuBar(self):
        menuBar = self.menuBar()
        fileOption = menuBar.addMenu("File")

        newAction = QAction("New", self)
        openAction = QAction("Open", self)
        saveAction = QAction("Save", self)
        saveAction.setShortcut('ctrl+s')
        saveAction.triggered.connect(self.saveApp)

        exitAction = QAction("Exit", self)
        exitAction.setShortcut('ctrl+w')
        exitAction.triggered.connect(self.exitApp)

        fileOption.addAction(newAction)
        fileOption.addAction(openAction)
        fileOption.addAction(saveAction)
        fileOption.addAction(exitAction)

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

    def saveApp(self):
        self.createMessageBox("Save", "Saved successfully")


    def createMessageBox(self, title, message):
        reply = QMessageBox.about(self, title, message)
        
        
    def createMainLayout(self):
        MainWidget = QWidget()
        self.setCentralWidget(MainWidget)
        
        self.mainLayout = QHBoxLayout(MainWidget)
        
        self.createLeftSection(self.mainLayout)
        
        self.plotArea = QWidget()
        self.plotArea.setStyleSheet("background-color: lightgray;")
        self.mainLayout.addWidget(self.plotArea, stretch=5)
        self.latestWidget = self.plotArea

        


    def createLeftSection(self, mainLayout):
        leftSection = QWidget()
        leftSection.setFixedWidth(300) 
        leftLayout = QVBoxLayout(leftSection)

        functionGroupBox = QGroupBox("Function")
        functionGroupBox.setFont(self.font)
        functionLayout = QVBoxLayout()
        
        self.functionInput = QLineEdit()
        self.functionInput.setPlaceholderText("Enter function to plot")
        self.functionInput.setFont(self.font)
        functionLayout.addWidget(self.functionInput)
        
        functionGroupBox.setLayout(functionLayout)
        leftLayout.addWidget(functionGroupBox)

        xRangeGroupBox = QGroupBox("X Range")
        xRangeGroupBox.setFont(self.font)
        xRangeLayout = QHBoxLayout()
        
        self.xMin = QLineEdit()
        self.xMin.setPlaceholderText("x min value")
        self.xMin.setFont(self.font)
        xRangeLayout.addWidget(self.xMin)

        self.xMax = QLineEdit()
        self.xMax.setPlaceholderText("x max value")
        self.xMax.setFont(self.font)
        xRangeLayout.addWidget(self.xMax)
        xRangeGroupBox.setLayout(xRangeLayout)
        
        leftLayout.addWidget(xRangeGroupBox)

        stepGroupBox = QGroupBox("Step")
        stepGroupBox.setFont(self.font)
        stepLayout = QVBoxLayout()
        
        self.step = QLineEdit()
        self.step.setPlaceholderText("step")
        self.step.setFont(self.font)
        stepLayout.addWidget(self.step)
        stepGroupBox.setLayout(stepLayout)
        leftLayout.addWidget(stepGroupBox)

        plotButton = QPushButton("Plot")
        plotButton.setFont(self.font)
        plotButton.clicked.connect(self.plotFunction)
        leftLayout.addWidget(plotButton)

        clearButton = QPushButton("Clear")
        clearButton.setFont(self.font)
        clearButton.clicked.connect(self.clearPlotArea)
        leftLayout.addWidget(clearButton)

        leftLayout.addStretch()
        
        mainLayout.addWidget(leftSection)
    
    def plotFunction(self):
        plot = plotCanvas.PlotCanvas(self.functionInput.text() or 'x', (self.xMin.text() or 0), (self.xMax.text() or 5), (self.step.text() or 1), self)

        if self.latestWidget:
            self.mainLayout.replaceWidget(self.latestWidget, plot)
            self.latestWidget.deleteLater()
        else:
            self.mainLayout.addWidget(plot, stretch=5)

        self.latestWidget = plot

    def clearLatestWidget(self):
        if self.latestWidget:
            self.latestWidget.setParent(None)
            self.latestWidget.deleteLater()
            self.latestWidget = None

    def clearPlotArea(self):
        self.clearLatestWidget()
        self.plotArea = QWidget()
        self.plotArea.setStyleSheet("background-color: lightgray;")
        self.mainLayout.addWidget(self.plotArea, stretch=5)
        self.latestWidget = self.plotArea

myApp = QApplication(sys.argv)
window = Window()

sys.exit(myApp.exec_())