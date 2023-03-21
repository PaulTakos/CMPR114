# Exercise 6 Challenge 3
# Author: Paul Takemoto

def sales():
    total_sales = 0.0

    num_days = int(input('Enter # of days of sales: '))
    sales_file = open('sales.txt', 'w')

    for count in range(1, num_days + 1):
        sale = float(input('Enter the sales for day #' + str(count) + ': '))
        total_sales += sale
        sales_file.write(str(sale) + '\n')

    salary = float(input('Enter your salary: '))

    if total_sales > 1000:
        salary = salary * 1.1
    sales_file.write(str(salary) + '\n')

    sales_file.close()
    print('Sales and salary recorded.')

sales()

def read_sales():
    sales_file = open('sales.txt', 'r')
    line = sales_file.readline()
    while line != '':
        amount = float(line)
        print(f'{amount: .2f}')
        line = sales_file.readline()

    sales_file.close()

read_sales()
