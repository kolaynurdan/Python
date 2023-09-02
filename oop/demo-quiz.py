#Question

class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    
    def checkAnswer(self, answer):
        return self.answer == answer

#q1 = Question('What is best program language in the world?', ['C#','python','javascript', 'java'], 'python')
#q2 = Question('What is earned money program language in the world?', ['C#','python','javascript', 'java'], 'python')
#list = [q1,q2]

#print(q1.checkAnswer('python'))
#print(q2.checkAnswer('java'))

#Quiz

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Soru {self.questionIndex + 1}: {question.text}')
        for q in question.choices:
            print('-'+ q)

        answer = input('Response: ')
        self.guess(answer)

    def guess(self, answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score +=1
        self.questionIndex += 1
    
q1 = Question('What is best program language in the world?', ['C#','python','javascript', 'java'], 'python')
q2 = Question('What is earned money program language in the world?', ['C#','python','javascript', 'java'], 'python')
questions = [q1,q2]

quiz = Quiz(questions)
question = quiz.questions[quiz.questionIndex]
print(question.text, question.choices,question.choices,question.answer)