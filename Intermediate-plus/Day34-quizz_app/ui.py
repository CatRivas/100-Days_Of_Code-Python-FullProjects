import tkinter as tk
from tkinter import Canvas
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_questions: QuizBrain):
        self.quiz = quiz_questions

        # Main window
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score label
        self.score_label = tk.Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 12, "bold"))
        self.score_label.grid(row=0, column=1)

        # Question canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
            width=280
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # "True" and "False" buttons
        true_img = tk.PhotoImage(file="images/true.png")
        self.true_button = tk.Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_img = tk.PhotoImage(file="images/false.png")
        self.false_button = tk.Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        # Load the first question
        self.get_next_question()

        # Prevent the window from being resized
        self.window.resizable(False, False)
        
        # Keep the window running
        self.window.mainloop()

    # Load the next question
    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've completed the quiz")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    # Handle "True" button press
    def true_pressed(self):
        real_answer = self.quiz.check_answer('True')
        self.canvas_color_feedback(real_answer)

    # Handle "False" button press
    def false_pressed(self):
        real_answer = self.quiz.check_answer('False')
        self.canvas_color_feedback(real_answer)

    # Change canvas background color based on the answer
    def canvas_color_feedback(self, answer):
        if answer:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.window.after(500, self.canvas_color_reset)  

    # Reset the canvas color and update the score
    def canvas_color_reset(self):
        self.canvas.config(bg='white')
        self.score_update()
        self.get_next_question()

    # Update the score label
    def score_update(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")
