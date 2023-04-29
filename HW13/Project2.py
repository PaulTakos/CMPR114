# HW 13 Project 2
# Paul Takemoto

import Person_data

def main():
    name = input('Enter your name: ')
    address = input('Enter your address: ')
    phone_num = input('Enter your phone number: ')
    customer_num = int(input('Enter your customer number: '))

    new_customer = Person_data.Customer(name, address, phone_num, customer_num, True)
    answer = input('Type \'Y\' if you\'re on the mailing list, type anything else if not: ')
    if answer != 'Y' and answer != 'y':
        new_customer.set_mail_list_status(False)

    print()
    print('Customer name: ', new_customer.get_name())
    print('Customer address: ', new_customer.get_address())
    print('Customer phone number: ', new_customer.get_phone_num())
    print('Customer number: ', new_customer.get_customer_num())
    new_customer.mail_list_status()

main()
