# HW 6 Project 1 Part 2
# Author: Paul Takemoto

def main():
    output_file = open('things.txt', 'r')
    line = output_file.readline().rstrip()
    while line != '':
        print(line)
        line = output_file.readline().rstrip()

    output_file.close()

main()
