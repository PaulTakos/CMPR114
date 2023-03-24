# Exercise 6 Challenge 4
# Author: Paul Takemoto

def write_records():
    num_emps = int(input('Enter number of employee records: '))

    emp_file = open('employees.txt', 'w')  # Opens file for writing

    for count in range(1, num_emps + 1):
        # Asks user to input name, ID, and department for each employee
        print('Enter data for employee #', count)
        name = input('NAME: ')
        id_num = input('ID NUMBER: ')
        dept = input('DEPARTMENT: ')

        # Writes each info to file
        emp_file.write(name + '\n')
        emp_file.write(id_num + '\n')
        emp_file.write(dept + '\n')

        print()

    emp_file.close()  # Closes file
    print('Recorded.\n')

def read_records():
    emp_file = open('employees.txt', 'r')  # Opens file for reading

    # Uses a while loop to read and print each line from the file.
    line = emp_file.readline().rstrip()
    while line != '':
        print(line)
        line = emp_file.readline().rstrip()

    emp_file.close()  # Closes file

write_records()

read_records()
