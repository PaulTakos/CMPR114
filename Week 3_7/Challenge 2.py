# Exercise 3.7
# Challenge 2
# Author: Paul Takemoto

days_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
sales_list = []
total_sales = 0.0
count = 0

# Asks user to enter sales for each day
for day in days_list:
    sales = float(input(f'Enter the sales for {day}: '))
    sales_list.insert(count, sales)  # Adds new sales to list
    total_sales += sales  # Adds new sales to total
    count += 1

# Prints sales list and total to console
print('Daily sales values entered: ')
for value in sales_list:
    print(f'${value: .2f}')
print(f'Total sales: ${total_sales: .2f}')

# Writes sales list and total to file
outfile = open('sales.txt', 'w')
for value in sales_list:
    outfile.write(f'${value:.2f}\n')
outfile.write(f'\nTotal sales: ${total_sales: .2f}')
outfile.close()
print('Sales values written to file.')
