# Midterm Project 4
# Paul Takemoto

def main():
    write_expenses()
    read_expenses()

def write_expenses():
    expense_file = open('expenses.txt', 'w')

    rent = float(input('Enter your expenses for rent: '))
    gas = float(input('Enter your expenses for gas: '))
    food = float(input('Enter your expenses for food: '))
    clothing = float(input('Enter your expenses for clothing: '))
    car_pay = float(input('Enter your expenses for car payments: '))

    expense_file.write(f'Rent: ${rent: .2f}\n')
    expense_file.write(f'Gas: ${gas: .2f}\n')
    expense_file.write(f'Food: ${food: .2f}\n')
    expense_file.write(f'Clothing: ${clothing: .2f}\n')
    expense_file.write(f'Car payment: ${car_pay: .2f}\n')

def read_expenses():
    expense_file = open('expenses.txt', 'r')

    line = expense_file.readline().rstrip()
    while line != '':
        print(line)
        line = expense_file.readline().rstrip()

if __name__ == '__main__':
    main()
