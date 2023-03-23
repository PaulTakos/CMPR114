# HW 6 Project 1 Part 1
# Author: Paul Takemoto

def main():
    output_file = open('things.txt', 'w')
    output_file.write('Red fox' + '\n')
    output_file.write('Durian' + '\n')
    output_file.write('Morocco' + '\n')

    output_file.close()

main()
