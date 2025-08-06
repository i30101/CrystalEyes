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

    GRAPH_COLOR = "#2a9d8f"

    def __init__(self, root):
        super().__init__(root, "Analysis Results")

        self.bins = 10

        # control buttons
        self.buttons_frame = ttk.Frame(self.box)
        self.buttons_frame.pack(fill="x", pady=Variables.NOPAD_PAD)

        self.area_distribution_button = ttk.Button(self.buttons_frame, text="Area Distribution")
        self.area_distribution_button.pack(side="left", padx=Variables.PAD_NOPAD, pady=Variables.PAD_NOPAD)

        self.average_area_button = ttk.Button(self.buttons_frame, text="Average Area")
        self.average_area_button.pack(side="left", padx=Variables.PAD_NOPAD, pady=Variables.PAD_NOPAD)

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


    def clear_graph(self):
        """ Clear the graph """
        self.ax.clear()
        self.canvas.draw()


"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# === CONFIGURATION ===
BIN_EDGES = np.linspace(0, 7.5, 31)  # 30 bins between 0 and 7.5
VMAX = 0.25  # 30% max for heatmap scale
NUM_FRAMES = 30  # Number of time frames to consider

# === LOAD DATA ===

# === HEATMAP FUNCTION ===
def heatmap(filepath: str):
    df = pd.read_excel(filepath)

    heatmap_data = []
    means = []
    medians = []

    for col in df.columns[:NUM_FRAMES]:
        data = np.log(df[col].dropna())

        # Compute histogram
        hist, _ = np.histogram(data, bins=BIN_EDGES)
        total = hist.sum()
        proportions = hist / total if total > 0 else np.zeros_like(hist)
        heatmap_data.append(proportions)

        # Store stats
        means.append(data.mean())
        medians.append(np.median(data))

    # Convert to heatmap matrix
    heatmap_matrix = np.array(heatmap_data).T

    # === PLOT HEATMAP ===
    plt.figure(figsize=(12, 6))
    cmap = plt.cm.viridis

    im = plt.imshow(heatmap_matrix, aspect='auto', origin='lower',
                    extent=[0, NUM_FRAMES, BIN_EDGES[0], BIN_EDGES[-1]],
                    cmap=cmap, vmin=0, vmax=VMAX)

    # Plot mean and median dots
    x_vals = np.arange(NUM_FRAMES) + 0.5  # Center dots within each frame
    plt.plot(x_vals, means, 'ro', label='Mean')
    plt.plot(x_vals, medians, 'bo', label='Median')
    plt.colorbar(im, label='Proportion of Ice Crystals')
    plt.xlabel("Time Frame")
    plt.ylabel("Log(Area) Bin")
    plt.title("Log(Area) Distribution Over Time")
    plt.tight_layout()
    plt.show()

for i in range(5):
    heatmap(f"data{i+1}.xlsx")  # Adjust file names as needed


"""