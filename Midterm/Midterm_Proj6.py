# Midterm Project 6
# Paul Takemoto

LUCKY_NUM = 27  # Global lucky number variable

def main():
    num_list = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

    # Compares each number to the lucky number. If equal, prints the number and index.
    for num in num_list:
        if num == LUCKY_NUM:
            print(f'You found the lucky number {num} at index {num_list.index(num)}')

main()
