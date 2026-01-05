"""Web visualization"""

import pandas as pd
import plotly.express as px

#Load cleaned air quality dataset
df=pd.read_csv("data/istanbul_air_quality_clean.csv")
#Concert date column from string to datetime format for time-based analysis
df["date"]=pd.to_datetime(df["date"])
print("Dataset is loaded ready for web visualization.")
print(df.head())

#" This creates a web-based line chart that allows,
#comparison of PM2.5 and PM10 values on the same graph.
fig=px.line(
    df,
    x="date",
    y=["pm25","pm10"],
    title="PM2.5 & PM10 Levels by Date in Istanbul(2024)",
    labels={
        "date":"Date",
        "value":"Pollution Level",
        "variable":"Air Quality"
    }
)

fig.show()
print("Web visualization is done.")
