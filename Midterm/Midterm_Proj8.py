# Midterm Project 8
# Paul Takemoto

import random

def main():
    name_list = ['Jason', 'John', 'Greg', 'Liam', 'Matt']

    # Outputs names from the list randomly
    for count in range(len(name_list)):
        name = random.choice(name_list)
        print(name)

main()
