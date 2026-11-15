#-   Check whether a number is divisible by both 3 and 5.
no= int(input("Enter a number: "))
if no % 3 == 0 and no % 5 == 0:
    print(no, "is divisible by both 3 and 5.")
else:
    print("Not divisible by either 3 or 5")