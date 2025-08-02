import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("room_log.csv")

# Drop final row if it's the average
data = data[~data['Timestamp'].str.contains("----")]

# Convert values
temp = data['Temperature (°C)']
hum = data['Humidity (%)']

# Create plot
plt.figure(figsize=(12, 6))

# Plot temperature
plt.plot(temp, label="Temperature (°C)", marker='o', color='tomato')
# Plot humidity
plt.plot(hum, label="Humidity (%)", marker='s', color='dodgerblue')

# Add threshold lines
plt.axhline(y=38, color='red', linestyle='--', label="High Temp (38°C)")
plt.axhline(y=30, color='blue', linestyle='--', label="Low Humidity (30%)")

# Titles and labels
plt.title("Smart Room Sensor Readings (Temp & Humidity)")
plt.xlabel("Reading Number")
plt.ylabel("Sensor Values")
plt.legend()
plt.grid(True)

# Save the dashboard image
plt.savefig("dashboard.png")
plt.show()
