class Quiz:

    def __init__(self, questions_list):
        self.question_number = 0
        self.score = 0
        self.question_list = questions_list

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            print(f"\nQuiz Completed!\nFinal score: {self.score}/{len(self.question_list)}")
            return False

    def next_question(self):
        question = self.question_list[self.question_number]
        correct_answer = question.answer
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text} (True/False) ")
        self.check_answer(user_answer, correct_answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Correct!")
        else:
            print(f"Sorry! The correct answer is {correct_answer}.")

        print(f"Current score: {self.score}/{len(self.question_list)}\n\n")
