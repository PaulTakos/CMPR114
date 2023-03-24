# Exercise 6 Challenge 8
# Author: Paul Takemoto
import random

def write_num():
    num_file = open('random_numbers.txt', 'a')

    # Generates 3 random numbers between 1-10 for each run, and appends to file.
    for val in range(0, 3):
        num = random.randint(1, 10)
        num_file.write(str(num) + '\n')

    num_file.close()

def read_num():
    num_file = open('random_numbers.txt', 'r')

    # Reads each line from the file and prints them.
    line = num_file.read().rstrip()
    while line != '':
        print(line)
        line = num_file.read().rstrip()

    num_file.close()

write_num()

read_num()
