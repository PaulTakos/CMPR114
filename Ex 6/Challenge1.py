# Exercise 6 Challenge 1
# Author: Paul Takemoto

firstname = input('Enter your first name: ')
lastname = input('Enter your last name: ')
age = int(input('Enter your age: '))

info_file = open('info.txt', 'w')
info_file.write(firstname)
info_file.write('\n' + lastname)
info_file.write('\n' + str(age))

info_file.close()
print('\nInformation written to file \'info.txt\'')
