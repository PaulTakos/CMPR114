# Exercise 4 Challenge 1
# Author: Paul Takemoto

def main():
    # Asks user for number of birds in Texas and California.
    birds_tx = int(input('Enter number of birds in Texas: '))
    birds_ca = int(input('Enter number of birds in California: '))
    texas(birds_tx)
    california(birds_ca)

def texas(num_birds):
    birds = num_birds
    print(f'Texas has {birds} birds.')

def california(num_birds):
    birds = num_birds
    print(f'California has {birds} birds.')

# main function
main()
