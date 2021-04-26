# Question

class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def CheckAnswer(self, answer):
        return self.answer == answer     

#Quiz

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0
    def getQuestions(self):
        return self.questions[self.questionIndex]
    def displayquesiton(self):
        question = self.getQuestions



q1 = Question("en iyi programlama dili hangisidir ? ", ["C#", "Python", "java", "CSS"], "Python")
q2 = Question("en popüler programlama dili hangisidir ? ", ["C#", "Python", "java", "CSS"], "Python")
q3 = Question("en basit programlama dili hangisidir ? ", ["C#", "Python", "java", "CSS"], "Python")

questions = [q1, q2, q3]

quiz = Quiz(questions)
question = quiz.getQuestions()
print(question.text)