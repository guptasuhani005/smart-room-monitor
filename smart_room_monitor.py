import random
import time
from datetime import datetime
import csv

# Thresholds
HIGH_TEMP = 38
LOW_HUMIDITY = 30

# Create lists to store values for averages
temps = []
humidities = []

# Open CSV for writing
with open("room_log.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Temperature (°C)", "Humidity (%)", "Status"])

    for i in range(20):  # 20 readings
        temp = round(random.uniform(18.0, 45.0), 2)
        humidity = round(random.uniform(20.0, 90.0), 2)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Save values for average later
        temps.append(temp)
        humidities.append(humidity)

        # Alert logic
        if temp > HIGH_TEMP and humidity < LOW_HUMIDITY:
            status = "🔥 Risk: Overheating & Dry"
        elif temp > HIGH_TEMP:
            status = "⚠️ High Temperature"
        elif humidity < LOW_HUMIDITY:
            status = "💧 Low Humidity"
        else:
            status = "✅ Normal"

        print(f"[{timestamp}] Temp: {temp}°C | Humidity: {humidity}% → {status}")
        writer.writerow([timestamp, temp, humidity, status])
        time.sleep(1)

    # Calculate and write averages (INSIDE the with-block)
    avg_temp = round(sum(temps) / len(temps), 2)
    avg_hum = round(sum(humidities) / len(humidities), 2)

    writer.writerow(["----", "Avg Temp", "Avg Humidity", f"{avg_temp}°C | {avg_hum}%"])
    print(f"\n📊 Average Temp: {avg_temp}°C | Average Humidity: {avg_hum}%")

