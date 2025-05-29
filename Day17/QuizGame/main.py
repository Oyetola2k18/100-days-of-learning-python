from question_model import Question
#importing the question class
from quiz_brain import QuizBrain
from data import question_data

question_bank=[]
for x in range(len(question_data)):
    quest = question_data[x]["question"]
    answer = question_data[x]["correct_answer"]

    question = Question(quest,answer)
    question_bank.append(question)


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("You Have completed the Quiz")
print(f"Your final Score Was:{quiz.score}/{len(question_bank)}")