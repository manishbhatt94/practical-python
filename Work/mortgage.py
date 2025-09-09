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

    # Monthly installment payment handling
    if (curr_principal := principal * (1 + rate / 12)) < payment:
        principal = 0
        total_paid = total_paid + curr_principal
    else:
        principal = curr_principal - payment
        total_paid = total_paid + payment

    # Extra payment months handling
    if extra_payment_start_month <= month <= extra_payment_end_month:
        if principal < extra_payment:
            principal = 0
            total_paid = total_paid + principal
        else:
            principal = principal - extra_payment
            total_paid = total_paid + extra_payment

    # Log current month's payment info
    print(f"{month:>3d} {round(total_paid, 2):>10.2f} {round(principal, 2):>10.2f}")


print("Total paid", total_paid)
print("Months", month)
