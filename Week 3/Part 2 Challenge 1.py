# Exercise 3 Part 2
# Challenge 1
# Name: Paul Takemoto

MAX = 5
total = 0.0

# Explains what the program does
print('This program calculates the sum of')
print(f'{MAX} numbers we will enter.')

# Gets the numbers and accumulates them.
for counter in range(MAX):
    number = int(input('Enter a number: '))
    total = total + number

avg = total / MAX

# Displays the total number.
print(f'The total is {total}.')
print(f'The average is {avg}.')
