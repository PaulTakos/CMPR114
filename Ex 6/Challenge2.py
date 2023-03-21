# Exercise 6 Challenge 1
# Author: Paul Takemoto

def writenumbers():
    outfile = open('numbers.txt', 'w')

    num1 = int(input('Enter #1: '))
    num2 = int(input('Enter #2: '))
    num3 = int(input('Enter #3: '))

    sum = num1 + num2 + num3
    avg = sum/3

    outfile.write('The 1st number is ' + str(num1) + '\n')
    outfile.write('The 2nd number is ' + str(num2) + '\n')
    outfile.write('The 3rd number is ' + str(num3) + '\n')
    outfile.write('The average number is ' + str(avg) + '\n')
    outfile.write('The total number is ' + str(sum) + '\n')

    outfile.close()
    print('Data recorded.')

def readnumbers():
    outfile = open('numbers.txt', 'r')
    line = outfile.readline().rstrip()
    while line != '':
        print(line)
        line = outfile.readline().rstrip()
    outfile.close()

writenumbers()

readnumbers()
