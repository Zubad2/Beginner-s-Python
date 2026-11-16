# 31. Ask for a number and print its first 10 multiples.
number = int(input("Enter a number: "))
for multiplier in range(1, 11):
    print(number * multiplier)
