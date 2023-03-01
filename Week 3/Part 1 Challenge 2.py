# Exercise 3 Part 1
# Challenge 2
# Name: Paul Takemoto

num_input = 0
sales_total = 0.0
commission_total = 0.0

# Gets sales and commission rate 4 times
while num_input < 4:
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commission rate: '))
    # Adds to total sales and commission
    sales_total = sales_total + sales
    commission = sales * comm_rate
    commission_total = commission_total + commission
    num_input += 1

# Prints total sales and commission
print(f'Total sales: ${sales_total: .2f}.')
print(f'Total commission: ${commission_total: .2f}')
