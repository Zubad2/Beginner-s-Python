#-   Input two numbers and display their sum, average, difference, product, and quotient.
A= int(input("Enter the first number: "))
B= int(input("Enter the second number: "))
print("Sum:", A + B)
print("Average:", (A + B) / 2)
print("Difference:", A - B)
print("Product:", A * B)
if B != 0:
    print("Quotient:", A / B)
else:
    print("Cannot divide by zero.")
