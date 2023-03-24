# Exercise 6 Challenge 7
# Author: Paul Takemoto

def write_grades():
    grades_file = open('grades.txt', 'a')  # Opens file for appending

    while True:  # Uses while loop to
        try:
            # Asks user to input name and test scores
            name = input('Enter full name: ')
            score_midterm = float(input('Enter midterm score: '))
            while score_midterm > 100:  # while loop ensures midterm score is below 100
                print('Score must be below 100!')
                score_midterm = float(input('Enter midterm score again: '))

            score_final = float(input('Enter final score: '))
            while score_final > 100:  # while loop ensures final score is below 100
                print('Score must be below 100!')
                score_final = float(input('Enter final score again: '))

            break
        except ValueError:  # Throws exception for invalid entries for scores
            print('ERROR: Scores must be valid numbers!')

    # Calculates average score and gets letter grade using functions
    score_avg = findAverage(score_midterm, score_final)
    grade_avg = getLetterGrade(score_avg)

    # Writes name, average score, letter grade to file
    grades_file.write('Name: ' + name + '\n')
    grades_file.write('Average score: ' + str(format(score_avg, '.2f')) + '\n')
    grades_file.write('Average grade: ' + grade_avg + '\n')

    grades_file.close()

def findAverage(num1, num2):  # Calculates average
    avg = float((num1 + num2) / 2)
    return avg

def getLetterGrade(score):  # Assigns letter grade to average score
    if score >= 90 and score <= 100:
        letter = 'A'
    elif score >= 80 and score <= 89:
        letter = 'B'
    elif score >= 70 and score <= 79:
        letter = 'C'
    elif score >= 60 and score <= 69:
        letter = 'D'
    else:
        letter = 'F'

    return letter

def read_grades():
    grades_file = open('grades.txt', 'r')  # Opens file for reading

    # Uses while loop to read and print each line from file until blank line encountered
    line = grades_file.read().rstrip()
    while line != '':
        print(line)
        line = grades_file.read().rstrip()

    grades_file.close()

write_grades()

read_grades()
