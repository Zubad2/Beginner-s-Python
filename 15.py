#-   Calculate an employee's bonus: salary >= $50,000 earns a 10% bonus; otherwise, 5%.
salary = float(input("Enter your salary: "))
if salary >= 50000:
    d= 0.1
else:
    d= 0.05
bonus= salary*d
print(bonus)