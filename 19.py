#-   Determine movie ticket price based on age: child (below 12), $8; adult, $15; senior (60+), $10.
age = int(input("Enter your age: "))
if age < 12:
    price = 8
elif age >= 60:
    price = 10
else:
    price = 15
print("Your ticket price is: $", price)
