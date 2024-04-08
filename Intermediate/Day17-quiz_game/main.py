from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
    
for item in question_data:
    q = item['text']
    a = item['answer']

    question = Question(q, a)
    question_bank.append(question)

# print(question_bank)  #devuelve una lista de 12 objetos con sus direcciones
# print(len(question_bank)) #12
# print(question_bank[2].question) #"Approximately one quarter of human bones are in the feet". imprime si llamas a la variable q le pusiste al crear la clase.

quiz = QuizBrain(question_bank)

while quiz.still_has_questions(): #while that is true will run and is not infinite 
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{len(question_bank)}.")
