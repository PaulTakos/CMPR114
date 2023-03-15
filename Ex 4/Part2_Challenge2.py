# Exercise 4
# Part 2 Challenge 2
# Author: Paul Takemoto

def main():
    # Asks the user to input values of automobile expenses
    loan_payment = float(input('Enter monthly loan payment: '))
    insurance = float(input('Enter monthly insurance: '))
    gas = float(input('Enter monthly gas cost: '))
    oil = float(input('Enter monthly oil costs: '))
    tires = float(input('Enter monthly tire costs: '))
    maintenance = float(input('Enter monthly maintenance costs: '))

    # Uses input values to find total monthly and annual costs, then prints out results
    total_monthly, total_annual = get_totals(loan_payment, insurance, gas, oil, tires, maintenance)
    print(f'Total monthly cost: ${total_monthly: .2f}')
    print(f'Total annual cost: ${total_annual: .2f}')

# Adds the values to get the monthly total, then gets the annual total by multiplying by 12
def get_totals(val1, val2, val3, val4, val5, val6):
    total_month = val1 + val2 + val3 + val4 + val5 + val6
    total_year = total_month * 12
    return total_month, total_year

# Calls the main function
main()
