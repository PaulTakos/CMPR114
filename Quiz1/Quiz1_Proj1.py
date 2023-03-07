# Quiz 1 Project 1
# Author: Paul Takemoto

salary_gross = float(input('Enter the gross salary: '))

# Calculates total by adding 10% to gross input.
salary_total = salary_gross + (salary_gross * 0.1)

print(f'The total is ${salary_total: ,.2f}')
