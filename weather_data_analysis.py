import pandas as pd
import datetime as dt

df = pd.read_csv("weather.csv")
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month
print("Weather Data:")
print(df)
print("\nMax Temperature:", df["Temperature"].max())
print("Min Temperature:", df["Temperature"].min())
monthly_avg = df.groupby("Month")["Temperature"].mean()
print("\nMonthly Average Temperature:")
print(monthly_avg)