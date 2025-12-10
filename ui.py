from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface():
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzlet")
        self.window.config(padx = 20, pady = 20, bg= THEME_COLOR)

        correct_img = PhotoImage(file = "Day 34/images/true.png")
        false_img = PhotoImage(file= "Day 34/images/false.png")

        self.label_score = Label(text = "Score: 0", fg = "white", bg = THEME_COLOR)
        
        self.label_score.grid(row = 0, column = 1)
        
        self.canvas = Canvas(width= 300, height= 250, highlightthickness= 0)
        self.canvas.grid(row= 1, column=  0, columnspan = 2, pady = 50)
        self.question_text = self.canvas.create_text(150, 125, width = 280, text = "Hello", font=("Arial", 20, "italic"))

        self.true_button = Button(image = correct_img, highlightthickness = 0, command = self.true_pressed)
        self.true_button.grid(row = 3, column = 0)

        self.wrong_button = Button(image = false_img, highlightthickness = 0, command = self.false_pressed)
        self.wrong_button.grid(row = 3, column = 1)
        
        self.get_question()

        self.window.mainloop()

    def get_question(self):
        self.reset_canvas()
        if self.quiz.still_has_questions():
            self.label_score.config(text = f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)
        else:
            self.canvas.itemconfig(self.question_text, text = f"You have reached the end of the quiz, your final score was {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state = "disabled")
            self.wrong_button.config(state = "disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
        
    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))
    
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg = "green")
        else:
            self.canvas.config(bg = "red")
        self.window.after(1000,self.get_question)

    def reset_canvas(self):
        self.canvas.config(bg = "white")

           
            
        