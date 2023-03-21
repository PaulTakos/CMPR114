# Exercise 6 Challenge 1
# Author: Paul Takemoto

def write_info():
    firstname = input('Enter your first name: ')
    lastname = input('Enter your last name: ')
    age = int(input('Enter your age: '))

    info_file = open('info.txt', 'w')
    info_file.write('First Name: ' + firstname)
    info_file.write('\nLast Name: ' + lastname)
    info_file.write('\nAge: ' + str(age))

    info_file.close()
    print('Information written to file \'info.txt\'\n')

def read_info():
    info_file = open('info.txt', 'r')
    line = info_file.readline().rstrip()
    while line != '':
        print(line)
        line = info_file.readline().rstrip()
    info_file.close()

write_info()

read_info()
