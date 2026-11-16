# 48. Input 20 exam scores; count scores 75+ and below 40, and calculate the average.
total = 0
high_scores = 0
low_scores = 0
for student in range(1, 21):
    score = float(input(f"Enter score for student {student}: "))
    total += score
    if score >= 75:
        high_scores += 1
    if score < 40:
        low_scores += 1
print("Scores of 75 or above:", high_scores)
print("Scores below 40:", low_scores)
print("Average score:", total / 20)
