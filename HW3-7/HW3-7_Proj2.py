# HW 3-7 Project 2
# Author: Paul Takemoto

# Initializes total, list of numbers, min, and max
total = 0.0
num_list = []
min_num = 0.0
max_num = 0.0

for num in range(20):
    # Prompts user to enter 20 numbers, then adds each one to list
    val = float(input('Enter a number: '))
    num_list.append(val)
    # On the first entry, assigns min and max to first number
    if num == 0:
        min_num = val
        max_num = val
    # After 1st entry, compares input value to min and max
    # and sets min and max appropriately
    elif num > 0:
        if val < min_num:
            min_num = val

        if val > max_num:
            max_num = val
    # adds input value to total
    total += val

average = total / 20

# Prints out results
print(f'Numbers entered: {num_list}')
print(f'Lowest number: {min_num}')
print(f'Highest number: {max_num}')
print(f'Total: {total}')
print(f'Average: {average}')
