"""
Andrew Kim

1 July 2025

Version 1.0.0

Analysis box
"""


import tkinter as tk
from tkinter import ttk

from databox import DataBox


class AnalyzeBox(DataBox):
    """ Box for analysis options and button """

    def __init__(self, root):
        super().__init__(root, "Analysis")

        self.box.grid_columnconfigure(0, weight=0)
        self.box.grid_columnconfigure(1, weight=0)
        self.box.grid_columnconfigure(2, weight=0)
        self.box.grid_columnconfigure(3, weight=0)
        self.box.grid_columnconfigure(4, weight=0)

        self.LABEL_WIDTH = 10
        self.ENTRY_WIDTH = 4

        # starting frame number
        self.starting_frame = tk.IntVar()
        self.starting_label = ttk.Label(self.box, text="Start frame", width=9)
        self.starting_label.grid(row=0, column=0, padx=0, pady=5, sticky="w")
        self.starting_entry = ttk.Entry(self.box, textvariable=self.starting_frame, width=self.ENTRY_WIDTH)
        self.starting_entry.grid(row=0, column=1, padx=(5, 0), pady=5, sticky="w")

        # ending frame number
        self.ending_frame = tk.IntVar()
        self.ending_label = ttk.Label(self.box, text="End frame", width=8)
        self.ending_label.grid(row=0, column=2, padx=(15, 0), pady=5, sticky="w")
        self.ending_entry = ttk.Entry(self.box, textvariable=self.ending_frame, width=self.ENTRY_WIDTH)
        self.ending_entry.grid(row=0, column=3, padx=(5, 0), pady=5, sticky="w")

        # analyze button
        self.analyze_button = ttk.Button(self.box, text="Analyze")
        self.analyze_button.grid(row=0, column=4, padx=(20, 0), pady=5, sticky="ew")

        # export button
        self.export_button = ttk.Button(self.box, text="Export")
        self.export_button.grid(row=0, column=5, padx=(20, 0), pady=5, sticky="ew")


        # bin controls
        self.bin_label = ttk.Label(self.box, text="Bins:", width=4)
        self.bin_label.grid(row=0, column=6, padx=(30, 0), pady=5, sticky="w")

        self.bin_decrease = ttk.Button(self.box, text="-", width=2)
        self.bin_decrease.grid(row=0, column=7, padx=(10, 0), pady=5, sticky="ew")

        self.bins = tk.IntVar(value=10)
        self.bin_entry = ttk.Entry(self.box, textvariable=self.bins, width=3, justify="center")
        self.bin_entry.grid(row=0, column=8, padx=(10, 0), pady=5, sticky="ew")

        self.bin_increase = ttk.Button(self.box, text="+", width=2)
        self.bin_increase.grid(row=0, column=9, padx=(10, 0), pady=5, sticky="ew")
