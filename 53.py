# 53. Input scores for 15 students; count each score group and calculate the average.
total = 0
high_scores = 0
middle_scores = 0
low_scores = 0
for student in range(1, 16):
    score = float(input(f"Enter score for student {student}: "))
    total += score
    if score >= 90:
        high_scores += 1
    elif score >= 50:
        middle_scores += 1
    else:
        low_scores += 1
print("Scores of 90 or above:", high_scores)
print("Scores from 50 to 89:", middle_scores)
print("Scores below 50:", low_scores)
print("Average score:", total / 15)
