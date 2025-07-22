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

    GRAPH_COLOR = "#ff6d6d"

    def __init__(self, root):
        super().__init__(root, "Analysis Results")

        # control buttons
        self.buttons_frame = ttk.Frame(self.box)
        self.buttons_frame.pack(fill="x", pady=Variables.NOPAD_PAD)

        self.area_distribution_button = ttk.Button(self.buttons_frame, text="Area Distribution")
        self.area_distribution_button.pack(side="left", padx=Variables.PAD_NOPAD, pady=Variables.PAD_NOPAD)

        self.average_area_button = ttk.Button(self.buttons_frame, text="Average Area")
        self.average_area_button.pack(side="left", pady=Variables.PAD_NOPAD)

        self.density_button = ttk.Button(self.buttons_frame, text="Density")
        self.density_button.pack(side="left", padx=Variables.PAD_NOPAD, pady=Variables.PAD_NOPAD)

        self.coverage_button = ttk.Button(self.buttons_frame, text="Coverage")
        self.coverage_button.pack(side="left", padx=Variables.PAD_NOPAD, pady=Variables.PAD_NOPAD)

        self.ratio_button = ttk.Button(self.buttons_frame, text="Side Ratio")
        self.ratio_button.pack(side="left", padx=Variables.PAD_NOPAD, pady=Variables.PAD_NOPAD)

        self.contours_button = ttk.Button(self.buttons_frame, text="Contours")
        self.contours_button.pack(side="left", padx=Variables.PAD_NOPAD, pady=Variables.PAD_NOPAD)


        self.graph_frame = ttk.Frame(self.box)
        self.graph_frame.pack(fill="both", expand=True)

        self.figure = Figure(figsize=(5, 4), dpi=80)
        self.figure.subplots_adjust(top=0.9, right=0.97, bottom=0.2)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.graph_frame)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(fill="both", expand=True)


    def line(self, y: list[float], label: str):
        """ Plots line graph """
        self.clear_graph()

        frames = list(range(len(y)))

        self.ax.clear()
        self.ax.set_xlabel("Frame")
        self.ax.set_ylabel(label)

        # plot line
        self.ax.plot(frames, y, color=Results.GRAPH_COLOR, linewidth=2)

        self.ax.set_xlim(0, max(frames) if frames else 1)
        if y:
            self.ax.set_ylim(min(y) * 0.9, max(y) * 1.1)

        self.canvas.draw()

        # TODO add scatter points


    def histogram(self, data: list[float], label: str):
        """ Plots histogram """
        self.clear_graph()

        self.ax.clear()
        self.ax.set_xlabel(label)
        self.ax.set_ylabel("Frequency")

        # plot histogram
        self.ax.hist(data, bins=20, color=Results.GRAPH_COLOR)

        if data:
            self.ax.set_xlim(min(data) * 0.9, max(data) * 1.1)

        self.canvas.draw()


    def clear_graph(self):
        """ Clear the graph """
        self.ax.clear()
        self.canvas.draw()
