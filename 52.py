# 52. Input ages of 20 people; count adults and minors and calculate the average age.
total = 0
adults = 0
under_18 = 0
for person in range(1, 21):
    age = int(input(f"Enter age for person {person}: "))
    total += age
    if age >= 18:
        adults += 1
    else:
        under_18 += 1
print("People aged 18 or older:", adults)
print("People under 18:", under_18)
print("Average age:", total / 20)
