"""
This module reads data and returns it.
"""


import sqlite3


class Data:

    _connection = None

    @classmethod
    def connect(cls):
        if cls._connection == None:
            cls._connection = sqlite3.connect("super_mario_bros_quiz.db")

    @classmethod
    def read_data(cls, row_id):
        cls.connect()
        cursor = cls._connection.cursor()
        query = (
            """
            SELECT    id,
                      question,
                      answer,
                      wrong_answer_1,
                      wrong_answer_2
            FROM      questions_answers
            WHERE     id == ?
            """
        )
        cursor.execute(query, [row_id])
        row = cursor.fetchall()
        return row
