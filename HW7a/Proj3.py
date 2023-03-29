# HW 7a Project 3
# Paul Takemoto

def main():
    # Asks user to input a string w/ no spaces, words starting w/ uppercase letters
    my_string = input('Enter a sentence (no spaces, words begin w/ uppercase): ')

    new_string = separate_sentence(my_string)
    print(new_string)

def separate_sentence(string):
    for char in string:
        if char.isupper():  # Checks for uppercase, then converts to lowercase and adds whitespace
            string = string.replace(char, ' ' + char.lower(), 1)
        # print(string)

    string = string.lstrip()  # Remove leading whitespace
    string = string.replace(string[0], string[0].upper(), 1)  # Capitalize 1st letter in string

    return string

# Calls main function
main()
