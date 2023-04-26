# Vehicles 2 class (Project 6)

class Automobiles:
    # The _ _init_ _method accepts arguments for the
    # make, model, mileage, and price. It initializes
    # the data attributes with these values.
    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price

    # Mutator methods
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_price(self, price):
        self.__price = price

    # Accessor methods
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price

class Truck(Automobiles):
    def __init__(self, make, model, mileage, price):
        super().__init__(make, model, mileage, price)

class SUV(Automobiles):
    def __init__(self, make, model, mileage, price):
        super().__init__(make, model, mileage, price)

class EV(Automobiles):
    def __init__(self, make, model, mileage, price):
        super().__init__(make, model, mileage, price)
