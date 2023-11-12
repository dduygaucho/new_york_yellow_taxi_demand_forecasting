import numpy as np
import pandas as pd
import subprocess
import os

folder_path = "./data/landing"

# links to weather datasets and mta subways
weather_link_2022 = \
    "https://www.ncei.noaa.gov/data/global-hourly/access/2022/74486094789.csv"
weather_link_2023 = \
    "https://www.ncei.noaa.gov/data/global-hourly/access/2023/74486094789.csv"
mta_link =  \
    "https://data.ny.gov/api/views/wujg-7c2s/rows.csv?accessType=DOWNLOAD&bom=true&format=true&sorting=true"

link_names = ['weather_link_2022.csv', 'weather_link_2023.csv', "mta_2023.csv"]
print(f"Current directory: {os.getcwd()}")


# start the download process
for ind, link in enumerate([weather_link_2022, weather_link_2023, mta_link]):
    output_path = f"{folder_path}/{link_names[ind]}"

    # this code piece is adopted from chatgpt
    # Command to run wget
    command = ["wget", link, "-O", output_path]
    # Run the wget command
    try:
        subprocess.run(command, check=True)
        print(f"Download {link} completed successfully.")
    except subprocess.CalledProcessError:
        print(f"Error {link} occurred during download.")
