# Ex 10 Challenge 1
# Paul Takemoto

class AnimalType:
    def eats(self):
        print('This animal likes to eat...')

class Rabbits(AnimalType):
    def munch(self):
        print('...carrots.')

class Birds(Rabbits):
    def munch1(self):
        print('...seeds.')

class Reptiles(Birds):
    def munch2(self):
        print('...crickets.')

RabbitObject = Rabbits()
RabbitObject.eats()
RabbitObject.munch()

# Bird object inherits from 2 different classes
BirdObject = AnimalType()
BirdObject = Birds()
BirdObject.eats()
BirdObject.munch1()

ReptileObject = Reptiles()
ReptileObject.eats()
ReptileObject.munch2()
