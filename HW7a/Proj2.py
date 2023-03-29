# HW 7a Project 2
# Paul Takemoto

def main():
    my_string = input('Enter a string: ')  # Asks user to input a string
    max_total = 0

    my_string_upper = my_string.upper()  # Converts all letters in string to uppercase
    max_char = ''
    # Uses a for loop to count occurrences of each character, and sets the maximum occurrence
    # if it is greater than the current maximum.
    for char1 in my_string_upper:
        if char1 != ' ':
            current_total = 0
            for char2 in my_string_upper:
                if char2 == char1:
                    current_total += 1

            if current_total >= max_total:
                max_total = current_total
                max_char = char1

    print('Most frequent: ', max_char)
    print(f'Frequency: {max_total} times')

# Calls main function
main()
