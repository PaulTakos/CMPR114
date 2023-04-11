# Midterm Project 5
# Paul Takemoto

def main():
    num_list = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    total = 0  # Initialize total value

    # Uses a for loop to add all numbers in list
    for num in num_list:
        total += num
    average = total / len(num_list)  # Calculates average

    # Prints outputs
    print(f'Total: {total}')
    print(f'Average: {average}')

main()
