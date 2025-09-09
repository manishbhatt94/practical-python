# pcost.py
#
# Exercise 1.27

with open("Data/portfolio.csv") as file:
    total = 0
    _ = next(file)
    for line in file:
        _, qty, price = line.strip().split(",")
        qty = int(qty)
        price = float(price)
        total += qty * price

print("Total cost", round(total, 2))
