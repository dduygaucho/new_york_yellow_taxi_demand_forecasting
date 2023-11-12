from urllib.request import urlretrieve
import os
import subprocess

# this code is partially adopted from python prerequisite notebook
# provided by the course and used ChatGPT for visualization aiding only

# adjust the range function to the numerical months i.e 1 = jan, 2 = feb, etc...
# MONTHS = range(1, 13)
URL_TEMPLATE = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_"
print("Downloading ")
OUTPUT_DIR = './data/landing'

# Create the directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs("./data/landing/taxi_zones", exist_ok= True)



def download_files(year, months, url_template, output_dir):
    """
    This function is used to download all the files specified in year and 
    months. All files will be downloaded to output_dir, which is landing layer
    """
    for month in months:
    # 0-fill i.e 1 -> 01, 2 -> 02, etc
        month = str(month).zfill(2) 
        print(f"Begin month {month}")
        
        # generate url
        url = f'{url_template}{year}-{month}.parquet'
        # generate output location and filename
        file_dir = f"{output_dir}/{year}-{month}.parquet"
        # download
        urlretrieve(url, file_dir) 
        
        print(f"Completed month {month}")

# 
def download_taxi_zone(link):
    """
    This function is used to download the taxi zone.csv for further analysis
    based on a given link.
    This is saved into the landing layer output_path below
    """
    output_path = "./data/landing/taxi_zones.csv"
    # Command to run wget
    command = ["wget", link, "-O", output_path]
    # Run the wget command
    try:
        subprocess.run(command, check=True)
        print(f"Download {link} completed successfully.")
    except subprocess.CalledProcessError:
        print(f"Error {link} occurred during download.")

# https://d37ci6vzurychx.cloudfront.net/misc/taxi_zones.zip

def download_taxi_zones_zip(link):
    """
    This function is used to download the zip file of taxi zone shape files
    It also unzips the .zip file; however, be cautioned that it might not 
    work if permission is denied.
    In that case, manually create taxi_zones folder
    Then unzip all the shape files in this folder
    """
    # Local directory where you want to save the downloaded zip file
    local_dir = f"./data/landing/taxi_zones"

    # Download the zip file using wget
    subprocess.run(["wget", link, "-P", local_dir])

    # Path to the downloaded zip file
    zip_file_path = f"{local_dir}/taxi_zones.zip"

    # Unzip the downloaded file using the unzip command
    subprocess.run(["unzip", zip_file_path, "-d", local_dir])

    print("Files extracted successfully.")




download_files('2022', range(2,13), URL_TEMPLATE, OUTPUT_DIR)
download_files('2023', range(1,3), URL_TEMPLATE, OUTPUT_DIR)
download_taxi_zone("https://d37ci6vzurychx.cloudfront.net/misc/taxi+_zone_lookup.csv")
download_taxi_zones_zip("https://d37ci6vzurychx.cloudfront.net/misc/taxi_zones.zip")




