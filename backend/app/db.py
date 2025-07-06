from motor.motor_asyncio import AsyncIOMotorClient
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")

client = AsyncIOMotorClient(MONGO_URI)
db = client[DATABASE_NAME]

async def insert_equity_list_async(csv_path: str):
    print(f"📁 Reading CSV from: {csv_path}")
    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.strip()
    df = df.dropna(subset=['SYMBOL'])
    df['SYMBOL'] = df['SYMBOL'].str.strip()

    records = df[["SYMBOL", "NAME OF COMPANY", "DATE OF LISTING", "ISIN NUMBER"]].rename(
        columns={
            "SYMBOL": "symbol",
            "NAME OF COMPANY": "company_name",
            "DATE OF LISTING": "date_of_listing",
            "ISIN NUMBER": "isin"
        }
    ).to_dict(orient="records")

    await db.equity_list.delete_many({})
    await db.equity_list.insert_many(records)
    print("✅ Equity list inserted successfully.")



async def insert_stock_reports_async(csv_folder_path: str):
    await db.stock_reports.delete_many({})  # Optional: Clean existing first

    for filename in os.listdir(csv_folder_path):
        if filename.endswith(".csv"):
            symbol = filename.split(".")[0]
            df = pd.read_csv(os.path.join(csv_folder_path, filename))
            df.columns = [col if not col.startswith("Unnamed") else "Metrics" for col in df.columns]
            df.columns = df.columns.str.strip()
            df = df[df.index.notna()]
            df = df[df["Section"].notna() & (df["Section"].str.strip() != "")]

            stock_data = {"symbol": symbol, "sections": {}}

            for section_name in df["Section"].unique():
                section_df = df[df["Section"] == section_name].drop(columns=["Section"])
                rows = section_df.to_dict(orient="records")

                stock_data["sections"][section_name] = rows

            await db.stock_reports.insert_one(stock_data)
    
    print("✅ Stock reports inserted as one document per stock.")