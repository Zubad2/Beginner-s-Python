#-   Ask for a student's mark and display the grade: 80 or above, A; 70-79, B; 60-69, C; below 60, F.
marks = int(input("Enter your marks: "))
if marks >= 80:
    print("You have scored A grade.")
elif marks >= 70:
    print("You have scored B grade.")
elif marks >= 60:
    print("You have scored C grade.")
else:
    print("You have scored F grade.")
    