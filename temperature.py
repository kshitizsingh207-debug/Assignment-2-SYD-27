import os

import pandas as pd

import numpy as np

base_dir = os.path.dirname(os.path.abspath(__file__))

data_folder = os.path.join(base_dir, "temperatures")
output_folder = os.path.join(base_dir, "output")

os.makedirs(output_folder, exist_ok=True)

total_records = 0

seasonal_temps = {
    "Summer": [],
    "Autumn": [],
    "Winter": [],
    "Spring": []
}
station_temps = {}
most_stable_std=float("inf")
most_variable_std = -1
most_stable_stations = []
most_variable_stations = []

def get_season(month_name):
    if month_name in ["December","January","February"]:
        return "Summer"
    elif month_name in ["March","April","May"]:
        return "Autumn"
    elif month_name in ["June","July","August"]:
        return "Winter"
    else:
        return "Spring"

for file in os.listdir(data_folder):
    if file.endswith(".csv"):
        file_path = os.path.join(data_folder,file)
        df=pd.read_csv(file_path)
       
        months = ["January", "February", "March","April","May","June",
                  "July","August","September","October","November","December" ]
        
        df = df.dropna(subset=months,how="all")

        for month in months:
            month_values = df[month].dropna().tolist()
            total_records += len(month_values)
            season = get_season(month)
            seasonal_temps[season].extend(month_values)

        for _, row in df.iterrows():
            station = row["STATION_NAME"]
            
            if station not in station_temps:
                station_temps[station]= []
            
            for month in months:
                if not pd.isna(row[month]):
                    station_temps[station].append(row[month])
                
max_range = -1
range_stations = []

print("Total valid temperature record: ", total_records)

for station, temps in station_temps.items():
    temp_range = max(temps) - min(temps)
    if temp_range> max_range:
        max_range = temp_range
        range_stations = [station]
    elif temp_range == max_range:
                range_stations.append(station)

range_file = os.path.join(output_folder, "largest_temp_range_station.txt")

# Calculate average for each season
print("\nAverage temperature for each season across ALL stations and ALL years:")
avg_file = os.path.join(output_folder, "average_temp.txt")
with open(avg_file, "w") as f:
    for season, temps in seasonal_temps.items():
        avg_temp = np.mean(temps)
        if len(temps) > 0:
            avg_temp = np.mean(temps)
            f.write(f"{season}: {avg_temp:.2f}°C\n")
            print(f"{season}: {avg_temp:.2f}°C")
        else:
            f.write(f"{season}:No data\n")
            print(f"{season}:No data")

# Save largest temperature range
print("\nStation with the largest temperature range:")
with open(range_file, "w") as f:
    for station in range_stations:
        temps = station_temps[station]
        line = (
        f"Station {station}: Range {max(temps)-min(temps):.2f}°C "
        f"(Max: {max(temps):.2f}°C, Min: {min(temps):.2f}°C)"
            )
        print(line)
        f.write(line + "\n")