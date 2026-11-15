#-   Determine delivery charges: orders >= $500 have free delivery; otherwise, charge $50.
order_amount = float(input("Enter the order amount: "))
if order_amount >= 500:
    delivery_charge = 0
else:
    delivery_charge = 50
print("Delivery charge: $", delivery_charge)