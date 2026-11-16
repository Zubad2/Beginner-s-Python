# 43. Input the marks of 20 students and calculate the total and average marks.
total = 0
for student in range(1, 21):
    mark = float(input(f"Enter marks for student {student}: "))
    total += mark
average = total / 20
print("Total marks:", total)
print("Average mark:", average)
