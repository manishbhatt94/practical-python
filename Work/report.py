# report.py
#
# Exercise 2.4

import csv
import sys


def read_portfolio(filename):
    """Given filename (path) of a portfolio CSV file containing
    (name, shares, price) records, read the file & return a list of
    (name, shares, price) tuples.
    """
    portfolio = []
    with open(filename, "rt", newline="") as file:
        reader = csv.reader(file)
        _ = next(reader)  # skip the header row
        for row in reader:
            try:
                holding = (row[0], int(row[1]), float(row[2]))
                portfolio.append(holding)
            except ValueError:
                print("Invalid record:", row)
                continue
    return portfolio


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

portfolio = read_portfolio(filename)
print("Portfolio:", portfolio)
