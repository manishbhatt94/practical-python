# pcost.py
#
# Exercise 1.27


def portfolio_cost(filename):
    with open(filename) as file:
        total = 0
        _ = next(file)
        for line in file:
            _, qty, price = line.strip().split(",")
            qty = int(qty)
            price = float(price)
            total += qty * price
        return total


cost = portfolio_cost("Data/portfolio.csv")
print("Total cost:", cost)
