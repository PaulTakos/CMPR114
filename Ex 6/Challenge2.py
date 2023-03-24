# Exercise 6 Challenge 1
# Author: Paul Takemoto

def writenumbers():
    # Opens a file for writing.
    outfile = open('numbers.txt', 'w')

    # Asks user to input 3 numbers.
    num1 = int(input('Enter #1: '))
    num2 = int(input('Enter #2: '))
    num3 = int(input('Enter #3: '))

    # Finds the sum and average of the 3 numbers
    sum = num1 + num2 + num3
    avg = sum/3

    # Writes the 3 numbers, sum, and average to the file
    outfile.write('The 1st number is ' + str(num1) + '\n')
    outfile.write('The 2nd number is ' + str(num2) + '\n')
    outfile.write('The 3rd number is ' + str(num3) + '\n')
    outfile.write('The average number is ' + str(avg) + '\n')
    outfile.write('The total number is ' + str(sum) + '\n')

    outfile.close()  # Closes the file
    print('Data recorded.')

def readnumbers():
    # Opens the file for reading
    outfile = open('numbers.txt', 'r')

    # Reads and prints each line from the file using a while loop
    line = outfile.readline().rstrip()
    while line != '':
        print(line)
        line = outfile.readline().rstrip()

    outfile.close()  # Closes the file

# Calls the above functions
writenumbers()

readnumbers()
