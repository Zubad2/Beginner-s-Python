#-   Calculate a store discount: below $100, no discount; $100-299, 5%; $300 or more, 10%.
A= int (input("Enter the amount: "))
if A >= 300:
    d= 0.1
elif A >= 100:
    d= 0.05
else:
    d= 0
discounted_price= A*(1-d)
print("Your discounted price is: ", discounted_price)

