# Exercise 4
# Part 1 Challenge 4
# Author: Paul Takemoto

total = 0
average = 0

# Finds the sum and average of three numbers. Results are assigned to global variables.
def add(num1, num2, num3):
    global total
    total = num1 + num2 + num3
    global average
    average = total / 3
    return total

# Asks user to input three numbers
val1 = int(input('Enter 1st number: '))
val2 = int(input('Enter 2nd number: '))
val3 = int(input('Enter 3rd number: '))

# Calls add function to find the sum and average of the input numbers
add(val1, val2, val3)
print(f'Total : {total}')
print(f'Average: {average: .2f}')
