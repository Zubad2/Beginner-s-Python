# 30. Ask for a number and calculate the sum of all even numbers from 1 up to it.
limit = int(input("Enter a number: "))
total = 0
for number in range(2, limit + 1, 2):
    total += number
print("Sum of even numbers:", total)
