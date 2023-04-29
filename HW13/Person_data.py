# Person class (Project 2)

class Person:
    def __init__(self, name, address, phone_num):
        self.__name = name
        self.__address = address
        self.__phone_num = phone_num

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone_num(self, phone_num):
        self.__phone_num = phone_num

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone_num(self):
        return self.__phone_num

class Customer(Person):
    def __init__(self, name, address, phone_num, customer_num, on_mail_list):
        super().__init__(name, address, phone_num)
        self.__customer_num = customer_num
        self.__on_mail_list = on_mail_list

    def set_customer_num(self, customer_num):
        self.__customer_num = customer_num

    def set_mail_list_status(self, on_mail_list):
        self.__on_mail_list = on_mail_list

    def get_customer_num(self):
        return self.__customer_num

    def mail_list_status(self):
        if self.__on_mail_list:
            print('You are on the mailing list.')
        else:
            print('You are not on the mailing list.')
