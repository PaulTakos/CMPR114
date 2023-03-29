# Exercise 7a Project 4
# Paul Takemoto

def main():
    csv_file = open('test_scores.csv', 'r')

    lines = csv_file.readlines()

    csv_file.close()

    # Process the lines
    for line in lines:
        # Get test score as tokens
        tokens = line.split(',')

        # Calculate total of test scores
        total = 0.0
        for token in tokens:
            total += float(token)

        # Calculate average of test scores
        average = total / len(tokens)
        print(f'Average: {average}')

if __name__ == '__main__':
    main()
