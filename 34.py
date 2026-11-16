# 34. Calculate the sum of all odd numbers between 1 and 20.
total = 0
for number in range(1, 21, 2):
    total += number
print("Sum of odd numbers:", total)
