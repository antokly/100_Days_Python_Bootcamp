from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Typical application when we receive internet datas

question_bank = [] # list of questions objects

for  question in question_data:
    q = question["text"]
    a = question["answer"]
    question_object = Question(q, a)
    question_bank.append(question_object)


quiz = QuizBrain(question_bank)

while quiz.still_has_question:
    quiz.next_question()
    
print("You've completed the quiz")
print(f"Your final score : {quiz.score} / {quiz.question_number}")