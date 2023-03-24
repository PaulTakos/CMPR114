# HW 6 Project 1 Part 2
# Author: Paul Takemoto

def main():
    output_file = open('things.txt', 'r')  # Opens a file for reading

    # Uses a while loop to read and print each line from file
    line = output_file.readline().rstrip()
    while line != '':  # Ensures that file is read until blank is encountered
        print(line)
        line = output_file.readline().rstrip()

    output_file.close()

main()
