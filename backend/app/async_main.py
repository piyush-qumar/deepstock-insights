import asyncio

from db import insert_equity_list_async, insert_stock_reports_async

async def main():
    await insert_equity_list_async("scraper/data/nse_equity_list.csv") #TODO: Update the date in the filename
    # Insert stock reports from the specified directory
    await insert_stock_reports_async("scraper/stock_reports/")   # Adjust the path as needed for both the files

if __name__ == "__main__":
    asyncio.run(main())
