# Exercise 9 Challenge 3
# Paul Takemoto

class PI:
    def GetInformation(self, LN, FN, age, address, city, state, zipcode):
        return LN, FN, age, address, city, state, zipcode

PersonalInformation = PI()  # PI object
PersonalInformation.LastName = input('Enter your last name: ')
PersonalInformation.FirstName = input('Enter your first name: ')
PersonalInformation.Age = int(input('Enter your age: '))
# Also asks user for address, city, state, and zip code, which are added to personal information
PersonalInformation.Address = input('Enter your address: ')
PersonalInformation.City = input('Enter your city: ')
PersonalInformation.State = input('Enter your state: ')
PersonalInformation.Zipcode = int(input('Enter your zipcode: '))

# Prints out each info using GetInformation function and passing in the respective arguments
print(PersonalInformation.GetInformation(PersonalInformation.LastName, PersonalInformation.FirstName,
                                         PersonalInformation.Age, PersonalInformation.Address,
                                         PersonalInformation.City, PersonalInformation.State,
                                         PersonalInformation.Zipcode))
