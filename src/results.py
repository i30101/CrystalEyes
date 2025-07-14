"""
Andrew Kim

21 July 2025

Version 1.3.0
"""


from databox import DataBox

import tkinter as tk
from tkinter import ttk

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Results(DataBox):
    """ Visualizer for displaying data """

    def __init__(self, root):
        super().__init__(root, "Analysis Results")

        # control buttons
        self.buttons_frame = ttk.Frame(self.box)
