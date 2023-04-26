# Ex 10 Challenge 5
# Paul Takemoto

import Insect_Types

def main():
    bee = Insect_Types.Bumblebee('Bumblebee', 'Yellow', 4, True)

    hopper = Insect_Types.Grasshopper('Grasshopper', 'Green', 4, True)

    print('Insect 1 Type: ', bee.get_name())
    print('Insect 1 Color: ', bee.get_color())
    print('Insect 1 # Wings: ', bee.get_wings())
    bee.sting()

    print()

    print('Insect 2 Type: ', hopper.get_name())
    print('Insect 2 Color: ', hopper.get_color())
    print('Insect 2 # Wings: ', hopper.get_wings())
    hopper.jump()

main()
