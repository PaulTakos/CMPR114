# Exercise 7a Project 2
# Paul Takemoto

def get_login_name(first, last, idnumber):
    # Get the 1st 3 letters of first name
    # If name is less than 3 characters, the
    # slice will return the entire first name
    set1 = first[0:3]

    # Get the 1st 3 letters of last name
    # If name is less than 3 characters, the
    # slice will return the entire last name
    set2 = last[0:3]

    # Get the last 3 characters of ID
    # If ID number is less than 3 characters, the
    # slice will return entire ID number
    set3 = idnumber[-3:]

    # Put the sets of characters together
    login_name = set1 + set2 + set3

def valid_password(password):
    # Sets Boolean variables to False
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    # Begin validation. Start by testing password's length
    if len(password) >= 7:
        correct_length = True

        # Test each character and set the appropriate flag when required character is found
        for ch in password:
            if ch.isupper():
                has_uppercase = True
            if ch.islower():
                has_lowercase = True
            if ch.isdigit():
                has_digit = True

    # Determine whether all requirements are met
    # If they are, set is_valid = true.
    # Otherwise, set is_valid = false.

    if correct_length and has_uppercase and has_lowercase and has_digit:
        is_valid = True
    else:
        is_valid = False

    return is_valid
