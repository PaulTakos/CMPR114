# Exercise 6 Challenge 1
# Author: Paul Takemoto

firstname = input('Enter your first name: ')
lastname = input('Enter your last name: ')
age = int(input('Enter your age: '))

info_file = open('info.txt', 'w')
info_file.write('First Name: ', firstname)
info_file.write('\nLast Name: ', lastname)
info_file.write('\nAge: ', str(age))

info_file.close()
print('\nInformation written to file \'info.txt\'')
