import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from plot.regexMapper import regexMapper
from plot.inputValidation import validateInput

class PlotCanvas(FigureCanvas):
    def __init__(self, inputSection, plotFunction, xMin, xMax, step):
        
        self.xMin = xMin
        self.xMax = xMax
        self.step = step
        self.plotFunction = plotFunction

        # Check user input before creating the plot
        validateInput(self, inputSection)
    
        # Creating a new figure and axes for the plot
        figure, self.axes = plt.subplots()
        super(PlotCanvas, self).__init__(figure)

        # Creating the x-axis range and the plot function
        x = np.arange(self.xMin, self.xMax+self.step, self.step)    
        f = eval(self.plotFunction)

        # Setting the plot configurations
        self.axes.set(xlabel='x', ylabel='F(x)', title=f'Function: {plotFunction}')
        self.axes.grid()
        
        # Plotting the function on the canvas
        self.axes.plot(x, f)
