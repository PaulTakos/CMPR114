# HW 3-7 Project 1
# Author: Paul Takemoto

def main():
    # Gets the list of scores and the total
    scores = get_scores()
    total = get_total(scores)

    # Finds lowest score and subtracts from total
    lowest = min(scores)
    total -= lowest

    # Gets the average score without the lowest one
    average = total / (len(scores) - 1)
    print('The average, with the lowest score dropped, is ', average)

    # Writes the results to a file
    outfile = open('scores.txt', 'w')
    outfile.write('All scores: \n')
    for num in scores:
        outfile.write(f'{num:.2f}\n')
    outfile.write(f'\nAverage score (without lowest): {average: .2f}')
    outfile.close()
    print('All scores written to file.')

def get_scores():
    test_scores = []
    again = 'y'
    while again == 'y':
        value = float(input('Enter a test score: '))
        test_scores.append(value)
        # Want to do this again?
        print('Do you want to add another score?')
        again = input('\'y\' = yes, anything else = no: ')

    # return the list
    return test_scores

def get_total(value_list):
    # Gets values from list and adds to total.
    total = 0.0
    for num in value_list:
        total += num

    return total

main()
