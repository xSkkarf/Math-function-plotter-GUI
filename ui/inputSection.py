from PySide2.QtWidgets import  QHBoxLayout, QVBoxLayout, QWidget, QLineEdit, QPushButton, QGroupBox
from plot.plotCanvas import PlotCanvas


class InputSection:
    def createInputSection(self):
        leftSection = QWidget()
        leftSection.setFixedWidth(300) 
        leftLayout = QVBoxLayout(leftSection)

        functionGroupBox = QGroupBox("Function")
        functionGroupBox.setFont(self.font)
        functionLayout = QVBoxLayout()

        self.functionInput = QLineEdit()
        self.functionInput.setPlaceholderText("Enter function to plot")
        self.functionInput.setFont(self.font)
        self.functionInput.setText("x")
        functionLayout.addWidget(self.functionInput)

        functionGroupBox.setLayout(functionLayout)
        leftLayout.addWidget(functionGroupBox)

        xRangeGroupBox = QGroupBox("X Range")
        xRangeGroupBox.setFont(self.font)
        xRangeLayout = QHBoxLayout()

        self.xMin = QLineEdit()
        self.xMin.setPlaceholderText("x min value")
        self.xMin.setFont(self.font)
        self.xMin.setText("0")

        xRangeLayout.addWidget(self.xMin)

        self.xMax = QLineEdit()
        self.xMax.setPlaceholderText("x max value")
        self.xMax.setFont(self.font)
        self.xMax.setText("5")

        xRangeLayout.addWidget(self.xMax)
        xRangeGroupBox.setLayout(xRangeLayout)

        leftLayout.addWidget(xRangeGroupBox)

        stepGroupBox = QGroupBox("Step")
        stepGroupBox.setFont(self.font)
        stepLayout = QVBoxLayout()

        self.step = QLineEdit()
        self.step.setPlaceholderText("step")
        self.step.setFont(self.font)
        self.step.setText("1")
        stepLayout.addWidget(self.step)
        stepGroupBox.setLayout(stepLayout)
        leftLayout.addWidget(stepGroupBox)

        leftLayout.addSpacing(10)

        plotButton = QPushButton("Plot")
        plotButton.setFont(self.font)
        plotButton.clicked.connect(self.plotFunction)
        leftLayout.addWidget(plotButton)

        clearButton = QPushButton("Clear")
        clearButton.setFont(self.font)
        clearButton.clicked.connect(self.clearPlotArea)
        leftLayout.addWidget(clearButton)

        leftLayout.addStretch()

        instructionsButton = QPushButton("Instructions")
        instructionsButton.setFont(self.font)
        instructionsButton.clicked.connect(self.showInstructions)
        leftLayout.addWidget(instructionsButton)

        self.mainLayout.addWidget(leftSection)


    def plotFunction(self):
        plot = PlotCanvas(self.functionInput.text() or 'x', (self.xMin.text() or 0), (self.xMax.text() or 5), (self.step.text() or 1), self)

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

    def clearTextBoxes(self):
        self.functionInput.clear()
        self.xMin.clear()
        self.xMax.clear()
        self.step.clear()

    def clearPlotArea(self):
        self.clearLatestWidget()
        self.plotArea = QWidget()
        self.plotArea.setStyleSheet("background-color: lightgray;")
        self.mainLayout.addWidget(self.plotArea, stretch=5)
        self.latestWidget = self.plotArea
        self.clearTextBoxes()

    def showInstructions(self):
        self.createMessageBox("Instructions", "")