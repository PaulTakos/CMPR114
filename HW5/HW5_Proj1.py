# HW 5 Project 1
# Author: Paul Takemoto

def main():
    # Asks user to input actual property value, then calls functions to
    # calculate assessment value and property tax.
    value_actual = float(input('Enter actual property value: '))
    value_assessment = get_assessment_value(value_actual)
    tax_prop = get_property_tax(value_assessment)

    print(f'Assessment value: ${value_assessment: ,.2f}')
    print(f'Property tax: ${tax_prop: ,.2f}')

# Function to calculate assessment value (60% of actual)
def get_assessment_value(actual):
    assessment = actual * 0.6
    return assessment

# Function to calculate property tax (0.72% of assessment)
def get_property_tax(val):
    tax = val * 0.0072
    return tax

# Calls main function
main()
