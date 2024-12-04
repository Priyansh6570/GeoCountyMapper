import pandas as pd
import requests

def get_area_from_coords(latitude, longitude):
    try:
        url = "https://nominatim.openstreetmap.org/reverse"
        params = {
            "lat": latitude,
            "lon": longitude,
            "format": "json",
            "addressdetails": 1
        }
        headers = {
                "User-Agent": "PRIYANSH1234/1.0 (priyanshmishra20052003@gmail.com)"
            }
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        if "address" in data and "county" in data["address"]:
            return data["address"]["county"]
        else:
            return "Unknown Area"
    except Exception as e:
        return f"Error: {e}"

input_file = "input.csv"
output_file = "output.csv"

df = pd.read_csv(input_file)
df["Area"] = df.apply(lambda row: get_area_from_coords(row["Latitude"], row["Longitude"]), axis=1)

df.to_csv(output_file, index=False)

print(f"Updated file saved as {output_file}")