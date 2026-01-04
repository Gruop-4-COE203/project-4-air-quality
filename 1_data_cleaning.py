#Data Cleaning
#Istanbul Air Quality Project

#This file is collecting and cleaning the dataset
#that will be used analysis part

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

#Air quality web page(data source is referenced)
url = "https://www.iqair.com/turkey/istanbul/istanbul"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
raw_data = {
    "date": [
        "2024-09-01", "2024-09-02", "2024-09-03",
        "2024-01-04", "2024-01-05",  None
],
    "pm25": [35, 42, None, 110, 38, 999],
    "pm10": [70, 80, 65, None, 75, 500]
}
df_raw = pd.DataFrame(raw_data)

#Save raw data
df_raw.to_csv("data/istanbul_air_quality_raw.csv", index=False)

print("Raw dataset created.")
print("Raw Data before cleaning:")
print(df_raw)

#Data cleaning
df = df_raw.copy()
print("Before cleaning:",df.shape)

#Remove lines that do not contain date information
df = df.dropna(subset=["date"])

#Convert the data column to date and time format
df["date"] = pd.to_datetime(df["date"])

#Fill in missing values using column average
df["pm25"] = df["pm25"].fillna(df["pm25"].mean())
df["pm10"] = df["pm10"].fillna(df["pm10"].mean())

#Remove meaningless high values
df = df[(df["pm25"] < 300) & (df["pm10"] < 300)]

#Reset the directory after cleaning
df.reset_index(drop=True, inplace=True)
print("\nAfter cleaning:",df.shape)
#Save cleaned data
df.to_csv("data/istanbul_air_quality_clean.csv", index=False)
print("Cleaned dataset saved.")
print("Cleaned Data Preview:")
print(df.head())


