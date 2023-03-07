# Quiz 1 Project 2
# Author: Paul Takemoto

score1 = float(input('Enter score 1: '))
score2 = float(input('Enter score 2: '))
score3 = float(input('Enter score 3: '))
score4 = float(input('Enter score 4: '))

score_total = score1 + score2 + score3 + score4
score_avg = score_total / 4

print(f'Total score: {score_total: .2f}')
print(f'Average score: {score_avg: .2f}')