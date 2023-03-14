# Exercise 4 Challenge 1
# Author: Paul Takemoto

def main():
    texas()
    california()

def texas():
    # Asks user for number of birds in Texas.
    birds = int(input('Enter number of birds in Texas: '))
    print(f'Texas has {birds} birds.')

def california():
    # Asks user for number of birds in California.
    birds = int(input('Enter number of birds in California: '))
    print(f'California has {birds} birds.')

# Calls main function
main()
