question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


class QuizBrain:
    def __init__(self, q_list):
        self.number = 0
        self.list = q_list
        self.score = 0

    
    def still_has_questions(self):
        return self.number < len(self.list)
        
    
    def next_question(self):
        current_question = self.list[self.number]
        self.number += 1
        user_answer = input(f"Q.{self.number}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)


    def check_answer(self, user_answer, question_answer):
        answer_correct = user_answer.lower() == question_answer.lower()
        if answer_correct:
            self.score += 1
            print('You got it right!')
        else:
            print('You got it wrong :(')
        print(f'The correct answer is: {question_answer}')    
        print(f'Your current score is: {self.score}/{self.number}\n')
    

question_bank = []
for entry in question_data:
    new_data = Question(entry['text'], entry['answer'])
    question_bank.append(new_data)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions:
    quiz.next_question()
print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.number}")