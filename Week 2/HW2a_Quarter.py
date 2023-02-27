month = int(input('Enter month number between 1-12: '))
#Prints the corresponding quarter
if month < 1 or month > 12:
    print('Error: Number must be between 1 and 12.')
else:
    if month >= 1 and month <= 3:
        print('Your month is in the 1st quarter.')
    elif month >= 4 and month <= 6:
        print('Your month is in the 2nd quarter.')
    elif month >= 7 and month <= 9:
        print('Your month is in the 3rd quarter.')
    elif month >= 10 and month <= 12:
        print('Your month is in the 4th quarter.')

