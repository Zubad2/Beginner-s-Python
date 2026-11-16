# 45. Input the distance travelled each day for 5 days; calculate the total and average.
total_distance = 0
for day in range(1, 6):
    distance = float(input(f"Enter distance for day {day}: "))
    total_distance += distance
average_distance = total_distance / 5
print("Total distance:", total_distance)
print("Average distance per day:", average_distance)
