# ****************************************************************************
# Author:           Peter Jungers
# Program name:     Super Mario Bros. quiz
# Version:	        1.0
# Date:             July 2022
# Description:
# Main module:      super_mario_bros_quiz.py
# Other modules:
# Related files:
# ****************************************************************************


import random
import textwrap
import time

from logic_layer import QuestionAnswers
import validator


def super_mario_bros_quiz():
    print("- " * 30)
    print("Super Mario Bros. quiz".center(60))
    print("- " * 30)
    print()
    print("Ten questions will be presented at random. Your score will\n"
          "be presented to you at the end. Good luck!")
    print()
    input("Press the Enter key when you are ready.")
    print()

    take_quiz = "Y"
    while take_quiz == "Y":
        quiz()
        take_quiz = validator.y_n(input("Try the quiz again?"))

    print("Have a good one!")
    time.sleep(2)


def quiz():
    asked_questions = []
    question_number = 1
    amount_correct = 0

    while question_number < 2:
        row_id = random.randint(1, 20)
        if row_id not in asked_questions:
            asked_questions.append(row_id)

            print("- " * 30)
            print()
            # List object "row" consists of:
            # row.question, row.answer, row.wrong_answer_1, row.wrong_answer_2
            row = QuestionAnswers.get_row(row_id)
            current_question = (f"{question_number}. {row.question}")
            # Formats question string
            wrapped_question = textwrap.fill(
                current_question, width=56, subsequent_indent=(" " * 3)
            )
            print(wrapped_question)
            print()

            choices = [row.answer, row.wrong_answer_1, row.wrong_answer_2]
            random.shuffle(choices)
            # Answers have been put in random order
            a = choices[0]
            b = choices[1]
            c = choices[2]
            print("a)", a)
            print("b)", b)
            print("c)", c)
            print()
            user_answer = validator.abc(input("Answer: "))
            time.sleep(1)

            if (user_answer == "a" and a == row.answer
                or user_answer == "b" and b == row.answer
                or user_answer == "c" and c == row.answer):
                print("Correct!")
                amount_correct += 1
            else:
                print("Sorry, incorrect.")
            time.sleep(1)
            print()

            question_number += 1

    print("Tallying your score...")
    time.sleep(2)
    if amount_correct > 6:
        encouragement = "Great job!"
    elif amount_correct <= 6:
        encouragement = "You'll do better next time!"
    print(f"You earned {amount_correct}/10. {encouragement}")
    print()


if __name__ == "__main__":
    super_mario_bros_quiz()