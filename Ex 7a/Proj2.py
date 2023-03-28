# Exercise 7a Project 2
# Paul Takemoto
import login

def main():
    # Get a password from user
    password = input('Enter your password: ')

    # Validates password
    while not login.valid_password(password):
        print('That password is not valid.')
        password = input('Enter your password: ')

    print('That is a valid password.')

# Calls main function
if __name__ == '__main__':
    main()
