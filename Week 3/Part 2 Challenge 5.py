# Exercise 3 Part 2
# Challenge 5
# Author: Paul Takemoto

total_time = 0
time_min = 0
time_max = 0

num_laps = int(input('Enter number of laps run: '))
# Collects the time in minutes for each lap.
for num in range(num_laps):
    print('Lap', (num + 1))
    lap_time = float(input('Enter the time (minutes) for this lap: '))
    # For 1st lap, sets min and max time as Lap 1 time.
    if num == 0:
        time_min = lap_time
        time_max = lap_time
    # After 1st lap, compares new lap times to current min and max to determine
    # new min and max times
    else:
        if lap_time > time_max:
            time_max = lap_time
        elif lap_time < time_min:
            time_min = lap_time
    total_time += lap_time

# Gets the average time
avg_time = total_time / num_laps

print('Slowest time: ', time_max, 'minutes')
print('Fastest time: ', time_min, 'minutes')
print(f'Average time: {avg_time: .2f} minutes')
