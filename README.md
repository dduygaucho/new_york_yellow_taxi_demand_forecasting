# New York Yellow Taxi Demand Forecasting and Analysis - README.md
- Name: `Ngoc Duy Tran`

All the requirements for dependencies are currently set in requirements.txt. Besides this repo acknowledges the use of ChatGPT for more understanding about visualizations, yet this by no means affects the core results and original ideas

## README 

**Research Goal:** This research focuses on hourly prediction for highly-demanded taxi boroughs to help the target audience TLC answer a million-dollar question: Given the data in a borough from the previous w = 96 hours, what are the predictions for yellow taxi demand in the next k = 8 hours? This research focuses on Yellow Taxi due to its flexibility, in which they have no restrictions in picking up, including Manhattan, the core borough of this study. 

**Timeline:** The timeline for the research area is Feb 2022 - Feb 2023.

To run the pipeline, please follows all the steps and run the files in sequential order:


To download all datasets into landing layer, please visit the `scripts` directory and run the files in order:
1. `download_taxi.py`: This downloads all raw data within the specified range from TLC website into the `data/landing` directory. To run: python3 download_taxi.py. Note that when downloading the taxi_zone folder from tlc trip record, unzip might be denied due to permission issues. To fix: manually unzip and remove the .zip file in the ./data/landing/taxi_zones
2. `download_mta_weather.py`: This downloads all raw data 2022-2023 datasets for Weather (Integrated Surface Database) and MTA Subway Hourly Ridership (data.ny.gov) into the `data/landing` directory.


To preprocess from landing layer to raw layer, please visit the `notebooks` directory and run the files in order:
1. `preprocess_landing_to_raw_taxi.ipynb`: This notebook details all preprocessing steps and outputs it to the `data/raw` directory.
2. `preprocess_landing_to_raw_mta_weather.ipynb`: This notebook is used to conduct analysis on the curated data.
3. `preprocess_raw_to_curated.ipynb`: This notebok is used to transform raw layer datasets into curated layers with dataframes which are ready for further analysis and visualization.
4. `preprocess_curated_to_analysis.ipynb`: This notebok is used to transform curated layer datasets for model training and visualization. This contains code for visualization
5. `Hourly demand modelling.ipynb`:  The notebook is used for training the model. Discussion and analysis is also conducted in the notebook as limitations in GPU, will have to rerun on colab to get the results
