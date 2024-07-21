
from plot.regexMapper import regexMapper
import numpy as np

globalXMin = 0
globalXMax = 0

class InvalidFunctionError(ValueError):
    pass

def validateInput(self, inputSection, plotFunction, xMin, xMax, step):
    if plotFunction == "":
        inputSection.functionInput.setStyleSheet("border: 1.5px solid red;")
        raise ValueError("Enter a plot function")
    
    try:
        mappedPlotFunction = regexMapper(plotFunction)
        x = np.arange(0, 5, 1)
        eval(mappedPlotFunction)
    except Exception as e:
        # print(f"Error validating input: {e}")
        inputSection.functionInput.setStyleSheet("border: 1.5px solid red;")
        raise InvalidFunctionError(f"Invalid plot function {e}")

    if xMin == "":
        inputSection.xMin.setStyleSheet("border: 1.5px solid red;")
        raise ValueError("Enter a minimum x value")
    if not is_number(xMin, 1):
        inputSection.xMin.setStyleSheet("border: 1.5px solid red;")
        raise ValueError("Minimum x value should be a number")
    
    if xMax == "":
        inputSection.xMax.setStyleSheet("border: 1.5px solid red;")
        raise ValueError("Enter a maximum x value")
    if not is_number(xMax, 2):
        inputSection.xMax.setStyleSheet("border: 1.5px solid red;")
        raise ValueError("Maximum x value should be a number")
    
    if globalXMin >= globalXMax:
        inputSection.xMax.setStyleSheet("border: 1.5px solid red;")
        inputSection.xMin.setStyleSheet("border: 1.5px solid red;")
        raise ValueError("Maximum x value should be greater than minimum x value")
    
    if step == "":
        inputSection.step.setStyleSheet("border: 1.5px solid red;")
        raise ValueError("Enter a step value")
    if not is_number(step, 3):
        inputSection.step.setStyleSheet("border: 1.5px solid red;")
        raise ValueError("Step value should be a number")
    

def is_number(value, id):
    global globalXMin
    global globalXMax
    try:
        value = regexMapper(value)
        if id == 1:
            globalXMin = evaluateExpression(value)
        elif id == 2:
            globalXMax = evaluateExpression(value)
        elif id == 3:
            evaluateExpression(value)
        return True
    except ValueError:
        return False  

def evaluateExpression(expression):
    try:
        return eval(expression)
    except Exception as e:
        raise ValueError()