# Exercise 4 Challenge 5
# Author: Paul Takemoto

def main():
    hours_worked = float(input('Enter number of hours worked: '))
    hourly_pay = float(input('Enter hourly pay: '))
    total = get_total_pay(hours_worked, hourly_pay)
    print(f'Your total pay is ${total: .2f}')

def get_total_pay(time, pay):
    total_pay = time * pay
    return total_pay

main()
