# HW3 Project 2
# Author: Paul Takemoto

rain_total = 0.0
years = int(input('Enter number of years: '))
month_total = years * 12

for year_num in range(years): # Cycles through each year.
    print(f'Year {year_num+1}')
    for month_num in range(12):  # Cycles through 12 months. User inputs rainfall for each month.
        rain = float(input(f'Enter amount of rainfall in inches for month {month_num+1}: '))
        rain_total += rain  # Adds each input to total amount.

# Calculates average rainfall over entire period.
rain_avg = rain_total / month_total

# Prints out results.
print('Total months: ', month_total)
print(f'Total rainfall: {rain_total: .2f} in')
print(f'Average rainfall: {rain_avg: .2f} in/month')
