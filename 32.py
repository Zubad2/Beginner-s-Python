# 32. Ask for a positive integer N and calculate the product of all numbers from 1 to N.
n = int(input("Enter a positive integer: "))
product = 1
for number in range(1, n + 1):
    product *= number
print("Product:", product)
