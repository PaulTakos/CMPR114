# HW 5 Project 3
# Author: Paul Takemoto

def main():
    # Asks user to enter total monthly sales, then gets the county and state taxes
    sales_month = float(input('Enter the total sales for the month: '))
    tax_county = get_county_tax(sales_month)
    tax_state = get_state_tax(sales_month)

    # Gets the total tax by adding county and state values
    tax_total = tax_county + tax_state

    print(f'County sales tax: ${tax_county: ,.2f}')
    print(f'State sales tax: ${tax_state: ,.2f}')
    print(f'Total sales tax: ${tax_total: ,.2f}')

# Function to get the county tax based on input sales
def get_county_tax(sales):
    result_county = sales * 0.025
    return result_county

# Function to get the state tax based on input sales
def get_state_tax(sales):
    result_state = sales * 0.05
    return result_state

# Calls the main function
main()
