# Exercise 7b Challenge 3
# Paul Takemoto

def main():
    names = ['Howard', 'Jamie', 'Jill']

    print('The list before the insert or remove: ')
    print(names)

    name_remove = input('Enter the name to remove: ')  # Asks user to input a name to remove from list

    names.insert(0, 'Joe')  # Inserts new name at index 0, shifting element 0 to 1
    names.remove(name_remove)  # Removes specified name from list

    print('The names after insert and remove: ')
    print(names)

main()

def total():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sum = 0

    for value in numbers:
        sum += value  # Total of numbers from list
    average = sum / len(numbers)  # Finds the average of the number list
    print('The total is', sum, 'and the average is', average)

    out_file = open('numbers.txt', 'w')  # Opens a file for writing

    # Uses for loop to write each number from list into file
    for value in numbers:
        out_file.write(str(value) + ' ')
    out_file.close()  # Closes file

total()
