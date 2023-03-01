# Exercise 3 Part 1
# Challenge 1
# Name: Paul Takemoto

MAX_TEMP = 102.5
temp1 = float(input('Enter temperature 1: '))
# Checks the input temperature to ensure it's less than 102.5 degrees.
while temp1 > MAX_TEMP:
    print('The temperature is too high.')
    temp1 = float(input('Enter new temperature 1: '))

temp2 = float(input('Enter temperature 2: '))
while temp2 > MAX_TEMP:
    print('The temperature is too high.')
    temp2 = float(input('Enter new temperature 2: '))

temp3 = float(input('Enter temperature 3: '))
while temp3 > MAX_TEMP:
    print('The temperature is too high.')
    temp3 = float(input('Enter new temperature 3: '))

temp4 = float(input('Enter temperature 4: '))
while temp4 > MAX_TEMP:
    print('The temperature is too high.')
    temp4 = float(input('Enter new temperature 4: '))

# Gets the sum and average of the 4 temperatures.
temp_sum = temp1 + temp2 + temp3 + temp4
temp_avg = temp_sum / 4

print('Sum: ', temp_sum)
print('Average: ', temp_avg)
