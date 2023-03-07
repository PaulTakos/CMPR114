# Quiz 1 Project 5
# Author: Paul Takemoto

sales = float(input('Enter the sales: '))

# Assigns commission value depending on what range the sales input is in.
if sales >= 50000 and sales < 70000:
    salary = 70000.00
    commission = 10
elif sales >= 70000 and sales < 90000:
    salary = 80000.00
    commission = 20
elif sales >= 90000 and sales < 100000:
    salary = 90000.00
    commission = 30
else:
    salary = 0.00
    commission = 0.0

# Calculates final salary by adding the corresponding commission rate
salary_comm = salary * float(commission / 100)
salary_total = salary + salary_comm

print(f'\nSalary group: ${salary: ,.2f}')
print('Commission: ', commission, '%')
print(f'Final salary: ${salary_total: ,.2f}')
