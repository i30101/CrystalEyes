"""
Andrew Kim

21 July 2025

Version 1.3.0
"""


from databox import DataBox

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Visualizer(DataBox):
    """ Visualizer for displaying data """

    def __init__(self, root):
        super().__init__(root, "Data Visualization")

