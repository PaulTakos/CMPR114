# Midterm Project 5
# Paul Takemoto

def main():
    num_list = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    total = 0
    for num in num_list:
        total += num
    average = total / len(num_list)

    print(f'Total: {total}')
    print(f'Average: {average}')

main()
