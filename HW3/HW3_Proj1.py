# HW3 Project 1
# Author: Paul Takemoto

# Asks user to input speed and time.
speed = float(input('What is the speed of the vehicle in mph? '))
hours = int(input('How many hours has it traveled? '))
distance = 0.0

# Prints header for table
print('Hour \t Distance traveled')
print('---------------------------')
# Displays distance for each hour.
for count in range(1, hours+1):
    distance = speed * count
    print(f'{count} \t \t {distance}')
