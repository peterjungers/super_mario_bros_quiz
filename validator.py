"""
This module contains functions that validate user input.
"""


def abc(user_answer):
    while True:
        if (user_answer.lower() == "a"
            or user_answer.lower()  == "b"
            or user_answer.lower()  == "c"):
            return user_answer.lower()
        else:
            user_answer = input("Invalid answer. Please try again: ")


def y_n(answer):
    while True:
        if answer.upper() == "Y" or answer.upper() == "N":
            return answer.upper()
        else:
            answer = input("Please answer \"Y\" or \"N\": ")
