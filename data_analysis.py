"""Data Analysis"""
import pandas as pd

try:
    df = pd.read_csv("data/istanbul_air_quality_clean.csv")
except FileNotFoundError as exc:
    raise FileNotFoundError("Clean dataset not found: data/istanbul_air_quality_clean.csv") from exc
except pd.errors.EmptyDataError as exc:
    raise ValueError("Clean dataset is empty.") from exc
except Exception as exc:
    raise RuntimeError(f"Unexpected error while loading dataset: {exc}") from exc

try:
    df["date"] = pd.to_datetime(df["date"])
except KeyError as exc:
    raise KeyError("Column 'date' not found in dataset.") from exc
except Exception as exc:
    raise ValueError(f"Date conversion failed: {exc}") from exc

required_columns = ["pm25", "pm10"]
for col in required_columns:
    if col not in df.columns:
        raise ValueError(f"Required column '{col}' is missing from dataset.")

#Add a city column with a constant value
df["city"]="Istanbul"
print("Dataset loaded successfully.")
print("Dataset shape:",df.shape)
print("\n----Air Quality of Istanbul----")
print(df.head())

print("\n----All Numerical Values of PM2.5 and PM10----")
#This shows count, mean,min and max values for air pollution
print(df[["pm25","pm10"]].describe())

print("\n----DataFrame Info----")
#This shows the number of entries, column names, non-null counts, and data types
print(df.info())


#Calculate mean,min and max values for PM2.5 and PM10
#PM2.5 and PM10 are particulate matter indicators used to assess air pollution levels

#Calculations
print("\n----Calculations of PM2.5 and PM10---")
print("These calculations summarize the average, maximum, and minimum"
      " daily air pollution levels in Istanbul.\n")

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


#Since PM10 is more variable, more detailed statistical analysis is performed
#and the data is divided into parts for visualization purposes.
print(df["pm10"].describe())

#Since PM10 values show higher variability,segments are created to better analyze
#the data distribution.Quartiles lower_part,median_part,upper_part) and the
#interquartile range (IQR) are calculated.
lower_part=df["pm10"].quantile(0.25)
median_part=df["pm10"].quantile(0.50)
upper_part=df["pm10"].quantile(0.75)

#IQR provides a robust measure of variability that is less affected by outliers than the mean
IQR=upper_part-lower_part
print("\n----PM10 Parts & Spread----")
print(f"Lower Part of PM10:{lower_part}")
print(f"Median Part of PM10 (median value):{median_part}")
print(f"Upper Part of PM10:{upper_part}")
print(f"IQR (Interquartile Range/middle %50 spread):{IQR}")
print("\nData analysis completed.")
