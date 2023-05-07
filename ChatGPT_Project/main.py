import chat_interface

def main():
    chat_gpt_answer = chat_interface.interface()
    question_list = []

    try:
        num_questions = int(input('How many questions would you like to ask? '))

        for count in range(num_questions):
            is_same_question = False

            question = input(f'Enter question {count + 1}: ')

            for q1 in question_list:
                if question == q1:
                    # print('You already asked that!')
                    is_same_question = True

                while is_same_question:
                    print('You already asked that!')
                    question = input(f'Enter a new question {count + 1}: ')
                    for q2 in question_list:
                        if question != q2:
                            is_same_question = False

            question_list.append(question)

            answer = chat_gpt_answer.answer_question(question)
            print(answer)

    except ValueError:
        print('You must enter an integer.')


main()
