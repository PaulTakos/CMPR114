# HW11 Project 2
# Paul Takemoto

import Employee_data

def main():
    # Creates 3 Employee objects w/ info filled in
    employee1 = Employee_data.Employee('Susan Meyers', '47899', 'Accounting', 'Vice President')
    employee2 = Employee_data.Employee('Mark Jones', '39119', 'IT', 'Programmer')
    employee3 = Employee_data.Employee('Joy Rogers', '81774', 'Manufacturing', 'Engineer')

    print('Employee 1: ' + employee1.get_name() + ', ' + employee1.get_id())
    print('Department: ' + employee1.get_department() + ', ' + employee1.get_job() + '\n')

    print('Employee 2: ' + employee2.get_name() + ', ' + employee2.get_id())
    print('Department: ' + employee2.get_department() + ', ' + employee2.get_job() + '\n')

    print('Employee 3: ' + employee3.get_name() + ', ' + employee3.get_id())
    print('Department: ' + employee3.get_department() + ', ' + employee3.get_job() + '\n')

main()
