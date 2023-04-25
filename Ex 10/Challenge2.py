# Ex 10 Challenge 2
# Paul Takemoto

class Person:
    def __init__(self, name, age, address, city, state, zipcode):
        self.name = name
        self.age = age
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode

# Student class inherits from Person class
class Student(Person):
    def __init__(self, name, age, address, city, state, zipcode, studentID, GPA):
        super().__init__(name, age, address, city, state, zipcode)
        self.studentID = studentID
        self.GPA = GPA

class Teacher(Person):
    def __init__(self, name, age, address, city, state, zipcode, teacherID, classTeaching):
        super().__init__(name, age, address, city, state, zipcode)
        self.teacherID = teacherID
        self.classTeaching = classTeaching

student = Student('Jane Doe', 25, '1234 Tower Ln', 'Santa Ana', 'CA', 54321, 777, 3.8)
print('Student name: ', student.name)
print('Student age: ', student.age)
print('Student address: ', student.address)
print('Student city: ', student.city)
print('Student state: ', student.state)
print('Student zipcode: ', student.zipcode)
print('Student ID: ', student.studentID)
print('Student GPA: ', student.GPA)

print('\n')

teacher = Teacher('Ms. Cantor', 45, '543 City St', 'Santa Ana', 'CA', '54321', 7, 'Python')
print('Teacher name: ', teacher.name)
print('Teacher age: ', teacher.age)
print('Teacher address: ', teacher.address)
print('Teacher city: ', teacher.city)
print('Teacher state: ', teacher.state)
print('Teacher zipcode: ', teacher.zipcode)
print('Teacher ID: ', teacher.teacherID)
print('Teacher class: ', teacher.classTeaching)
