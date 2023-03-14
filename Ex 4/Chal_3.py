# Exercise 4 Challenge 3
# Author: Paul Takemoto

total = 0

def add(num1, num2, num3):
    global total
    total = num1 + num2 + num3
    return total

add(3, 4, 5)
print(total)
