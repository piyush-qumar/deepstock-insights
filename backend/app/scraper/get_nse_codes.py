from io import StringIO
import pandas as pd
import requests
import os
from datetime import datetime
import json

# Step 1: Fetch CSV
url = "https://archives.nseindia.com/content/equities/EQUITY_L.csv"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
response.raise_for_status() # raise exception if download fails

today = datetime.now().strftime("%Y-%m-%d")
# check if the data folder exists, if not create it
data_folder = os.path.join(os.getcwd(), "data")
os.makedirs(data_folder, exist_ok=True)

csv_path = os.path.join(data_folder, f"nse_equity_list.csv")

#filename = f"nse_equity_list_{today}.csv"
with open(csv_path, "w", encoding='utf-8') as f:
    f.write(response.text)

# Step 2: Read CSV into DataFrame
df = pd.read_csv(StringIO(response.text), encoding='utf-8')
df.columns = df.columns.str.strip()  # Clean column names
df = df.dropna(subset=['SYMBOL'])  # Drop rows without stock symbols
df['SYMBOL'] = df['SYMBOL'].str.strip()  # Clean stock symbols

# Step 3: Define the fields you want to include
fields_to_extract = [
    'NAME OF COMPANY',
    'DATE OF LISTING',
    'ISIN NUMBER',
    'FACE VALUE',
    'INDUSTRY',
    'PAID UP VALUE',
    'MARKET LOT',
    'SERIES'
]

# Step 4: Create the mapping dictionary
ticker_info_map = {
    row['SYMBOL']: {
        key.lower().replace(" ", "_"): row[key]
        for key in fields_to_extract if key in row
    }
    for _, row in df.iterrows()
}

# Save the mapping to a JSON file
json_path = os.path.join(data_folder, "ticker_info_map.json")
with open(json_path, "w", encoding='utf-8') as f:
    json.dump(ticker_info_map, f, indent=4)


