# Exercise 9 Challenge 4
# Paul Takemoto

import class7

def main():
    name = input('Enter the name: ')
    address = input('Enter the address: ')
    phone = input('Enter the phone number: ')
    age = input('Enter your age: ')
    city = input('Enter your city: ')
    state = input('Enter your state: ')
    zipcode = input('Enter your zipcode: ')

    # calling class7, then the name of the class, then name of function which
    # equals to input variable
    v1 = class7.Customer.set_name = name
    v2 = class7.Customer.set_address = address
    v3 = class7.Customer.set_phone = phone

    v4 = class7.Customer.set_age = age
    v5 = class7.Customer.set_city = city
    v6 = class7.Customer.set_state = state
    v7 = class7.Customer.set_zipcode = zipcode

    print('Hello, ' + v1 + ', your address is ' + v2 + ' and your phone # is ' + v3)
    print('Your age is ' + v4 + ' and you live in ' + v5 + ', ' + v6 + ' ' + v7)

main()
