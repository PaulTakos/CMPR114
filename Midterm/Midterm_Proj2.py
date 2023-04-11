# Midterm Project 2
# Paul Takemoto

def main():
    coffee_file = open('Coffee.txt', 'r')

    line = coffee_file.readline()
    while line != '':
        print(line)
        line = coffee_file.readline()

    coffee_file.close()

if __name__ == '__main__':
    main()
