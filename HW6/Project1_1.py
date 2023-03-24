# HW 6 Project 1 Part 1
# Author: Paul Takemoto

def main():
    output_file = open('things.txt', 'w')  # Opens a file for writing

    # Writes an animal, a fruit, and a country to file
    output_file.write('Red fox' + '\n')
    output_file.write('Durian' + '\n')
    output_file.write('Morocco' + '\n')

    output_file.close()

main()
