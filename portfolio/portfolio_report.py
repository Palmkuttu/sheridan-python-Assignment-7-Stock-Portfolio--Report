import csv
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


# ⚠️ REQUIRED FOR test_api.py (DO NOT DELETE)
def get_market_data(symbols):
    """
    Dummy function for tests (no real API call)
    """
    return {}
