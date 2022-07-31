"""
Gets data.
"""


from data_layer import  Data


class QuestionAnswers:

    def __init__(self, question, answer, wrong_answer_1, wrong_answer_2):
        self._question = question
        self._answer = answer
        self._wrong_answer_1 = wrong_answer_1
        self._wrong_answer_2 = wrong_answer_2

    @property
    def question(self):
        return self._question

    @property
    def answer(self):
        return self._answer

    @property
    def wrong_answer_1(self):
        return self._wrong_answer_1

    @property
    def wrong_answer_2(self):
        return self._wrong_answer_2

    @staticmethod
    def get_row(row_id):
        data = Data.read_data(row_id)
        for row in data:
            row = QuestionAnswers(row[1], row[2], row[3], row[4])
        return row
