# Exercise 9 Challenge 1
# Paul Takemoto

class Students:
    # the keyword (self)
    def GetInformation(self):
        print("Last name: " + self.LastName)
        print("First name: " + self.FirstName)
        print("Address: " + self.Address)
        print("City: " + self.City)
        print("State: " + self.State)
        print("Zipcode: " + self.Zipcode)

# Student1 object
Student1 = Students()
Student1.LastName = 'Doe'
Student1.FirstName = 'Jane'
Student1.Address = '111 St'
Student1.City = 'Santa Ana'
Student1.State = 'CA'
Student1.Zipcode = '12345'

# Student2 object
Student2 = Students()
Student2.LastName = 'Cantor'
Student2.FirstName = 'Mike'
Student2.Address = '222 St'
Student2.City = 'Garden Grove'
Student2.State = 'CA'
Student2.Zipcode = '67890'

# Student3 object - takes user input for all variables
Student3 = Students()
Student3.LastName = input('Enter new student\'s last name: ')
Student3.FirstName = input('Enter new student\'s first name: ')
Student3.Address = input('Enter new student\'s street address: ')
Student3.City = input('Enter new student\'s city: ')
Student3.State = input('Enter new student\'s state: ')
Student3.Zipcode = input('Enter new student\'s zipcode: ')

Student1.GetInformation()
Student2.GetInformation()
Student3.GetInformation()
