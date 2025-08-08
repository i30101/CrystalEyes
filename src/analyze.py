"""
Andrew Kim

1 July 2025

Version 2.0.0

Analysis box
"""


import tkinter as tk
from tkinter import ttk

from databox import DataBox
from variables import Variables


class AnalyzeBox(DataBox):
    """ Box for analysis options and button """

    def __init__(self, root):
        super().__init__(root, "Analysis")

        self.box.grid_columnconfigure(0, weight=6)
        self.box.grid_columnconfigure(1, weight=4)

        self.ENTRY_WIDTH = 3


        # left column
        self.left_column = ttk.Frame(self.box)
        self.left_column.grid(column=0, row=0, sticky="w")

        self.starting_label = ttk.Label(self.left_column, text="Analyze frames ", width=12)
        self.starting_label.grid(row=0, column=0, padx=Variables.PAD_NOPAD, pady=5, sticky="w")

        self.starting_frame = tk.IntVar()
        self.starting_entry = ttk.Entry(self.left_column, textvariable=self.starting_frame, width=self.ENTRY_WIDTH)
        self.starting_entry.grid(row=0, column=1, padx=(3, 0), pady=5, sticky="w")

        self.to_label = ttk.Label(self.left_column, text="to", width=2)
        self.to_label.grid(row=0, column=2, padx=Variables.PAD_NOPAD, pady=5, sticky="w")

        self.ending_frame = tk.IntVar()
        self.ending_entry = ttk.Entry(self.left_column, textvariable=self.ending_frame, width=self.ENTRY_WIDTH)
        self.ending_entry.grid(row=0, column=3, padx=(3, 0), pady=5, sticky="w")

        self.histogram_label = ttk.Label(self.left_column, text="Histogram: from", width=13)
        self.histogram_label.grid(row=1, column=0, padx=Variables.PAD_NOPAD, pady=5, sticky="w")

        self.histogram_start = tk.IntVar(value=0)
        self.bin_start_entry = ttk.Entry(self.left_column, textvariable=self.histogram_start, width=self.ENTRY_WIDTH)
        self.bin_start_entry.grid(row=1, column=1, padx=(3, 0), pady=5, sticky="w")

        self.to_histogram_label = ttk.Label(self.left_column, text="to", width=3)
        self.to_histogram_label.grid(row=1, column=2, padx=Variables.PAD_NOPAD, pady=5, sticky="w")

        self.histogram_end = tk.IntVar(value=500)
        self.bin_end_entry = ttk.Entry(self.left_column, textvariable=self.histogram_end, width=self.ENTRY_WIDTH)
        self.bin_end_entry.grid(row=1, column=3, padx=(3, 0), pady=5, sticky="w")

        self.with_label = ttk.Label(self.left_column, text="µm² with", width=8)
        self.with_label.grid(row=1, column=4, padx=Variables.PAD_NOPAD, pady=5, sticky="w")

        self.bins = tk.IntVar(value=10)
        self.bin_entry = ttk.Entry(self.left_column, textvariable=self.bins, width=self.ENTRY_WIDTH)
        self.bin_entry.grid(row=1, column=5, padx=(3, 0), pady=5, sticky="w")

        self.bins_label = ttk.Label(self.left_column, text="bins", width=4)
        self.bins_label.grid(row=1, column=6, padx=Variables.PAD_NOPAD, pady=5, sticky="w")


        # right column

        self.right_column = ttk.Frame(self.box)
        self.right_column.grid(column=1, row=0, padx=10, sticky="e")

        self.export_button = ttk.Button(self.right_column, text="Export", width=10)
        self.export_button.grid(row=0, column=0, padx=Variables.PAD_NOPAD, ipadx=10, ipady=24, sticky="e")

        self.analyze_button = ttk.Button(self.right_column, text="Analyze", width=10)
        self.analyze_button.grid(row=0, column=1, padx=Variables.PAD_NOPAD, ipadx=10, ipady=24, sticky="e")
