# 39. Calculate 10 + 20 + 30 + ... + 100.
total = 0
for number in range(10, 101, 10):
    total += number
print("Sum:", total)
