# HW 7b Project 2
# Paul Takemoto

import pickle

def main():
    vegetables = {}  # Creates an empty dictionary
    selection = 0

    end_of_file = False
    veg_file1 = open('vegetables.dat', 'rb')  # Opens a .dat file for binary reading

    # Reads file to the end
    while not end_of_file:
        try:
            # Unpickles the file
            vegetables = pickle.load(veg_file1)
        except EOFError:
            # Sets flag to indicate end of file
            end_of_file = True

    veg_file1.close()  # Closes file

    while selection != 5:  # As long as user doesn't quit program (option 5)
        selection = get_menu_choice()  # Gets user's selection via function

        # Processes user's choice based on selection (calls appropriate function)
        if selection == 1:
            show_list(vegetables)
        elif selection == 2:
            add(vegetables)
        elif selection == 3:
            change(vegetables)
        elif selection == 4:
            delete(vegetables)

    # Pickles the vegetable dictionary into a file
    veg_file2 = open('vegetables.dat', 'wb')  # Opens a .dat file for binary writing
    pickle.dump(vegetables, veg_file2)
    veg_file2.close()

def get_menu_choice():
    # Prints menu with choices, and prompts user for input
    print('Vegetables and Their Prices')
    print('1. Show vegetable list')
    print('2. Add new vegetable')
    print('3. Change the price of existing vegetable')
    print('4. Delete an existing vegetable')
    print('5. Quit the program')
    selection = int(input('Enter your choice: '))

    while selection < 1 or selection > 5:  # Ensures selection is valid
        print('Selection must be a number between 1-5')
        selection = int(input('Enter a valid choice: '))
    return selection

def show_list(vegetables):
    # Displays dictionary contents (key and value)
    print('\nVegetables and Their Prices')
    for key, value in vegetables.items():
        print(key + '  $' + value)
    print()

def add(vegetables):
    # Asks user to enter new vegetable and price to add
    name = input('Enter a vegetable: ')
    price = float(input('Enter its price: '))

    # If vegetable doesn't exist, add it
    if name not in vegetables:
        vegetables[name] = str(price)
    else:
        print('That entry already exists.')
    print()

def change(vegetables):
    # Asks user to enter a vegetable to change its price
    name = input('Enter a vegetable: ')

    if name in vegetables:  # Checks to ensure vegetable is in dictionary
        # Get a new price
        price = float(input('Enter a new price: '))

        # Updates entry
        vegetables[name] = str(price)
    else:
        print('That vegetable is not found.')
    print()

def delete(vegetables):
    # Asks user to enter a vegetable to delete
    name = input('Enter a vegetable: ')

    # Ensures vegetable is in dictionary, then deletes it
    if name in vegetables:
        del vegetables[name]
    else:
        print('That vegetable is not found.')
    print()

# Calls main function
main()
