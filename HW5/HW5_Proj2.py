# HW 5 Proj 2
# Author: Paul Takemoto

def main():
    # Asks user to input number of tickets sold for each class
    tickets_a = int(input('How many Class A tickets were sold? '))
    tickets_b = int(input('How many Class B tickets were sold? '))
    tickets_c = int(input('How many Class C tickets were sold? '))

    total_income = get_income(tickets_a, tickets_b, tickets_c)

    print(f'Total income from ticket sales: ${total_income: ,.2f}')

# Function to calculate total income based on number of tickets sold for each class
def get_income(num_a, num_b, num_c):
    total = (num_a * 20.0) + (num_b * 15.0) + (num_c * 10.0)
    return total

# Calls main function
main()
