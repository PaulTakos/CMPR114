# Exercise 4
# Part 1 Challenge 2
# Author: Paul Takemoto

def main():
    print('Collecting information')
    get_info()

# Asks user to input name, address, city, state, and zipcode, then prints them.
def get_info():
    firstname = input('Enter your first name: ')
    lastname = input('Enter your last name: ')
    address = input('Enter your street address: ')
    city = input('Enter your city of residence: ')
    state = input('Enter your state of residence: ')
    zipcode = input('Enter your zipcode: ')

    print()
    print('Last name: ', lastname)
    print('First name: ', firstname)
    print(address)
    print(city, ',', state, zipcode)

# Calls main function
main()
