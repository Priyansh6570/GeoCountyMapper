# GeoCountyMapper

GeoCountyMapper is a Python-based tool that processes latitude and longitude data to determine corresponding geographic areas (counties). It reads an input CSV, resolves errors using the Nominatim API, and outputs an updated CSV with enriched location details.

## Features
- Extracts county information from latitude and longitude.
- Saves results in a user-friendly CSV format.

## Usage
1. Provide an input CSV with `Subcell_ID`, `Longitude`, `Latitude`, and `Area` columns.
2. The tool fetches county details for missing or erroneous entries.
3. Outputs a new CSV with corrected "Area" data.

## Requirements
- Python 3.x
- Libraries: `pandas`, `requests`

## Installation
```bash
pip install pandas requests
