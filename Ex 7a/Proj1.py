# Exercise 7a Project 1a
# Author: Paul Takemoto

def main():

    user_string = input('Enter a string: ')

    print('This is what I found about that string: ')

    # Test the string
    if user_string.isalnum():
        print('The string is alphanumeric.')
    if user_string.isdigit():
        print('The string contains only digits.')
    if user_string.isalpha():
        print('The string contains only alphabetic characters.')
    if user_string.isspace():
        print('The string contains only whitespace characters.')
    if user_string.islower():
        print('The letters in the string are all lowercase.')
    if user_string.isupper():
        print('The letters in the string are all uppercase.')

if __name__ == '__main__':
    main()
