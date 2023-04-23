# RetailItem class (Project  3)

class RetailItem:
    def __init__(self, description, quantity, price):
        self.__description = description
        self.__quantity = quantity
        self.__price = price

    def get_description(self):
        return self.__description

    def get_quantity(self):
        return self.__quantity

    def get_price(self):
        return self.__price
