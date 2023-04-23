# HW11 Project 1
# Paul Takemoto

import Pets

def main():
    my_pet = Pets.Pet  # Creates a pet object

    # Prompts user to input pet info
    name = input('Enter your pet\'s name: ')
    animal_type = input('Enter your pet\'s animal type: ')
    age = int(input('Enter your pet\'s age: '))

    # Assigns internal object attributes to variables
    v1 = my_pet.set_name = name
    v2 = my_pet.set_animal_type = animal_type
    v3 = my_pet.set_age = age

    print('Your pet, ' + v1 + ', is a ' + str(v3) + ' year old ' + v2)

if __name__ == '__main__':
    main()
