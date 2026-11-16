# 47. Input 10 product prices; count prices over 1000 and display total cost and average.
total = 0
over_1000 = 0
for product in range(1, 11):
    price = float(input(f"Enter price for product {product}: "))
    total += price
    if price > 1000:
        over_1000 += 1
print("Products costing more than 1000:", over_1000)
print("Total cost:", total)
print("Average price:", total / 10)
