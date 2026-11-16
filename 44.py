# 44. Input 5 employee salaries, add a 10% bonus to each, and display the total paid.
total_paid = 0
for employee in range(1, 6):
    salary = float(input(f"Enter salary for employee {employee}: "))
    total_paid += salary * 1.10
print("Total salary paid including bonuses:", total_paid)
