# Midterm Project 2
# Paul Takemoto

def main():
    coffee_file = open('Coffee.txt', 'r')  # Opens file for reading

    # Uses a while loop
    line = coffee_file.readline().rstrip()
    while line != '':
        print(line)
        line = coffee_file.readline().rstrip()

    coffee_file.close()

if __name__ == '__main__':
    main()
