import chat_interface

def main():
    chat_gpt_answer = chat_interface.interface()

    for count in range(3):
        question = input(f'Enter question {count + 1}: ')
        answer = chat_gpt_answer.answer_question(question)
        print(answer)

main()
