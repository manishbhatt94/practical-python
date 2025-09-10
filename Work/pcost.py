# pcost.py

import csv


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


cost = portfolio_cost("Data/portfolio.csv")
# cost = portfolio_cost("Data/missing.csv")
print("Total cost:", cost)
