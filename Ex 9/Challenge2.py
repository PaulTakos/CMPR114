# Exercise 9 Challenge 2
# Paul Takemoto

class Teacher:
    # using init to create customized constructor with 3 arguments
    def __init__(self, name, classroom, course):
        self.name = name
        self.classroom = classroom
        self.course = course

    def GetProfessor(self):
        print('Name: ' + self.name)
        print('Class: ' + self.classroom)
        print('Course: ' + self.course)

# new Teacher objects, each with 3 arguments (name, classroom, course)
Teacher1 = Teacher('Prof. Sim', 'A206', 'Python Programming')
Teacher2 = Teacher('Prof. Princeton', 'A223', 'Music Theory')

Teacher1.GetProfessor()
Teacher2.GetProfessor()
