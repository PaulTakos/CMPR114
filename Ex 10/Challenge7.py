# Ex 10 Challenge 7
# Paul Takemoto

import Employee_data

def main():
    name = input('Enter your name: ')
    emp_id = int(input('Enter your employee number: '))
    shift = int(input('Enter your shift (1 = day, 2 = night): '))
    pay_rate = float(input('Enter your hourly pay rate: '))

    # New Production Worker object
    prod_worker1 = Employee_data.ProductionWorker(name, emp_id, shift, pay_rate)
    print()
    print('Employee name: ', prod_worker1.get_name())
    print('Employee number: ', prod_worker1.get_number())
    print('Shift: ', prod_worker1.get_shift_num())
    print(f'Hourly pay: ${prod_worker1.get_hourly_pay(): .2f}')

main()
