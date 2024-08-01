
from plot.regexMapper import regexMapper
import numpy as np


# Custom exception for invalid input in the plot function field
class InvalidFunctionError(ValueError):
    pass

def validateInput(self, inputSection):
    """
    Validates the input for plotting a function.

    Parameters:
    self (object): The instance of the class calling this method.
    inputSection (object): The object containing the input fields.
    plotFunction (str): The mathematical function to be plotted.
    xMin (str): The minimum value of the x-axis.
    xMax (str): The maximum value of the x-axis.
    step (str): The step value for the x-axis.

    Returns:
    None. Raises ValueError if any of the input validations fail.

    Raises:
    ValueError: If any of the following conditions are met:
        - plotFunction is an empty string.
        - xMin is an empty string.
        - xMin is not a valid number.
        - xMax is an empty string.
        - xMax is not a valid number.
        - xMax is not greater than xMin.
        - step is an empty string.
        - step is not a valid number.
        - step is zero or less

        (Optional depending on the requirements, I assumed that it's ok for the step to be greater than the range)
        - step is greater than the x values range
    InvalidFunctionError: If any of the following conditions are met:
        - plotFunction is not a valid mathematical function.
    """

    # Checking empty plot function field
    if self.plotFunction == "":
        inputSection.functionInput.setStyleSheet("border: 1.5px solid red;")
        raise ValueError("Enter a plot function")
    
    # Checking invalid input in plot function field. This is actually a small test with dummy x-axis to validate the input.
    try:
        self.plotFunction = regexMapper(self.plotFunction)
        x = np.arange(0, 5, 1)
        eval(self.plotFunction)
        if 'x' not in self.plotFunction:
            self.isConstant = True

    except Exception as e:
        inputSection.functionInput.setStyleSheet("border: 1.5px solid red;")    # Red outline around plot function text box to indicate invalid input
        raise InvalidFunctionError(f"Invalid plot function {e}")
    
    # Checking empty xMin field
    if self.xMin == "":
        inputSection.xMin.setStyleSheet("border: 1.5px solid red;")
        raise ValueError("Enter a minimum x value")
    
    # Checking if xMin is not a number
    if not is_number(self, 1):
        inputSection.xMin.setStyleSheet("border: 1.5px solid red;")
        raise ValueError("Minimum x value should be a number")
    
    # Checking empty xMax field
    if self.xMax == "":
        inputSection.xMax.setStyleSheet("border: 1.5px solid red;")
        raise ValueError("Enter a maximum x value")
    
    # Checking if xMax is not a number
    if not is_number(self, 2):
        inputSection.xMax.setStyleSheet("border: 1.5px solid red;")
        raise ValueError("Maximum x value should be a number")
    
    # Checking if the x value range is valid (xMin < xMax)
    if self.xMin >= self.xMax:
        inputSection.xMax.setStyleSheet("border: 1.5px solid red;")
        inputSection.xMin.setStyleSheet("border: 1.5px solid red;")
        raise ValueError("Maximum x value should be greater than minimum x value")
    
    # Checking empty step field
    if self.step == "":
        inputSection.step.setStyleSheet("border: 1.5px solid red;")
        raise ValueError("Enter a step value")
    
    # Checking if step is not a number
    if not is_number(self, 3):
        inputSection.step.setStyleSheet("border: 1.5px solid red;")
        raise ValueError("Step value should be a number")
    
    # Checking if step is zero
    if self.step <= 0:
        inputSection.step.setStyleSheet("border: 1.5px solid red;")
        raise ValueError("Step value can't be zero or less")

def is_number(self, id):
    """
    This function checks if the input string can be evaluated as a number. It also catches the ValueError exception from the evaluateExpression function.

    Parameters:
    self (object): The instance of the class calling this method.
    id (int): An identifier to determine which input field to check.
        - 1: Check xMin field.
        - 2: Check xMax field.
        - 3: Check step field.

    Returns:
    bool: True if the input string can be evaluated as a number, False otherwise.

    """

    try:
        if id == 1:
            self.xMin = regexMapper(self.xMin)
            self.xMin = evaluateExpression(self.xMin)
        elif id == 2:
            self.xMax = regexMapper(self.xMax)
            self.xMax = evaluateExpression(self.xMax)
        elif id == 3:
            self.step = regexMapper(self.step)
            self.step = evaluateExpression(self.step)
        return True
    except ValueError:
        return False  

def evaluateExpression(expression):
    """
    Evaluates a mathematical expression.

    This function takes a mathematical expression as a string and evaluates it using Python's built-in eval() function.
    If the evaluation fails due to an exception, it raises a ValueError.

    Parameters:
    expression (str): The mathematical expression to be evaluated.

    Returns:
    float: The result of the evaluated expression.

    Raises:
    ValueError: If the evaluation fails due to an exception.
    """
    try:
        return eval(expression)
    except Exception as e:
        raise ValueError()