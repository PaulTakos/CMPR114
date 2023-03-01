# Exercise 3 Part 2
# Challenge 4
# Author: Paul Takemoto

# Calculates total calories for each time in minutes. Rate = 4.2 cal/min.
for time in [10, 15, 20, 25, 30]:
    calories = 4.2 * time
    print(f'Calories burned in {time} minutes: {calories: .2f}')
