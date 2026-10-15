

import csv

def celsius_converter(f_temp):
    temperature_fahr = float(f_temp)
    temperature_C = (temperature_fahr-32)/1.8
    return round(temperature_C, 2)


def parse_and_clean(line):
    split_line = line.split("|")

    if len(split_line) != 5:
        return None

    cleaned_split_line = [element.strip() for element in split_line]

    if "" in cleaned_split_line:
        return None

    if cleaned_split_line[-1] != "ACTIVE":
        return None

    try:
        float(cleaned_split_line[2])
    except ValueError:
        return None

    return cleaned_split_line




skipped_lines = 0

with open("environmental_raw.txt", "r") as raw_line,\
     open("environmental_raw.csv", "w", newline="") as cleaned_line:
    
    writer = csv.writer(cleaned_line)

    writer.writerow([
    "Timestamp",
    "StationID",
    "Temp(°C)",
    "Humidity(%)",
    "Sensor_Status"
    ])

    for line in raw_line:
        if line.strip().lower().startswith("timestamp"):
            continue

        cleaned_data = parse_and_clean(line)

        if cleaned_data is None:
            skipped_lines += 1
            continue

        cleaned_data[2] = celsius_converter(cleaned_data[2])

        writer.writerow(cleaned_data)
        
print(f"corrupted lines: {skipped_lines}")
