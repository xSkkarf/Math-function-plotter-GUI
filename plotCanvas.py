import numpy as np
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class PlotCanvas(FigureCanvas):
    def __init__(self, plotFunction, xMin, xMax, step, parent=None):
        figure, self.axes = plt.subplots(figsize=(6,4), dpi=100)
        super(PlotCanvas, self).__init__(figure)

        x = np.arange(float(xMin), float(xMax), float(step))
        f = eval(plotFunction)

        self.axes.set(xlabel='x', ylabel='F(x)', title='Function plotter :)')
        self.axes.grid()
        
        self.axes.plot(x, f)
