# Midterm Project 7
# Paul Takemoto

LUCKY_NUM = 7

def main():
    num_list_2d = [[1, 2],
                   [3, 4],
                   [5, 6],
                   [7, 8],
                   [9, 10]]

    for list_component in num_list_2d:
        for num in list_component:
            if num == LUCKY_NUM:
                print(f'You found the lucky number {num} in the list at index {num_list_2d.index(list_component)}')

main()
