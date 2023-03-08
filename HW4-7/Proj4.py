# HW 4-7 Project 4
# Author: Paul Takemoto

input_tup = ([2, 20], [44, 1], [3, 13])

# Sorts the tuple as a list based on sums, then casts to tuple.
sorted_tup = tuple(sorted(input_tup, key=sum))

print(sorted_tup)
