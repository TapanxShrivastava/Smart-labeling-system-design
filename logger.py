import csv
from datetime import datetime
import os

def log_inspection(label_data, result, log_file="logs.csv"):
    # Ensure the log file exists and has headers
    file_exists = os.path.isfile(log_file)
    
    with open(log_file, mode='a', newline='') as file:
        writer = csv.writer(file)

        # Write headers only once
        if not file_exists:
            writer.writerow([
                "Timestamp", "Device ID", "Batch ID", "Serial Number", 
                "Temperature (°C)", "Humidity (%)", "Location", "Status", 
                "Inspection Result"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            label_data.get("Device ID", ""),
            label_data.get("Batch ID", ""),
            label_data.get("Serial Number", ""),
            label_data.get("Temperature (°C)", ""),
            label_data.get("Humidity (%)", ""),
            label_data.get("Location", ""),
            label_data.get("Status", ""),
            result
        ])
