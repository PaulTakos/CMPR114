# Exercise 3 Part 2
# Challenge 3
# Author: Paul Takemoto
bugs_total = 0

# Asks user for number of bugs collected in each of 5 days, then adds to the total
for day in range(5):
    bugs = int(input('Enter the number of bugs collected this day: '))
    bugs_total += bugs

print('You collected a total of', bugs_total, 'bugs.')
