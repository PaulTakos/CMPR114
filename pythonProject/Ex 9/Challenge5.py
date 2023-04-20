# Exercise 9 Challenge 5
# Paul Takemoto

import Bank

def main():
    start_bal = float(input('Enter starting balance: '))

    # Calls external BankAccount class from Bank
    savings = Bank.BankAccount(start_bal)

    pay = float(input('How much were you paid this week? '))
    print('This amount will be deposited into your account.')

    # Deposit function w/ amount argument, fill that w/ pay value
    savings.deposit(pay)

    print('Your account balance is $', format(savings.get_balance(), '.2f'))

    cash = float(input('How much would you like to withdraw? '))
    print('This amount will be withdrawn from your account.')

    # Withdraw function w/ amount argument, fill that w/ cash value
    savings.withdraw(cash)

    print('Your account balance is $', format(savings.get_balance(), '.2f'))

main()
