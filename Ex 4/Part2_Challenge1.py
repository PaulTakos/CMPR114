# Exercise 4
# Part 2 Challenge 1
# Author: Paul Takemoto

# Asks user to input a distance in km, then converts to miles and prints the result.
def main():
    distance_km = float(input('Enter a distance in kilometers: '))
    distance_mi = km_to_mi(distance_km)
    print(f'{distance_km: .2f} km = {distance_mi: .2f} mi.')

# Converts the value in kilometers to miles.
def km_to_mi(val_km):
    val_mi = val_km * 0.6214
    return val_mi

# Calls the main function
main()
