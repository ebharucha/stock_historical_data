# Stock Historical Data Downloader

A simple Python utility to download historical stock market data using the Yahoo Finance API (`yfinance`).

## Features

- **Interactive CLI**: Prompts for stock symbol, timeframe, date range, and output format.
- **Flexible Timeframes**: Supports daily (`1d`) and weekly (`1wk`) data.
- **Multiple Formats**: Save data as CSV or Excel (`.xlsx`).
- **Organized Output**: Automatically saves all downloaded files into a `data/` directory.
- **Data Integrity**: Handles splits and dividends automatically via `yfinance`.

## Prerequisites

- Python 3.x
- `pip` (Python package installer)

## Installation

1.  **Clone the repository** (or download the files):
    ```bash
    git clone <repository-url>
    cd stock_historical_data
    ```

2.  **Set up a virtual environment** (recommended):
    ```bash
    # Windows
    python -m venv .venv
    .venv\Scripts\activate

    # macOS/Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the script from your terminal:

```bash
python stock_data_downloader.py
```

Follow the on-screen prompts:

1.  **Stock Symbol**: Enter the ticker symbol (e.g., `AAPL`, `MSFT`, `TSLA`).
2.  **Timeframe**: Choose `daily` or `weekly`.
3.  **Duration**: Enter the Start Date and End Date in `MM/DD/YYYY` format.
4.  **Output Format**: Choose `csv` or `excel`.

## Output

Downloaded files are saved in the `data/` directory with the naming convention:
`{SYMBOL}_data_{START_DATE}_to_{END_DATE}.{extension}`

Example: `data/AAPL_data_2023-01-01_to_2023-12-31.csv`
