#Data Collection
#Istanbul Air Quality Project
#This file collects raw air quality data

import requests
from bs4 import BeautifulSoup
import pandas as pd

#Air quality web page
url = "https://www.iqair.com/turkey/istanbul/istanbul"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

#A raw dataset is created
#Demostrate data cleaning steps

raw_data = {
    "date": [
        "2024-09-01",
        "2024-09-02",
        "2024-09-03",
        "2024-09-04",
        "2024-09-05",
        None
    ],
    "pm25": [35,42,None,110,38,999],
    "pm10": [70,80,65,None,75,500]
}

df_raw = pd.DataFrame(raw_data)

#Save the raw dataset
df_raw.to_csv("istanbul_air_quality_raw.csv", index=False)

print("Raw air quality dataset collected and saved dataset.")
print(df_raw)
