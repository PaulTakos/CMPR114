# Exercise 6 Challenge 3
# Author: Paul Takemoto

def sales():
    total_sales = 0.0

    num_days = int(input('Enter # of days of sales: '))  # Asks user to input number of days of sales
    sales_file = open('sales.txt', 'w')  # Opens a file for reading

    # Uses a for loop to ask user to input sales for each day, accumulates total,
    # and writes each value to file
    for count in range(1, num_days + 1):
        sale = float(input('Enter the sales for day #' + str(count) + ': '))
        total_sales += sale
        sales_file.write(str(sale) + '\n')  # Writes value to file

    # Asks user for salary
    salary = float(input('Enter your salary: '))

    # Adds 10% commission to salary if total sales is above 1000
    if total_sales > 1000:
        salary = salary * 1.1
    sales_file.write(str(salary) + '\n')  # Writes salary to file

    sales_file.close()  # Closes the file
    print('Sales and salary recorded.')

sales()

def read_sales():
    sales_file = open('sales.txt', 'r')  # Opens file for reading

    # Reads and prints each line from the file using a while loop
    line = sales_file.readline()
    while line != '':
        amount = float(line)  # Casts to float before printing
        print(f'{amount: .2f}')
        line = sales_file.readline()

    # Closes the file
    sales_file.close()

read_sales()
