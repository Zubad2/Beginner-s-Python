#-   Input a temperature and print Cold (below 15), Warm (15-30), or Hot (above 30).
temp = float(input("Enter the temperature: "))
print("cold" if temp < 15 else "warm" if temp <= 30 else "hot")