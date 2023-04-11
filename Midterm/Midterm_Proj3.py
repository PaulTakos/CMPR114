# Midterm Project 3
# Paul Takemoto

def main():
    coffee_file = open('Coffee.txt', 'a')

    print('Enter your favorite coffee brand to add.')
    new_coffee = input('Its product number will be 99-8888, its price will be $9.88: ')

    coffee_file.write('\n' + new_coffee + ',' + '99-8888' + ',' + '9.88')

if __name__ == '__main__':
    main()
