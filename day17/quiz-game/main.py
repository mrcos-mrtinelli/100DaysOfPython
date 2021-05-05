from data import question_data
from question_model import Question
from quiz_brain import Quiz

question_bank = []
for item in question_data:
    q = item["question"]
    a = item["correct_answer"]
    q_a = Question(q, a)
    question_bank.append(q_a)

quiz = Quiz(question_bank)

while quiz.still_has_questions():
    quiz.next_question()