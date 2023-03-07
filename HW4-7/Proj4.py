# HW 4-7 Project 4
# Author: Paul Takemoto

input_tup = ([2, 20], [44, 1], [3, 13])

sorted_tup = tuple(sorted(input_tup, key=sum))

print(sorted_tup)
