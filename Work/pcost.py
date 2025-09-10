# pcost.py


def portfolio_cost(filename):
    """Calculates the total cost of a stock portfolio ∑ (shares * price),
    given filename (path) of a portfolio CSV file containing
    (name, shares, price) records
    """
    with open(filename) as file:
        total = 0
        _ = next(file)
        for line in file:
            _, qty, price = line.strip().split(",")
            try:
                qty = int(qty)
                price = float(price)
                total += qty * price
            except ValueError:
                print("Invalid record:", line)
                continue
        return total


# cost = portfolio_cost("Data/portfolio.csv")
cost = portfolio_cost("Data/missing.csv")
print("Total cost:", cost)
