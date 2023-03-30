# HW 7a Project 5
# Paul Takemoto

# Global alphabet list
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def main():
    # Asks user to input a string and shift amount.
    my_string = input('Enter a string: ')
    shift = int(input('Enter the amount you would like to shift: '))

    string_cipher = caesar_cipher(my_string, shift)  # Calls the function
    print(string_cipher)

def caesar_cipher(string, amount):
    # Uses nested for loops to compare each character in string to ALPHABET list.
    for char in string:
        for letter in ALPHABET:
            if char.upper() == letter:  # Checks that character is alphabetic letter

                index_new = ALPHABET.index(letter) + amount  # Shifts index by input amount

                # If new index is within list length, sets a new character based on shift in alphabet
                # If new index is beyond list length, subtracts the length to obtain new index (for wrap around)
                if index_new < len(ALPHABET):
                    new_char = ALPHABET[index_new]
                else:
                    index_new = index_new - len(ALPHABET)
                    new_char = ALPHABET[index_new]

                # Replaces character in string with shifted letter
                string = string.replace(char, new_char, 1)

    return string

main()
