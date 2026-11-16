# 51. Input sales for 10 customers; count customers spending over 5000 and display total and average.
total = 0
over_5000 = 0
for customer in range(1, 11):
    sales = float(input(f"Enter sales for customer {customer}: "))
    total += sales
    if sales > 5000:
        over_5000 += 1
print("Customers who spent more than 5000 taka:", over_5000)
print("Total sales:", total)
print("Average sales amount:", total / 10)
