# HW 4-7 Project 2
# Author: Paul Takemoto

test_tup = ([17, 28], [93, 11], [20, 17])
total = 0

# Processes each list in tuple and adds to the total
for r in range(len(test_tup)):  # Each element in tuple is a row
    for c in range(len(test_tup[r])):  # Each element in list is a column
        total += test_tup[r][c]

print('The sum of this tuple is', total)
