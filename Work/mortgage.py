# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment = 1000
extra_payment_start_month = 5 * 12 + 1  # 61
extra_payment_end_month = (5 + 4) * 12  # 108

while principal > 0:
    month = month + 1
    principal = principal * (1 + rate / 12) - payment
    if extra_payment_start_month <= month <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment
    total_paid = total_paid + payment
    print(f"{month} {round(total_paid, 2)} {round(principal, 2)}")

print("Total paid", total_paid)
print("Months", month)
