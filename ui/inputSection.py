from PySide2.QtWidgets import  QHBoxLayout, QVBoxLayout, QWidget, QLineEdit, QPushButton, QGroupBox, QLabel, QMessageBox
from plot.plotCanvas import PlotCanvas
from plot.inputValidation import InvalidFunctionError
from PySide2.QtCore import Qt
from ui.instructions import instructions_text

lastErrorType = 0
errorCount = 0

class InputSection:
    def createInputSection(self):
        leftSection = QWidget()
        leftSection.setFixedWidth(300) 
        leftLayout = QVBoxLayout(leftSection)

        functionGroupBox = QGroupBox("Function")
        functionGroupBox.setFont(self.font)
        functionLayout = QVBoxLayout(functionGroupBox)

        self.functionInput = QLineEdit()
        self.functionInput.setPlaceholderText("Enter function to plot")
        self.functionInput.setFont(self.font)
        functionLayout.addWidget(self.functionInput)

        leftLayout.addWidget(functionGroupBox)

        xRangeGroupBox = QGroupBox("X Range")
        xRangeGroupBox.setFont(self.font)
        xRangeLayout = QHBoxLayout(xRangeGroupBox)

        self.xMin = QLineEdit()
        self.xMin.setPlaceholderText("x min value")
        self.xMin.setFont(self.font)

        xRangeLayout.addWidget(self.xMin)

        self.xMax = QLineEdit()
        self.xMax.setPlaceholderText("x max value")
        self.xMax.setFont(self.font)

        xRangeLayout.addWidget(self.xMax)

        leftLayout.addWidget(xRangeGroupBox)

        stepGroupBox = QGroupBox("Step")
        stepGroupBox.setFont(self.font)
        stepLayout = QVBoxLayout(stepGroupBox)

        self.step = QLineEdit()
        self.step.setPlaceholderText("step")
        self.step.setFont(self.font)
        stepLayout.addWidget(self.step)
        leftLayout.addWidget(stepGroupBox)

        leftLayout.addSpacing(10)

        plotButton = QPushButton("Plot")
        plotButton.setFont(self.font)
        plotButton.clicked.connect(self.plotFunction)
        leftLayout.addWidget(plotButton)

        clearButton = QPushButton("Clear")
        clearButton.setFont(self.font)
        clearButton.clicked.connect(self.clearButtonAction)
        leftLayout.addWidget(clearButton)

        leftLayout.addSpacing(10)
        
        errorConsole = QGroupBox("Error Console")
        errorConsole.setFont(self.font)
        errorConsoleLayout = QVBoxLayout(errorConsole)
        self.errorStatement = QLabel()
        self.errorStatement.setStyleSheet("color: red;")
        self.errorStatement.setWordWrap(True)
        errorConsoleLayout.addWidget(self.errorStatement)

        leftLayout.addWidget(errorConsole)

        leftLayout.addStretch()

        instructionsButton = QPushButton("Instructions")
        instructionsButton.setFont(self.font)
        instructionsButton.clicked.connect(self.showInstructions)
        leftLayout.addWidget(instructionsButton)

        self.mainLayout.addWidget(leftSection)


    def plotFunction(self):
        global errorCount
        # print(self.functionInput.text()=="")
        try:
            self.clearTextBoxesStyle()
            self.clearErrorMessage()

            self.plot = PlotCanvas(self,
                            self.functionInput.text(),
                            self.xMin.text(),
                            self.xMax.text(),
                            self.step.text())
            if self.latestWidget:
                self.mainLayout.replaceWidget(self.latestWidget, self.plot)
                self.latestWidget.deleteLater()
            else:
                self.mainLayout.addWidget(self.plot, stretch=5)
            
            errorCount = 0
            self.latestWidget = self.plot
        except InvalidFunctionError as e:
            self.showErrorMessage(e, "Invalid plot function, see Instructions for more information")
        except Exception as e:
            self.showErrorMessage(e, f"{e}")




    def clearButtonAction(self):
        global errorCount
        errorCount = 0
        self.clearLatestWidget()
        self.clearPlotArea()
        self.clearTextBoxesStyle()
        self.clearTextBoxes()
        self.clearErrorMessage()

    def clearLatestWidget(self):
        if self.latestWidget:
            self.latestWidget.setParent(None)
            self.latestWidget.deleteLater()
            self.latestWidget = None

    def clearTextBoxes(self):
        self.functionInput.clear()
        self.xMin.clear()
        self.xMax.clear()
        self.step.clear()

    def clearTextBoxesStyle(self):
        self.functionInput.setStyleSheet("")
        self.xMin.setStyleSheet("")
        self.xMax.setStyleSheet("")
        self.step.setStyleSheet("")


    def clearPlotArea(self):
        self.plotArea = QWidget()
        self.plotArea.setStyleSheet("background-color: lightgray;")
        self.mainLayout.addWidget(self.plotArea, stretch=5)
        self.latestWidget = self.plotArea


    def showErrorMessage(self, errorType, errorMessage):
        global lastErrorType
        global errorCount
        

        if str(lastErrorType) == str(errorType):
            errorCount+=1
        elif str(lastErrorType) != str(errorType):
            errorCount = 1
            lastErrorType = errorType    

        self.clearErrorMessage()
        self.errorStatement.setText(f"({errorCount}) {errorMessage}")

    def clearErrorMessage(self):
        self.errorStatement.setText("")

    def showInstructions(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Instructions")
        msg_box.setTextFormat(Qt.RichText)
        msg_box.setText(instructions_text)
        msg_box.exec_()

