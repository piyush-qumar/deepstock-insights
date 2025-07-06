import os
import requests
import pandas as pd
import json
from bs4 import BeautifulSoup
from collections import defaultdict
import time
import random

def fetch_stock_data(ticker: str, save_dir="stock_reports"):
    url = f"https://www.screener.in/company/{ticker}/consolidated"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"❌ Failed to fetch data for {ticker}. Status code: {response.status_code}")
    
    soup = BeautifulSoup(response.content, 'html.parser')
    all_tables = soup.find_all("table", class_="data-table")
    section_counts = defaultdict(int)
    
    # All sections will be appended to this list
    combined_df_parts = []

    for table in all_tables:
        heading = table.find_previous(["h2", "h3"])
        section_title = heading.text.strip().replace('+', '') if heading else "Unknown Section"
        # section_title = heading.text.strip() if heading else "Unknown Section"
        section_counts[section_title] += 1

        # Differentiate repeated sections like Shareholding
        if section_counts[section_title] == 2:
            section_title += " (Yearly)"
        elif section_counts[section_title] > 2:
            section_title += f" ({section_counts[section_title]})"
        else:
            section_title += " (Quarterly)" if "Shareholding" in section_title else ""

        # Extract headers and rows
        headers = [th.get_text(strip=True).replace('+', '') for th in table.find("thead").find_all("th")]
        rows = [
            [td.get_text(strip=True).replace(",", "").replace('+', '') for td in row.find_all("td")]
            for row in table.find("tbody").find_all("tr")
        ]
        if not rows or not headers:
            continue

        df = pd.DataFrame(rows, columns=headers[:len(rows[0])])
        df.insert(0, "Section", section_title)

        # Add empty row for visual separation
        empty_row = pd.DataFrame([[""] * df.shape[1]], columns=df.columns)
        combined_df_parts.extend([df, empty_row])

    # Combine and save
    final_df = pd.concat(combined_df_parts, ignore_index=True)
    
    os.makedirs(save_dir, exist_ok=True)
    output_path = os.path.join(save_dir, f"{ticker}.csv")
    final_df.to_csv(output_path, index=False)
    print(f"✅ Consolidated CSV saved: {output_path}")

# Example usage
if __name__ == "__main__":
    # fetch_stock_data("BEL", save_dir="stock_reports")
     with open("data/ticker_info_map.json", "r", encoding="utf-8") as f:
        ticker_map = json.load(f)
        tickers = list(ticker_map.keys())
        save_dir = "stock_reports"
        os.makedirs(save_dir, exist_ok=True)
        for ticker in tickers:
            try:
                fetch_stock_data(ticker, save_dir)
                time.sleep(random.uniform(1, 2)) 
            except Exception as e:
                print(f"❌ Error fetching data for {ticker}: {e}")
            


