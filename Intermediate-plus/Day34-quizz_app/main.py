from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


# print(question_bank) It is literally full of Question type objects
# [<question_model.Question object at 0x0000021C549D0BF0>, <question_model.Question object at 0x0000021C549D1130>, <question_model.Question object at 0x0000021C549E1B50>, <question_model.Question object at 0x0000021C549E0A70>, <question_model.Question object at 0x0000021C549E0AA0>, <question_model.Question object at 0x0000021C549E0AD0>, <question_model.Question object at 0x0000021C549E0B00>, <question_model.Question object at 0x0000021C549E0B30>, <question_model.Question object at 0x0000021C549E0B60>, <question_model.Question object at 0x0000021C549E0BC0>]

# instancia de QuizBrain q se crea con el atributo question_bank lleno de instancias de Question
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)


