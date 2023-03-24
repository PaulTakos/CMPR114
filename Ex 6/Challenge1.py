# Exercise 6 Challenge 1
# Author: Paul Takemoto

def write_info():
    # Asks user to input first name, last name, and age.
    firstname = input('Enter your first name: ')
    lastname = input('Enter your last name: ')
    age = int(input('Enter your age: '))

    # Opens a file and writes input info to the file
    info_file = open('info.txt', 'w')
    info_file.write('First Name: ' + firstname)
    info_file.write('\nLast Name: ' + lastname)
    info_file.write('\nAge: ' + str(age))

    # Closes the file
    info_file.close()
    print('Information written to file \'info.txt\'\n')

def read_info():
    # Opens a file for reading
    info_file = open('info.txt', 'r')

    # Reads and prints each line from the file
    line = info_file.readline().rstrip()
    while line != '':  # Uses a while loop to read and print each line from the file
        print(line)
        line = info_file.readline().rstrip()

    # Closes the file
    info_file.close()

# Calls the above functions
write_info()

read_info()
