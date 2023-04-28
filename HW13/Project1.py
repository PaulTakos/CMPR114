# HW 13 Project 1
# Paul Takemoto

import Employee_data

def main():
    name = input('Enter your name: ')
    number = int(input('Enter your employee number: '))
    yearly_sal = float(input('Enter your yearly salary: '))
    bonus = float(input('Enter your yearly production bonus: '))

    supervisor = Employee_data.ShiftSupervisor(name, number, yearly_sal, bonus)

    print()
    print('Employee name: ', supervisor.get_name())
    print('Employee number: ', supervisor.get_number())
    print(f'Employee annual salary: ${supervisor.get_annual_salary(): .2f}')
    print(f'Employee production bonus: ${supervisor.get_prod_bonus(): .2f}')

main()
