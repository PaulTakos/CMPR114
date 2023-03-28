
def main():
    # Variable to hold the count - starts at 0
    count = 0

    # Gets string from the user
    my_string = input('Enter a sentence: ')

    # Count the Ts
    for ch in my_string:
        if ch == 'T' or ch == 't':
            count += 1

    # Print the result
    print(f'The letter T appears {count} times.')

if __name__ == '__main__':
    main()
