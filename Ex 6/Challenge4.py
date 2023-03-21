# Exercise 6 Challenge 4
# Author: Paul Takemoto

def write_records():
    num_emps = int(input('Enter number of employee records: '))

    emp_file = open('employees.txt', 'w')

    for count in range(1, num_emps + 1):
        print('Enter data for employee #', count)
        name = input('NAME: ')
        id_num = input('ID NUMBER: ')
        dept = input('DEPARTMENT: ')

        emp_file.write(name + '\n')
        emp_file.write(id_num + '\n')
        emp_file.write(dept + '\n')

        print()

    emp_file.close()
    print('Recorded.\n')

def read_records():
    emp_file = open('employees.txt', 'r')

    line = emp_file.readline().rstrip()
    while line != '':
        print(line)
        line = emp_file.readline().rstrip()

    emp_file.close()

write_records()

read_records()
