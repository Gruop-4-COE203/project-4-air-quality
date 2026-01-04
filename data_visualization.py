import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("data/istanbul_air_quality_clean.csv")
df["date"]=pd.to_datetime(df["date"])

print("Dataset is loaded and ready for visualization.")
print(df.head())

plt.figure(figsize=(10,5))
sns.lineplot(data=df,x="date",y="pm25",markers="o")
plt.title("PM2.5 Levels Over Time in Istanbul")
plt.xlabel("Date")
plt.ylabel("PM2.5")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,5))
sns.lineplot(data=df, x="date", y="pm10", marker="o")
plt.title("PM10 Levels Over Time in Istanbul")
plt.xlabel("Date")
plt.ylabel("PM10")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,5))
sns.boxplot(y="pm25", data=df)
plt.title("Distribution of PM2.5 Levels")
plt.ylabel("PM2.5")
plt.show()

plt.figure(figsize=(10,5))
sns.boxplot(y="pm10", data=df)
plt.title("Distribution of PM10 Levels")
plt.ylabel("PM10")
plt.show()


plt.figure(figsize=(15,6))
sns.lineplot(data=df, x="date", y="pm25", marker="o", label="PM2.5")
sns.lineplot(data=df, x="date", y="pm10", marker="o", label="PM10")
plt.title("PM2.5 & PM10 Levels Over Time in Istanbul")
plt.xlabel("Date")
plt.ylabel("Air Pollution")
plt.xticks(rotation=45)
plt.legend() 
plt.tight_layout()
plt.show()

print("All visualizations are done.")