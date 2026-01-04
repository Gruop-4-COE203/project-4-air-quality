import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Load cleaned air quality dataset
df=pd.read_csv("data/istanbul_air_quality_clean.csv")
#Concert date column from string to datetime format for time-based analysis
df["date"]=pd.to_datetime(df["date"])

print("Dataset is loaded and ready for visualization.")
print(df.head())

#This line plot shows the detailed temporal variation of PM2.5 values over time
plt.figure(figsize=(10,5))
sns.lineplot(data=df,x="date",y="pm25",marker="o")
plt.title("PM2.5 Levels by Date in Istanbul(2024)")
plt.xlabel("Date")
plt.ylabel("PM2.5")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#This line plot shows the detailed temporal variation of PM10 values over time
plt.figure(figsize=(10,5))
sns.lineplot(data=df, x="date", y="pm10", marker="o")
plt.title("PM10 Levels by Date in Istanbul(2024)")
plt.xlabel("Date")
plt.ylabel("PM10")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#While the line plot shows temporal changes,this boxplot shows the overall
#distribution and spread of PM2.5 values.
plt.figure(figsize=(10,5))
sns.boxplot(y="pm25", data=df)
plt.title("Distribution of PM2.5 Levels")
plt.ylabel("PM2.5")
plt.show()

#This boxplot shows the overall distribution and spread of PM10 values
plt.figure(figsize=(10,5))
sns.boxplot(y="pm10", data=df)
plt.title("Distribution of PM10 Levels")
plt.ylabel("PM10")
plt.show()

#This graph shows the temporal changes of PM2.5 and PM10 values together
plt.figure(figsize=(15,6))
sns.lineplot(data=df, x="date", y="pm25", marker="o", label="PM2.5")
sns.lineplot(data=df, x="date", y="pm10", marker="o", label="PM10")
plt.title("PM2.5 & PM10 Levels by Date in Istanbul(2024)")
plt.xlabel("Date")
plt.ylabel("Air Pollution")
plt.xticks(rotation=45)
plt.legend() 
plt.tight_layout()
plt.show()

print("All visualizations are done.")