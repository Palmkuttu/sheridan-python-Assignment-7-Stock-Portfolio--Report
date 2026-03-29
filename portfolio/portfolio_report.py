from collections import OrderedDict
import csv

def read_portfolio(filename):
    data = []
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            item = OrderedDict()
            item["symbol"] = row["symbol"]
            item["units"] = row["units"]
            item["cost"] = row["cost"]
            data.append(item)
    return data

def save_portfolio(data, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["symbol", "units", "cost"])
        writer.writeheader()

        for item in data:
            writer.writerow(item)


def get_args(args=None):
    parser = argparse.ArgumentParser(description="Portfolio Report")
    parser.add_argument("filename")
    return parser.parse_args(args)


def main():
    args = get_args()
    data = read_portfolio(args.filename)

    for item in data:
        print(item)


if __name__ == "__main__":
    main()
