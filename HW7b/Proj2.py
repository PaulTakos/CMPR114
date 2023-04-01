
import pickle

def main():
    vegetables = {}  # Empty dictionary
    selection = 0

    end_of_file = False
    veg_file1 = open('vegetables.dat', 'rb')

    # Reads file to the end
    while not end_of_file:
        try:
            # Unpickles the file
            vegetables = pickle.load(veg_file1)
        except EOFError:
            # Sets flag to indicate end of file
            end_of_file = True

    veg_file1.close()

    while selection != 5:
        selection = get_menu_choice()

        # Processes user's choice
        if selection == 1:
            show_list(vegetables)
        elif selection == 2:
            add(vegetables)
        elif selection == 3:
            change(vegetables)
        elif selection == 4:
            delete(vegetables)

    # Pickles the vegetable dictionary into a file
    veg_file2 = open('vegetables.dat', 'wb')
    pickle.dump(vegetables, veg_file2)
    veg_file2.close()

def get_menu_choice():
    print('Vegetables and Their Prices')
    print('1. Show vegetable list')
    print('2. Add new vegetable')
    print('3. Change the price of existing vegetable')
    print('4. Delete an existing vegetable')
    print('5. Quit the program')
    selection = int(input('Enter your choice: '))
    while selection < 1 or selection > 5:
        print('Selection must be a number between 1-5')
        selection = int(input('Enter a valid choice: '))
    return selection

def show_list(vegetables):
    print('\nVegetables and Their Prices')
    for key, value in vegetables.items():
        print(key + '  $' + value)
    print()

def add(vegetables):
    name = input('Enter a vegetable: ')
    price = float(input('Enter its price: '))

    # If vegetable doesn't exist, add it
    if name not in vegetables:
        vegetables[name] = str(price)
    else:
        print('That entry already exists.')
    print()

def change(vegetables):
    name = input('Enter a vegetable: ')

    if name in vegetables:
        # Get a new price
        price = float(input('Enter a new price: '))

        # Updates entry
        vegetables[name] = str(price)
    else:
        print('That vegetable is not found.')
    print()

def delete(vegetables):
    name = input('Enter a vegetable: ')

    if name in vegetables:
        del vegetables[name]
    else:
        print('That vegetable is not found.')
    print()

main()
