"""
Andrew Kim

21 July 2025

Version 1.3.0
"""


from databox import DataBox

from variables import Variables

import tkinter as tk
from tkinter import ttk

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Results(DataBox):
    """ Visualizer for displaying data """

    GRAPH_COLOR = "red"

    def __init__(self, root):
        super().__init__(root, "Analysis Results")

        # control buttons
        self.buttons_frame = ttk.Frame(self.box)
        self.buttons_frame.pack(fill="x")

        self.average_area_button = ttk.Button(self.buttons_frame, text="Average Area")
        self.average_area_button.pack(side="left", pady=Variables.PAD_NOPAD)
        self.area_distribution_button = ttk.Button(self.buttons_frame, text="Area Distribution")
        self.area_distribution_button.pack(side="left", padx=Variables.PAD_NOPAD, pady=Variables.PAD_NOPAD)
        self.density_button = ttk.Button(self.buttons_frame, text="Density")
        self.density_button.pack(side="left", padx=Variables.PAD_NOPAD, pady=Variables.PAD_NOPAD)
        self.coverage_button = ttk.Button(self.buttons_frame, text="Coverage")
        self.coverage_button.pack(side="left", padx=Variables.PAD_NOPAD, pady=Variables.PAD_NOPAD)
        self.ratio_button = ttk.Button(self.buttons_frame, text="Side Ratio")
        self.ratio_button.pack(side="left", padx=Variables.PAD_NOPAD, pady=Variables.PAD_NOPAD)
        self.contours_button = ttk.Button(self.buttons_frame, text="Contours")
        self.contours_button.pack(side="left", padx=Variables.PAD_NOPAD, pady=Variables.PAD_NOPAD)
