# Bank class (Project 5)

class BankAccount:
    def __init__(self, bal):  # self is used to represent instance of class, used to access class variables
        self.__balance = bal

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Error: Insufficient funds.')

    def get_balance(self):
        return self.__balance
