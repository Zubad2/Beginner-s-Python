# 46. Input marks for 15 students; display the number who passed (40+) and the average.
total = 0
passed = 0
for student in range(1, 16):
    mark = float(input(f"Enter marks for student {student}: "))
    total += mark
    if mark >= 40:
        passed += 1
print("Students passed:", passed)
print("Average mark:", total / 15)
