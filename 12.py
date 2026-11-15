#-   Classify a person as Child, Teenager, Adult, or Senior based on age.
age = int(input("Enter your age: "))
if age < 13:
    print("You are a Child.")
elif 13 <= age < 20:
    print("You are a Teenager.")
elif 20 <= age < 60:
    print("You are an Adult.")
else:
    print("You are a Senior.")
