# 49. Input rainfall for 12 months; count months with 200 mm or more and display total and average.
total = 0
rainy_months = 0
for month in range(1, 13):
    rainfall = float(input(f"Enter rainfall for month {month} in mm: "))
    total += rainfall
    if rainfall >= 200:
        rainy_months += 1
print("Months with rainfall of 200 mm or more:", rainy_months)
print("Total rainfall:", total)
print("Average rainfall:", total / 12)
