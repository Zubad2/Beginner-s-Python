# 25. Ask the user for a positive number and print all numbers from that number down to 1.
number = int(input("Enter a positive number: "))
for value in range(number, 0, -1):
    print(value)
