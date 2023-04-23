# HW11 Project 3
# Paul Takemoto

import Retail_data

def main():
    # Creates 3 RetailItem objects with info filled in
    item1 = Retail_data.RetailItem('Jacket', 12, 59.95)
    item2 = Retail_data.RetailItem('Designer jeans', 40, 34.95)
    item3 = Retail_data.RetailItem('Shirt', 20, 24.95)

    print('Item 1: ' + item1.get_description() + ', $' + str(item1.get_price()))
    print('Quantity: ' + str(item1.get_quantity()) + '\n')

    print('Item 2: ' + item2.get_description() + ', $' + str(item2.get_price()))
    print('Quantity: ' + str(item2.get_quantity()) + '\n')

    print('Item 3: ' + item3.get_description() + ', $' + str(item3.get_price()))
    print('Quantity: ' + str(item3.get_quantity()) + '\n')

main()
