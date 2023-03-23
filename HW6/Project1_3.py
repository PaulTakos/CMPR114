# HW 6 Project 1 Part 3
# Author: Paul Takemoto

def main():
    num_file = open('number_list.txt', 'w')
    for num in range(1, 101):
        num_file.write(str(num) + '\n')

    num_file.close()

main()
