# 28. Ask for a number and print its multiplication table from 1 to 10.
number = int(input("Enter a number: "))
for multiplier in range(1, 11):
    print(number, "x", multiplier, "=", number * multiplier)
