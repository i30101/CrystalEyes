"""
Andrew Kim

7 August 2025

Version 2.0.0

Extracts data from files that were already analyzed
"""


from ldf import LinkamDataFile

import pandas as pd
import numpy as np
import cv2
import os


"""
TODO debug this
"""



class LinkamDataReader:
    """ Extracts data from directories containing data already analyzed """

    @staticmethod
    def extract_data(filepath: str) -> LinkamDataFile:
        # pull out analyzed data from Excel file

        filename = filepath.split("/")[-1]

        analyzed_df = pd.read_excel(f"{filepath}/{filename}.ldf.xlsx")

        # get file names within directory
        raw_directory = f"{filepath}/raw"

        raw_image_paths = os.listdir(raw_directory)

        # get frame numbers
        frame_numbers = [
            int(path.replace("raw_", "").replace(".jpg", ""))
            for path in raw_image_paths
        ]

        # extract raw images
        raw_images = [cv2.cvtColor(cv2.imread(f"{raw_directory}/{image}", cv2.IMREAD_COLOR), cv2.COLOR_BGR2RGB) for image in raw_image_paths]

        # create LinkamDataFile object
        ldf = LinkamDataFile(
            file=filename,
            frames=frame_numbers,
            ramp=analyzed_df['Ramp number'].values.tolist(),
            temp=analyzed_df['Temperature (°C)'].values.tolist(),
            temp_limit=analyzed_df['Temperature limit (°C)'].values.tolist(),
            temp_rate=analyzed_df['Temperature rate (°C/min)'].values.tolist(),
            raw=raw_images  # Add the image paths to the raw parameter
        )

        # extract processed images
        processed_images = [cv2.imread(f"{filepath}/processed/{image}") for image in os.listdir(f"{filepath}/processed")]

        # extract ice crystal areas
        # TODO update this file path
        areas_df = pd.read_excel(f"{filepath}/{filename}.ldf_areas.xlsx")

        areas = [[v for v in areas_df[col] if pd.notna(v)] for col in areas_df.columns]

        # update processed data
        ldf.processed_images = processed_images
        ldf.image_areas = areas

        # fill in analyzed data
        ldf.data = [
            analyzed_df["Average area (px²)"].values.tolist(),
            analyzed_df["Average area (µm²)"].values.tolist(),
            analyzed_df["Total area (px²)"].values.tolist(),
            analyzed_df["Total area (µm²)"].values.tolist(),
            analyzed_df["Density (crystals/µm²)"].values.tolist(),
            analyzed_df["Coverage (%)"].values.tolist(),
            analyzed_df["Side ratio"].values.tolist(),
            analyzed_df["Number of contours"].values.tolist(),
            analyzed_df["Duration of analysis (s)"].values.tolist()
        ]

        return ldf
