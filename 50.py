# 50. Input 20 integers; count even and odd numbers and calculate the sum of even numbers.
even_count = 0
odd_count = 0
even_sum = 0
for i in range(1, 21):
    number = int(input(f"Enter integer {i}: "))
    if number % 2 == 0:
        even_count += 1
        even_sum += number
    else:
        odd_count += 1
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
print("Sum of even numbers:", even_sum)
