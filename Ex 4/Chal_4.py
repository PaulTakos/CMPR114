# Exercise 4 Challenge 4
# Author: Paul Takemoto

total = 0
average = 0

def add(num1, num2, num3):
    global total
    total = num1 + num2 + num3
    global average
    average = total / 3
    return total


val1 = int(input('Enter 1st number: '))
val2 = int(input('Enter 2nd number: '))
val3 = int(input('Enter 3rd number: '))

add(val1, val2, val3)
print(f'Total : {total}')
print(f'Average: {average: .2f}')
