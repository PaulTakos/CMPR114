# Employee class (Project 7)

class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

class ProductionWorker(Employee):
    def __init__(self, name, number, shift_num, hourly_pay):
        super().__init__(name, number)
        self.__shift_num = shift_num
        self.__hourly_pay = hourly_pay

    def set_shift_num(self, shift_num):  # shift 1 = day, shift 2 = night
        self.__shift_num = shift_num

    def set_hourly_pay(self, hourly_pay):
        self.__hourly_pay = hourly_pay

    def get_shift_num(self):
        return self.__shift_num

    def get_hourly_pay(self):
        return self.__hourly_pay
