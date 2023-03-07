# Quiz 1 Project 6
# Author: Paul Takemoto

# Asks user to input 4 scores, then calculates total and average
score1 = float(input('Enter score 1: '))
score2 = float(input('Enter score 2: '))
score3 = float(input('Enter score 3: '))
score4 = float(input('Enter score 4: '))
score_total = score1 + score2 + score3 + score4

score_avg = score_total / 4

# Checks that average is 100 or less, otherwise asks user to re-enter scores
while score_avg > 100:
    print('Average is too high!')
    score1 = float(input('Re-enter score 1: '))
    score2 = float(input('Re-enter score 2: '))
    score3 = float(input('Re-enter score 3: '))
    score4 = float(input('Re-enter score 4: '))
    score_total = score1 + score2 + score3 + score4
    score_avg = score_total / 4

# Assigns letter grade to average
if score_avg >= 90 and score_avg <= 100:
    print('Letter grade: A')
elif score_avg >= 80 and score_avg <= 89:
    print('Letter grade: B')
elif score_avg >= 70 and score_avg <= 79:
    print('Letter grade: C')
elif score_avg >= 60 and score_avg <= 69:
    print('Letter grade: D')
else:
    print('Letter grade: F')

print(f'Average: {score_avg: .2f}')
