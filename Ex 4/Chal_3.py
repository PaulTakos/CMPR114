# Exercise 4 Challenge 3
# Author: Paul Takemoto

# Global variable
number = 0

def main():
    global number
    number = int(input('Enter a number: '))
    show_number()

def show_number():
    print(f'The number you entered is {number}.')

main()

def add(num1, num2):
    total = num1 + num2
    print(total)


add(3, 4)
