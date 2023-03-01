# Exercise 3.7
# Challenge 3
# Author: Paul Takemoto

months_list = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]
rain_list = []
rain_total = 0.0
count = 0
rain_max = 0.0
rain_min = 0.0

for month in months_list:
    rainfall = float(input(f'Enter the amount of rain in {month}: '))
    rain_list.insert(count, rainfall)
    # For 1st month, sets min and max rainfall as January amount.
    if count == 0:
        rain_min = rainfall
        month_min = month
        rain_max = rainfall
        month_max = month
    # After 1st month, compares new rainfall to current min and max to determine
    # new min and max rainfall
    else:
        if rainfall > rain_max:
            rain_max = rainfall
            month_max = month
        elif rainfall < rain_min:
            rain_min = rainfall
            month_min = month
    rain_total += rainfall
    count += 1
rain_avg = rain_total / len(months_list)

# Prints total and average rainfall, and min and max month/rainfall.
print(f'The total rainfall this year was {rain_total: .2f} inches.')
print(f'The average rainfall this year was {rain_avg: .2f} inches.')
print(f'The month with highest rainfall was {month_max}, with {rain_max: .2f} inches of rain.')
print(f'The month with lowest rainfall was {month_min}, with {rain_min: .2f} inches of rain.')

# Writes to file
outfile = open('rain.txt', 'w')
for value in rain_list:
    outfile.write(f'{value:.2f}\n')
outfile.write(f'\nTotal rain: {rain_total: .2f}')
outfile.write(f'\nAverage rain: {rain_avg: .2f}')
outfile.close()
print('Rainfall values written to file.')
