# Exercise 3.7
# Challenge 1
# Author: Paul Takemoto

def total():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sum = 0

    for value in numbers:
        sum += value  # total the numbers in the list

    average = sum / len(numbers)  # the len function returns number of items in list

    print('The total is ', sum)
    print('The average is ', average)

    # writes the list of numbers to a file
    outfile = open('numbers.txt', 'w')
    outfile.write(str(numbers))
    outfile.close()
    print('Numbers written to file.')

total()