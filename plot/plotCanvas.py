import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from plot.regexMapper import regexMapper
from plot.inputValidation import validateInput

class PlotCanvas(FigureCanvas):
    def __init__(self, inputSection, plotFunction, xMin, xMax, step):
        
        validateInput(self, inputSection, plotFunction, xMin, xMax, step)
    
        figure, self.axes = plt.subplots()
        super(PlotCanvas, self).__init__(figure)


        xMin = regexMapper(xMin)
        xMax = regexMapper(xMax)
        step = regexMapper(step)


        x = np.arange(eval(xMin), eval(xMax)+eval(step), eval(step))

        mappedPlotFunction = regexMapper(plotFunction)
        f = eval(mappedPlotFunction)

        self.axes.set(xlabel='x', ylabel='F(x)', title=f'Function: {plotFunction}')
        self.axes.grid()
        
        self.axes.plot(x, f)
