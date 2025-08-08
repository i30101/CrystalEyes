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

        analyzed_df = pd.read_excel(f"{filepath}/{filepath}.xlsx")

        # get file names within directory
        raw_directory = f"{filepath}/raw"

        raw_image_paths = os.listdir(raw_directory)

        # get frame numbers
        frame_numbers = [int(path[path.index("raw/")].replace("jpg", "")) for path in raw_image_paths]

        # extract raw images
        raw_images = [cv2.imread(f"{raw_directory}/{image}") for image in raw_image_paths]

        # create LinkamDataFile object
        ldf = LinkamDataFile(
            file=filepath,
            frames=frame_numbers,
            ramp=analyzed_df['Ramp'].values.tolist(),
            temp=analyzed_df['Temperature'].values.tolist(),
            temp_limit=analyzed_df['Temperature Limit'].values.tolist(),
            temp_rate=analyzed_df['Rate'].values.tolist(),
            raw=raw_images  # Add the image paths to the raw parameter
        )

        # extract processed images
        processed_images = [cv2.imread(f"{filepath}/processed/{image}") for image in os.listdir(f"{filepath}/processed")]

        # extract ice crystal areas
        # TODO update this file path
        areas_df = pd.read_excel(f"{filepath}/areas.xlsx")

        areas = [list(areas_df[col]) for col in areas_df.columns]

        # update processed data
        ldf.processed_images = processed_images
        ldf.image_areas = areas

        return ldf

