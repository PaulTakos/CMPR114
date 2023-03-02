# HW3 Project 3
# Author: Paul Takemoto

# Initialize sum
pos_sum = 0.0

# Asks user to input a number
y = float(input('Enter a positive number to add to series (negative will quit program): '))
# Adds number to sum if it's positive
while y >= 0:
    pos_sum += y
    y = float(input('Enter another positive number (negative will quit program): '))

# Prints out the sum
print(f'Your sum: {pos_sum: .2f}')
