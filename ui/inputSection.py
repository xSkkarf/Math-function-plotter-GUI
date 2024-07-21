from PySide2.QtWidgets import  QHBoxLayout, QVBoxLayout, QWidget, QLineEdit, QPushButton, QGroupBox, QLabel, QMessageBox
from plot.plotCanvas import PlotCanvas
from plot.inputValidation import InvalidFunctionError
from PySide2.QtCore import Qt
from ui.instructions import instructions_text

# Global variables to track error type and count for the error console
lastErrorType = 0
errorCount = 0

class InputSection:
    def createInputSection(self):
        # Creating a new input section with QVBoxLayout (vertical layout)
        inputSection = QWidget()
        inputSection.setFixedWidth(300) 
        inputSectionLayout = QVBoxLayout(inputSection)

        # Group box for the function input
        functionGroupBox = QGroupBox("Function")
        functionGroupBox.setFont(self.font)
        functionLayout = QVBoxLayout(functionGroupBox)

        # Text box for function input
        self.functionInput = QLineEdit()
        self.functionInput.setPlaceholderText("Enter function to plot")
        self.functionInput.setFont(self.font)
        functionLayout.addWidget(self.functionInput)

        inputSectionLayout.addWidget(functionGroupBox)

        # Group box for the x values range
        xRangeGroupBox = QGroupBox("X Range")
        xRangeGroupBox.setFont(self.font)
        xRangeLayout = QHBoxLayout(xRangeGroupBox)

        # Minimum value text box
        self.xMin = QLineEdit()
        self.xMin.setPlaceholderText("x min value")
        self.xMin.setFont(self.font)
        xRangeLayout.addWidget(self.xMin)

        # Maximum value text box
        self.xMax = QLineEdit()
        self.xMax.setPlaceholderText("x max value")
        self.xMax.setFont(self.font)
        xRangeLayout.addWidget(self.xMax)

        inputSectionLayout.addWidget(xRangeGroupBox)

        # Group box for the step value
        stepGroupBox = QGroupBox("Step")
        stepGroupBox.setFont(self.font)
        stepLayout = QVBoxLayout(stepGroupBox)

        # Text box for step value
        self.step = QLineEdit()
        self.step.setPlaceholderText("step")
        self.step.setFont(self.font)
        stepLayout.addWidget(self.step)
        inputSectionLayout.addWidget(stepGroupBox)

        inputSectionLayout.addSpacing(10)

        # Creating plot button
        plotButton = QPushButton("Plot")
        plotButton.setFont(self.font)
        plotButton.clicked.connect(self.plotFunction)
        inputSectionLayout.addWidget(plotButton)

        # Creating clear button
        clearButton = QPushButton("Clear")
        clearButton.setFont(self.font)
        clearButton.clicked.connect(self.clearButtonAction)
        inputSectionLayout.addWidget(clearButton)

        inputSectionLayout.addSpacing(10)
        
        # Creating error console group box to display error messages
        errorConsole = QGroupBox("Error Console")
        errorConsole.setFont(self.font)
        errorConsoleLayout = QVBoxLayout(errorConsole)
        self.errorStatement = QLabel()
        self.errorStatement.setStyleSheet("color: red;")
        self.errorStatement.setWordWrap(True)   # Continue on a newline if there's no space left for text
        errorConsoleLayout.addWidget(self.errorStatement)

        inputSectionLayout.addWidget(errorConsole)

        # Adding stretch to make the instruction button at the bottom of the layout
        inputSectionLayout.addStretch()

        # Creating instructions button to show instructions on how to use the application
        instructionsButton = QPushButton("Instructions")
        instructionsButton.setFont(self.font)
        instructionsButton.clicked.connect(self.showInstructions)
        inputSectionLayout.addWidget(instructionsButton)

        # Finally adding the inputSection layout to the main layout
        self.mainLayout.addWidget(inputSection)


    def plotFunction(self):
        """
        This function handles the plotting of a function based on user input.

        Parameters:
        self (object): The instance of the class calling this method.

        Returns:
        None. This function does not return any value.
        """
        global errorCount   # Used here to reset back to zero on successful plot attempts
        try:
            # Clearing old error traces (red text boxes outline and error messages in the console) before a new plot attempt
            self.clearTextBoxesStyle()
            self.clearErrorMessage()

            self.plot = PlotCanvas(self,
                            self.functionInput.text(),
                            self.xMin.text(),
                            self.xMax.text(),
                            self.step.text())
            
            # Replace the latest added widget to the main layout with the new plot if successful
            self.replacePlot(self.latestWidget, self.plot)
            
            # Resetting error count
            errorCount = 0

            # Setting the latest widget to the new plot
            self.latestWidget = self.plot

        except InvalidFunctionError as e:
            # This exception is only for plot function errors (syntax, wrong function names, missing parenthesis, etc..)
            self.showErrorMessage(e, "Invalid plot function, see Instructions for more information")
        except Exception as e:
            # This exception is for any other errors in x range values or step value
            self.showErrorMessage(e, f"{e}")



    def replacePlot(self, oldplot, newPlot):
        """
        This function replaces the old plot widget with a new plot widget in the main layout.
        It also deletes the old widget to free up resources (memory).

        Parameters:
        self (object): The instance of the class calling this method.
        oldplot (QWidget): The widget to be replaced.
        newPlot (QWidget): The new widget to be added.

        Returns:
        None. This function does not return any value.
        """
        self.mainLayout.replaceWidget(oldplot, newPlot)
        self.clearLatestWidget()


    def clearButtonAction(self):
        """
        This function clears all user inputs, the plot area, error console, and resets error tracking variables.
        It is assigned to the clear button.

        Parameters:
        self (object): The instance of the class calling this method.

        Returns:
        None. This function does not return any value.
        """
        global errorCount
        errorCount = 0
        self.clearLatestWidget()

        # Without this function the whole plot area would be deleted from the layout. This function sets it back to blank page
        self.clearPlotArea()

        self.clearTextBoxesStyle()
        self.clearTextBoxes()
        self.clearErrorMessage()

    def clearLatestWidget(self):
        """
        Clears the latest widget from the main layout and frees up resources.

        Parameters:
        self (object): The instance of the class calling this method.
            self.latestWidget (QWidget): The widget to be cleared.

        Returns:
        None. This function does not return any value.
        """
        if self.latestWidget:
            self.latestWidget.setParent(None)
            self.latestWidget.deleteLater()
            self.latestWidget = None

    def clearTextBoxes(self):
        """
        Clears all user inputs from the function, x min, x max, and step text boxes.

        Parameters:
        self (object): The instance of the class calling this method.

        Returns:
        None. This function does not return any value. It clears the text boxes.
        """
        self.functionInput.clear()
        self.xMin.clear()
        self.xMax.clear()
        self.step.clear()

    def clearTextBoxesStyle(self):
        """
        Clears the style of the function, x min, x max, and step text boxes.

        This function resets the style sheet of the text boxes to an empty string, effectively removing any
        previously applied styles. This is typically used to clear any red border or highlighting that might
        indicate an error in the user input.

        Parameters:
        self (object): The instance of the class calling this method.

        Returns:
        None. This function does not return any value. It clears the style of the text boxes.
        """
        self.functionInput.setStyleSheet("")
        self.xMin.setStyleSheet("")
        self.xMax.setStyleSheet("")
        self.step.setStyleSheet("")


    def clearPlotArea(self):
        """
        This function creates a new QWidget, sets its background color to light gray,
        adds it to the main layout with a stretch factor of 5, and updates the latestWidget
        to this new widget. This effectively clears the plot area.

        Parameters:
        self (object): The instance of the class calling this method.

        Returns:
        None. This function does not return any value. It clears the plot area.
        """
        self.plotArea = QWidget()
        self.plotArea.setStyleSheet("background-color: lightgray;")
        self.mainLayout.addWidget(self.plotArea, stretch=5)
        self.latestWidget = self.plotArea


    def showErrorMessage(self, errorType, errorMessage):
        """
        This function handles the display of error messages in the application.
        It increments the error count if the same error type occurs consecutively,
        and resets the count if a new error type is encountered (used in error cosole).

        Parameters:
        self (object): The instance of the class calling this method.
        errorType (any): The type of error that occurred. This can be any object,
                        but it's typically a string or an exception object.
        errorMessage (str): The error message to be displayed.

        Returns:
        None. This function does not return any value. It updates the error console.
        """
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
        """
        Clears the error message displayed in the error console.
        This function resets the text of the error statement label to an empty string, effectively
        clearing any previously displayed error message.

        Parameters:
        self (object): The instance of the class calling this method.
            self.errorStatement (QLabel): The label widget where the error message is displayed.

        Returns:
        None. This function does not return any value. It clears the error message.
        """
        self.errorStatement.setText("")

    def showInstructions(self):
        """
        This function displays a message box with instructions on how to use the application.

        Parameters:
        self (object): The instance of the class calling this method.

        Returns:
        None. This function does not return any value. It opens a message box with instructions.
        """
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Instructions")
        msg_box.setTextFormat(Qt.RichText)
        msg_box.setText(instructions_text)
        msg_box.exec_()

