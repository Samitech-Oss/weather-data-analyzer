import requests
import pandas as pd
import matplotlib.pyplot as plt

# 1. Fetch weather data
url = "https://wttr.in/Hangzhou?format=j1"
response = requests.get(url)
data = response.json()

# 2. Extract daily data
days = data["weather"]
records = []
for day in days:
    records.append({
        "date": day["date"],
        "avg_temp": day["avgtempC"],
        "max_temp": day["maxtempC"],
        "min_temp": day["mintempC"]
    })

# 3. Analyze with Pandas
df = pd.DataFrame(records)
print(df)

# 4. Plot temperature trend
plt.plot(df["date"], df["avg_temp"], marker="o")
plt.title("Average Temperature in Hangzhou")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()

# 5. Save to CSV
df.to_csv("weather_data.csv", index=False)
