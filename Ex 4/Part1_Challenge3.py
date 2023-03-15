# Exercise 4
# Part 1 Challenge 3
# Author: Paul Takemoto

total = 0

# Finds the sum of three numbers, assigns to global variable total
def add(num1, num2, num3):
    global total
    total = num1 + num2 + num3
    return total

add(3, 4, 5)
print(total)
