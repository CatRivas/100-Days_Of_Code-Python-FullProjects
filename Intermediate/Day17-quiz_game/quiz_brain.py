class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0 #default value
        self.score = 0 #default value


    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            
            return True
        return False


    def next_question(self):
        #                                                  0
        current_question = self.question_list[self.question_number]
        self.question_number += 1 
        user_answer = input(f'Q.{self.question_number}: {current_question.question} (True/False): ').lower().strip()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, answer, correct_answer):   
        if answer == correct_answer.lower():
            print('You got it rigth!')
            self.score += 1
        else:
            print("That's wrong.")
       
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print('\n')
