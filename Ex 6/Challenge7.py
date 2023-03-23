# Exercise 6 Challenge 7
# Author: Paul Takemoto

def write_grades():
    grades_file = open('grades.txt', 'a')

    while True:
        try:
            name = input('Enter full name: ')
            score_midterm = float(input('Enter midterm score: '))
            while score_midterm > 100:
                print('Score must be below 100!')
                score_midterm = float(input('Enter midterm score again: '))

            score_final = float(input('Enter final score: '))
            while score_final > 100:
                print('Score must be below 100!')
                score_final = float(input('Enter final score again: '))

            break
        except ValueError:
            print('ERROR: Scores must be valid numbers!')

    score_avg = findAverage(score_midterm, score_final)
    grade_avg = getLetterGrade(score_avg)

    grades_file.write('Name: ' + name + '\n')
    grades_file.write('Average score: ' + str(format(score_avg, '.2f')) + '\n')
    grades_file.write('Average grade: ' + grade_avg)

    grades_file.close()

def findAverage(num1, num2):
    avg = float((num1 + num2) / 2)
    return avg

def getLetterGrade(score):
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
    grades_file = open('grades.txt', 'r')
    line = grades_file.read().rstrip()
    while line != '':
        print(line)
        line = grades_file.read().rstrip()

    grades_file.close()

write_grades()

read_grades()
