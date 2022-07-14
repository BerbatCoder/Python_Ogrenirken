# import random
# Quiz Uygulaması

class Question():
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    def checkanswe(self, answer):
        return self.answer == answer

class Quiz():
    def __init__(self, question):
         self.question = question
         self.score = 0
         self.questionIndex = 0

    def getQuestion(self):
        return self.question[self.questionIndex]
    
    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Soru {self.questionIndex + 1}: {question.text}')

        for q in question.choices:
            print("-" + q)

        answer = input('Cevap Nedir: ')
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):

        if question.checkanswe(answer):
            self.score += 1
        self.questionIndex += 1
        

    def loadQuestion(self):
        if len(self.question) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()
    

    def showScore(self):
        print('Score', self.score)

    def displayProgress(self):
        totalQuestion = len(self.question)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            print('Quiz Bitti')
        else:
            print(f'Question {questionNumber} of {totalQuestion}'.center(100,'*'))

q1 = Question('Hangi programlama dilini seviyorsunuz : ', ['c#' , 'python', 'javascript', 'java'],'python')
q2 = Question('Hangi programlama dili en iyisi : ', ['java' , 'python', 'javascript', 'c#'],'python')
q3 = Question('Hangi programlama dilini çöpe atarsın : ', ['javascript' , 'java', 'c#', 'python'],'python')

question = [q1,q2,q3]
quiz = Quiz(question)
question = quiz.getQuestion()
quiz.loadQuestion()





"""
Sorular = ['Papatya severmisin ?' ,'İsmini Girermisin ?' ,'Sen Kimsin ? ', 'Buda Neyin nesi ? ']
cevaplar = ['Severim', 'Onur', 'Benim', 'Sanane ki']
ne = random.randint(0,4)
class Question():
    def __init__(self, name):
        print(Sorular[ne])
        self.name = name
    def cevap(self):
        cevap = input('Sorunun Cevabını Giriniz : ')
        if ne == 0:
            if cevap == cevaplar[0]:
                print(f'Doğru Cevap {self.name}')
        elif ne == 1:
            if cevap == cevaplar[1]:
                print(f'Doğru Cevap {self.name}')
        elif ne == 2:
            if cevap == cevaplar[2]:
                print(f'Doğru Cevap {self.name}')
        elif ne == 3:
            if cevap == cevaplar[3]:
                print(f'Doğru Cevap {self.name}')

p1 = Question('Onur')
p1.cevap()
"""
