# HW 4-7 Project 1
# Author: Paul Takemoto

test_tup = (15, 20, 123, 47, 26, 81)
num = 0
total = 0

# Adds each value in tuple to total using a while loop
while num < len(test_tup):
    total += test_tup[num]
    num += 1

print('The sum of this tuple is', total)
