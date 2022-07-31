# ****************************************************************************
# Author:           Peter Jungers
# Program name:     Super Mario Bros. quiz
# Version:	        1.0
# Date:             July 2022
# Description:      A quiz about Super Mario Bros. games
# Main module:      super_mario_bros_quiz.py
# Other modules:    data_layer.py, logic_layer.py, utilities.py, validator.py
# Related files:    super_mario_bros_quiz.db
# ****************************************************************************

"""
This is the main module. It contains two functions which guide the
program.
"""


import random
import textwrap
import time

from logic_layer import QuestionAnswers
import utilities
import validator


def super_mario_bros_quiz():
    utilities.header()

    print("This quiz consists of ten randomized questions about Super\n"
          "Mario Bros. games. Your score will be presented to you at\n"
          "the end. Good luck!\n"
          "\n"
          "Program written July 2022 by Peter Jungers")
    print()
    input("Press the Enter key when you are ready.")

    take_quiz = "Y"
    while take_quiz == "Y":
        utilities.clear_terminal()
        quiz()
        take_quiz = validator.y_n(input("Try the quiz again? (Y/N) "))

    print()
    print("No problem. Have a good one!")
    time.sleep(2)


def quiz():
    utilities.header()

    asked_questions = []
    question_number = 1
    amount_correct = 0

    while question_number < 11:
        row_id = random.randint(1, 20)
        if row_id not in asked_questions:
            asked_questions.append(row_id)

            # List object "row" consists of:
            # row.question, row.answer, row.wrong_answer_1, row.wrong_answer_2
            row = QuestionAnswers.get_row(row_id)
            current_question = (f"{question_number}. {row.question}")
            # Formats question
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
            print("- " * 30)
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
