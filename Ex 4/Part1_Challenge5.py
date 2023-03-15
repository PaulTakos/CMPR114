# Exercise 4
# Part 1 Challenge 5
# Author: Paul Takemoto

def main():
    # Asks user for hours and hourly pay before getting the total pay and printing the results
    hours_worked = float(input('Enter number of hours worked: '))
    hourly_pay = float(input('Enter hourly pay: '))
    total = get_total_pay(hours_worked, hourly_pay)
    print(f'Your total pay is ${total: .2f}')

# Finds the total pay from the hours and hourly rate
def get_total_pay(time, pay):
    total_pay = time * pay
    return total_pay

# Calls main function
main()
