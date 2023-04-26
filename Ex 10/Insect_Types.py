# Insect classes (Project 5)

class Insect:
    def __init__(self, name, color, wings):
        self.name = name
        self.color = color
        self.wings = wings

    def set_name(self, name):
        self.name = name

    def set_color(self, color):
        self.color = color

    def set_wings(self, wings):
        self.wings = wings

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color

    def get_wings(self):
        return self.wings

class Bumblebee(Insect):
    def __init__(self, name, color, wings, can_sting):
        super().__init__(name, color, wings)
        self.can_sting = can_sting

    def sting(self):
        if self.can_sting:
            print(f'This {self.name} has an uncomfortable sting.')
        else:
            print('Something is wrong with its stinger...')

class Grasshopper(Insect):
    def __init__(self, name, color, wings, can_jump):
        super().__init__(name, color, wings)
        self.can_jump = can_jump

    def jump(self):
        if self.can_jump:
            print(f'This {self.name} jumps without the need for wings.')
        else:
            print('It can\'t jump...')
