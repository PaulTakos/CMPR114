# HW 7a Project 1
# Paul Takemoto

# Global lists of vowel and consonant letters
VOWEL_LIST = ['A', 'E', 'I', 'O', 'U']
CONSONANT_LIST = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
                  'V', 'W', 'X', 'Y', 'Z']

def main():
    my_string = input('Enter a phrase or word: ')  # Asks user to input a string

    # Uses functions to get the number of vowels and of consonants
    num_vowels = get_vowels(my_string.upper())
    num_consonants = get_consonants(my_string.upper())

    print(f'Your string has {num_vowels} vowels and {num_consonants} consonants.')

def get_vowels(string):
    total_vowels = 0  # Initialize total

    # Uses a nested for loop to count the number of vowels
    # by comparing each one to VOWEL_LIST
    for char in string:
        for letter in VOWEL_LIST:
            if char == letter:
                total_vowels += 1  # Increments total vowels by 1 for every vowel found

    return total_vowels


def get_consonants(string):
    total_consonants = 0  # Initialize total

    # Uses a nested for loop to count the number of consonants
    # by comparing each one to CONSONANT_LIST
    for char in string:
        for letter in CONSONANT_LIST:
            if char == letter:
                total_consonants += 1  # Increments total consonants by 1 for every consonant found

    return total_consonants

main()
