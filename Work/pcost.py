# pcost.py

import csv
import sys


def portfolio_cost(filename):
    """Calculates the total cost of a stock portfolio ∑ (shares * price),
    given filename (path) of a portfolio CSV file containing
    (name, shares, price) records
    """
    with open(filename, "rt", newline="") as file:
        reader = csv.reader(file)
        total = 0
        _ = next(reader)  # skip the header row
        for row in reader:
            try:
                qty = int(row[1])
                price = float(row[2])
                total += qty * price
            except ValueError:
                print("Invalid record:", row)
                continue
        return total


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

cost = portfolio_cost(filename)
print("Total cost:", cost)
