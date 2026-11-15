#-   Calculate concert ticket prices and discounts. (Not full question)
p= 20
d = 0
a= int(input("How many tickets do you wanna buy??: "))
if a>25:
    print("invalid")
elif a>=20:
    d= 0.2
elif a>=10:
    d= 0.1
print("Your discount is: ", d)

total= a*p*(1-d)
print("Your total is: ", total)