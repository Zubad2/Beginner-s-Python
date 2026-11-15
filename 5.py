#-   Check if a number is positive, negative, or zero.
no = int(input("Enter a number: "))
if no > 0:
    print(no, "is a positive number.")
elif no < 0:
    print(no, "is a negative number.")
else:
    print("The number is zero.")
