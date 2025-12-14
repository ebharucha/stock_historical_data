# @ebharucha 12/14/2025

import yfinance as yf
import pandas as pd
from datetime import datetime
import sys

def get_valid_date(prompt):
    """Prompts user for a date and validates the format."""
    while True:
        date_str = input(prompt)
        try:
            # Parse MM/DD/YYYY
            dt_obj = datetime.strptime(date_str, "%m/%d/%Y")
            # Return in YYYY-MM-DD format required by yfinance
            return dt_obj.strftime("%Y-%m-%d")
        except ValueError:
            print("Invalid format. Please use MM/DD/YYYY (e.g., 01/31/2023).")

def download_historical_data():
    print("--- Yahoo Finance Data Downloader ---\n")

    # 1. Input: Stock Symbol
    symbol = input("1. Enter Stock Symbol (e.g., AAPL, TSLA): ").upper().strip()

    # 2. Input: Timeframe
    while True:
        timeframe_input = input("2. Enter Timeframe (daily/weekly): ").lower().strip()
        if timeframe_input in ['daily', 'd']:
            interval = '1d'
            break
        elif timeframe_input in ['weekly', 'w']:
            interval = '1wk'
            break
        else:
            print("Invalid input. Please type 'daily' or 'weekly'.")

    # 3. Input: Duration (Start and End Date)
    print("3. Enter Duration (Format: MM/DD/YYYY)")
    start_date = get_valid_date("   Start Date: ")
    end_date = get_valid_date("   End Date:   ")

    # 4. Output Format Selection
    while True:
        file_format = input("4. Output format (csv/excel): ").lower().strip()
        if file_format in ['csv', 'excel', 'xlsx']:
            break
        print("Please choose 'csv' or 'excel'.")

    print(f"\nDownloading data for {symbol}...")

    try:
        # Fetch data
        # auto_adjust=True fixes historical splits and dividends
        df = yf.download(symbol, start=start_date, end=end_date, interval=interval, progress=False)

        if df.empty:
            print(f"No data found for {symbol}. Please check the symbol and dates.")
            return

        # Save to file
        filename = f"{symbol}_data_{start_date}_to_{end_date}"
        
        if file_format == 'csv':
            filename += ".csv"
            df.to_csv(filename)
        else:
            filename += ".xlsx"
            # Requires openpyxl
            df.to_excel(filename)

        print(f"Success! Data saved to: {filename}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    download_historical_data()