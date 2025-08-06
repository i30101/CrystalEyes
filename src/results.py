"""
Andrew Kim

21 July 2025

Version 2.0.0
"""


from databox import DataBox

from variables import Variables

import tkinter as tk
from tkinter import ttk

import numpy as np

from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



class Results(DataBox):
    """ Visualizer for displaying data """

    GRAPH_COLOR = "#2a9d8f"

    BIN_EDGES = np.linspace(0, 500, 31)
    LOG_EDGES = np.linspace(0, 7.5, 31)
    VMAX = 0.25
    NUM_FRAMES = 30

    def __init__(self, root):
        super().__init__(root, "Analysis Results")

        self.bins = 10

        # control buttons
        self.buttons_frame = ttk.Frame(self.box)
        self.buttons_frame.pack(fill="x", pady=Variables.NOPAD_PAD)

        self.area_distribution_button = ttk.Button(self.buttons_frame, text="Area")
        self.area_distribution_button.pack(side="left", padx=Variables.PAD_NOPAD, pady=Variables.PAD_NOPAD)

        self.average_area_button = ttk.Button(self.buttons_frame, text="Mean Area")
        self.average_area_button.pack(side="left", padx=Variables.PAD_NOPAD, pady=Variables.PAD_NOPAD)

        self.density_button = ttk.Button(self.buttons_frame, text="Density")
        self.density_button.pack(side="left", padx=Variables.PAD_NOPAD, pady=Variables.PAD_NOPAD)

        self.coverage_button = ttk.Button(self.buttons_frame, text="Coverage")
        self.coverage_button.pack(side="left", padx=Variables.PAD_NOPAD, pady=Variables.PAD_NOPAD)

        self.ratio_button = ttk.Button(self.buttons_frame, text="Side Ratio")
        self.ratio_button.pack(side="left", padx=Variables.PAD_NOPAD, pady=Variables.PAD_NOPAD)

        self.contours_button = ttk.Button(self.buttons_frame, text="Contours")
        self.contours_button.pack(side="left", padx=Variables.PAD_NOPAD, pady=Variables.PAD_NOPAD)

        self.heatmap_button = ttk.Button(self.buttons_frame, text="Heatmap")
        self.heatmap_button.pack(side="left", padx=Variables.PAD_NOPAD, pady=Variables.PAD_NOPAD)

        self.log_button = ttk.Button(self.buttons_frame, text="Log Heatmap")
        self.log_button.pack(side="left", padx=Variables.PAD_NOPAD, pady=Variables.PAD_NOPAD)


        self.graph_frame = ttk.Frame(self.box)
        self.graph_frame.pack(fill="both", expand=True)

        self.figure = Figure(figsize=(5, 4), dpi=80)
        self.figure.subplots_adjust(top=0.9, right=0.97, bottom=0.2)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.graph_frame)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(fill="both", expand=True)

        self.colorbar = None


    def line(self, y: list[float], label: str):
        """ Plots line graph """
        self.clear_graph()

        frames = list(range(len(y)))

        self.ax.clear()
        self.ax.set_xlabel("Frame")
        self.ax.set_ylabel(label)

        # plot line
        self.ax.plot(frames, y, color=Results.GRAPH_COLOR, linewidth=2)
        self.ax.scatter(frames, y, color=Results.GRAPH_COLOR, s=30, picker=5)

        self.ax.set_xlim(0, max(frames) if frames else 1)
        if y:
            self.ax.set_ylim(min(y) * 0.9, max(y) * 1.1)

        self.canvas.draw()


    def histogram(self, data: list[float], label: str):
        """ Plots histogram """
        self.clear_graph()

        self.ax.clear()
        self.ax.set_xlabel(label)
        self.ax.set_ylabel("Frequency")

        # plot histogram
        self.ax.hist(data, bins=self.bins, color=Results.GRAPH_COLOR)

        if data:
            self.ax.set_xlim(min(data), max(data))

        self.canvas.draw()


    def heatmap(self,
                data: list[list[float]],
                title: str = "Area Distribution Over Time",
                ylabel: str = "Area Distribution",
                bin_edges = BIN_EDGES):
        """ Plots heatmap of area distributions """
        self.clear_graph()

        heatmap_data = []
        means = []
        medians = []

        to_index = min(Results.NUM_FRAMES, len(data))

        for frame in data[: to_index]:
            hist, _ = np.histogram(frame, bins=bin_edges)
            total = hist.sum()
            proportions = hist / total if total > 0 else np.zeros_like(hist)
            heatmap_data.append(proportions)

            # store stats
            means.append(np.mean(frame))
            medians.append(np.median(frame))

        # convert to heatmap matrix
        heatmap_matrix = np.array(heatmap_data).T

        # plot heatmap
        cmap = plt.cm.viridis
        im = self.ax.imshow(
            heatmap_matrix,
            aspect='auto',
            origin='lower',
            extent=(0, to_index, float(bin_edges[0]), float(bin_edges[-1])),
            cmap=cmap,
            vmin=0,
            vmax=Results.VMAX
        )

        # plot mean and median dots
        x_vals = np.arange(to_index) + 0.5
        self.ax.plot(x_vals, means, 'ro', label='Mean')
        self.ax.plot(x_vals, medians, 'bo', label='Median')

        self.ax.set_xlabel("Time Frame")
        self.ax.set_ylabel(ylabel)
        self.ax.set_title(title)

        # add colorbar
        if self.colorbar is not None:
            self.colorbar = self.figure.colorbar(im, ax=self.ax, label="Proportion of Ice Crystals")

        self.canvas.draw()


    def log_heatmap(self, data:list[list[float]]):
        """ Plots log heatmap of area distributions """
        self.clear_graph()

        log_data = [np.log(frame) for frame in data]

        self.heatmap(log_data, title="Log(Area) Distribution Over Time", ylabel="Log(Area) Bin", bin_edges=Results.LOG_EDGES)


    def clear_graph(self):
        """ Clear the graph """
        self.ax.clear()

        if self.colorbar is not None:
            self.colorbar.remove()
            self.colorbar = None

        self.canvas.draw()


