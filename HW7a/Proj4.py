# HW 7a Project 4
# Paul Takemoto

def main():
    my_string = input('Enter a sentence: ')  # Asks user to input a string.

    new_string = pig_latin(my_string)
    print(new_string)

def pig_latin(string):
    tokens = string.split(' ')
    string_piglatin = ''  # Initialize a new string to return
    new_tokens = []  # Initialize a new list to hold new substrings

    # Uses a for loop to go through each token and convert them to Pig Latin
    for item in tokens:
        first = item[0]  # Retrieves the first character of token
        item = item[1:] + first + 'ay'  # Moves 1st character to end of token and concatenates w/ 'ay'
        item = item.upper()
        new_tokens.append(item)  # Adds new substrings to new list

    # Uses a for loop to create new string of the words in Pig Latin
    for item in new_tokens:
        string_piglatin = string_piglatin + item + ' '

    return string_piglatin

main()
