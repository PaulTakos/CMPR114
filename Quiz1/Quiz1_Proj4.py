# Quiz 1 Project 4
# Author: Paul Takemoto

sales = float(input('Enter the sales: '))

# Assigns commission value depending on what range the sales input is in.
if sales >= 50000 and sales < 70000:
    commission = 10
elif sales >= 70000 and sales < 90000:
    commission = 20
elif sales >= 90000 and sales < 100000:
    commission = 30
else:
    commission = 0

print('Commission: ', commission, '%')
