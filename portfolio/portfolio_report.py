import csv
import requests
from collections import OrderedDict


# ---------------------------
# READ PORTFOLIO
# ---------------------------
def read_portfolio(filename):
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


# ---------------------------
# SAVE PORTFOLIO
# ---------------------------
def save_portfolio(data, filename):
    with open(filename, "w", newline="") as file:
        fieldnames = ["symbol", "units", "cost"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for row in data:
            writer.writerow(row)


# ---------------------------
# API FUNCTION
# ---------------------------
def get_market_data(symbols):
    symbols_str = ",".join(symbols)

    # MUST match test exactly
    url = f"https://fakeapi.com/prices?symbols={symbols_str}"

    response = requests.get(url)
    data = response.json()

    result = {}
    for item in data:
        result[item["symbol"]] = item["price"]

    return result


# ---------------------------
# CALCULATE METRICS (REQUIRED)
# ---------------------------
def calculate_metrics(portfolio, prices):
    results = []

    for stock in portfolio:
        symbol = stock["symbol"]
        units = int(stock["units"])
        cost = float(stock["cost"])
        price = prices[symbol]

        book_value = units * cost
        market_value = units * price
        gain_loss = market_value - book_value

        if book_value != 0:
            change = gain_loss / book_value
        else:
            change = 0

        results.append({
            "symbol": symbol,
            "book_value": book_value,
            "market_value": market_value,
            "gain_loss": gain_loss,
            "change": change
        })

    return results


# ---------------------------
# MAIN
# ---------------------------
def main():
    import argparse

    parser = argparse.ArgumentParser(description="Portfolio Report")
    parser.add_argument("file", help="CSV file path")

    args = parser.parse_args()

    portfolio = read_portfolio(args.file)
    symbols = [stock["symbol"] for stock in portfolio]

    prices = get_market_data(symbols)
    metrics = calculate_metrics(portfolio, prices)

    for item in metrics:
        print(item)


if __name__ == "__main__":
    main()
