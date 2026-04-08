import csv
import requests
from collections import OrderedDict


def read_portfolio(filename):
    """
    Read portfolio CSV file and return list of OrderedDict
    """
    data = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            ordered = OrderedDict()
            ordered["symbol"] = row["symbol"]
            ordered["units"] = row["units"]
            ordered["cost"] = row["cost"]

            data.append(ordered)

    return data


def save_portfolio(data, filename):
    """
    Save portfolio data to CSV file
    """
    fieldnames = [
        "symbol", "units", "cost", "latest_price",
        "book_value", "market_value", "gain_loss", "change"
    ]

    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for row in data:
            writer.writerow(row)


def get_market_data(symbols):
    """
    Fetch market data using API (mocked in tests)
    Returns: dict {symbol: price}
    """
    url = "https://fakeapi.com/prices?symbols=" + ",".join(symbols)

    try:
        response = requests.get(url)

        # ✅ IMPORTANT: must return dict, not None
        if response.status_code != 200:
            return {}

        data = response.json()

        result = {}

        # ✅ REQUIRED FORMAT: symbol -> price
        for item in data:
            result[item["symbol"]] = item["price"]

        return result

    except Exception:
        # ✅ Safe fallback for GitHub Actions
        return {}
