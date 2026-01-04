import pandas as pd
import numpy as np

df=pd.read_csv("data/istanbul_air_quality_clean.csv")

df["date"]=pd.to_datetime(df["date"])
df["city"]="Istanbul"
print("Dataset loaded successfully.")
print("Dataset shape:",df.shape)
print("\n----Air Quality of Istanbul----")
print(df.head())

print("\n----All Numerical Values ​​of PM2.5 and PM10----")
#This shows count, mean, std, min and max values for air pollution:
print(df[["pm25","pm10"]].describe())

print("\n----DataFrame Info----")
#This shows the number of entries, column names, non-null counts, and data types:
print(df.info())

#Calculations
print("\n----Calculations of PM2.5 and PM10---")
print("These calculations summarize the average, maximum, and minimum daily air pollution levels in Istanbul.\n")

pm25_mean = df["pm25"].mean()
pm25_max = df["pm25"].max()
pm25_min = df["pm25"].min()

print("Average of PM2.5 (general air pollution level):",pm25_mean)
print("Maximum value of PM2.5 (most polluted day):",pm25_max)
print("Minimum value of PM2.5 (cleanest day):",pm25_min)

pm10_mean = df["pm10"].mean()
pm10_max = df["pm10"].max()
pm10_min = df["pm10"].min()
print("\nAverage of PM10 (general air pollution level):",pm10_mean)
print("Maximum value of PM10 (most polluted day):",pm10_max)
print("Minimum value of PM10 (cleanest day):",pm10_min)


#Since PM10 data is more variable than PM2.5, the average alone is not sufficient.
print("\n----PM10 Summary----")
print(df["pm10"].describe())

lower_part=df["pm10"].quantile(0.25)
median_part=df["pm10"].quantile(0.50)
upper_part=df["pm10"].quantile(0.75)
IQR=upper_part-lower_part

print("\n----PM10 Parts & Spread----")
print(f"Lower Part of PM10:{lower_part}")
print(f"Median Part of PM10 (median value):{median_part}")
print(f"Upper Part of PM10:{upper_part}")
print(f"IQR (Interquartile Range/middle %50 spread):{IQR}")

print("\nData analysis completed.")

