import pandas as pd
import plotly.express as px

df=pd.read_csv("data/istanbul_air_quality_clean.csv")
df["date"]=pd.to_datetime(df["date"])
print("Dataset is loaded ready for web visualization.")
print(df.head())

fig=px.line(
    df,
    x="date",
    y=["pm25","pm10"],
    title="PM2.5 & PM10 Levels in Istanbul",
    labels={
        "date":"Date",
        "value":"Pollution Level",
        "variable":"Air Quality"
    }
)

fig.show()

print("Web visualization is done.")