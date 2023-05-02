# Quiz 2 Problem 51
# Paul Takemoto

# Employee class
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

# ProductionWorker class, a subclass of Employee
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

# main function
def main():
    worker1 = ProductionWorker('Rain Princeton', 1234, 1, 14.50)
    worker2 = ProductionWorker('Paul Takemoto', 4321, 1, 17.45)
    worker3 = ProductionWorker('Jane Doe', 1450, 2, 20.70)

    employee_list = [worker1, worker2, worker3]  # List of ProductionWorker objects

    for worker in employee_list:
        print('Employee name:', worker.get_name())
        print('Employee number:', worker.get_number())
        print('Employee shift:', worker.get_shift_num())
        print(f'Employee hourly pay: ${worker.get_hourly_pay(): .2f}')
        print()

main()
