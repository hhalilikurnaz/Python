#question classı oluştur
#quiz classı quesitondan classından sorularını alıcak



class Question:
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices #bu bir dizi olcak şıklar dizisi
        self.answer=answer


    def checkAnswer(self,answer):
        return self.answer == answer


    def __str__(self):
        return self.text


q1=Question('En İyi Programlama Dili Hangisidir ?',['C','C#','Python','JavaScript','Java'],'Python')
q2 = Question("HTML'de paragraf etiketi hangisidir?", ["<div>", "<h1>", "<p>", "<span>"], "<p>")
q3 = Question("CSS hangi amaçla kullanılır?", ["Veri tabanı yönetimi", "Web sayfası tasarımı", "Sunucu yönetimi", "Mobil uygulama geliştirme"], "Web sayfası tasarımı")
q4 = Question("Python dilinde yorum satırı nasıl yazılır?", ["//", "<!--", "#", "/* */"], "#")
q5 = Question("JavaScript'te bir değişken nasıl tanımlanır?", ["let", "define", "create", "set"], "let")
questions=[q1,q2,q3,q4,q5]

#print(q1.checkAnswer('Python'))

class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.questionIndex=0 #Bu iki değişken ,kullanıcıdan gelen bilgi değil sistemin içinde yönetilen değişkenler

    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    
    def displayQuestion(self):
        question = self.getQuestion()
        print(f"\nSoru {self.questionIndex + 1}: {question.text}")

        for q in question.choices:
            print("- " + q)

        answer = input("Cevabınızı giriniz: ")

        if question.checkAnswer(answer):
            self.score += 20
            print(f"Doğru Cevap ✅\t Skorunuz : {self.score}")
        else:
            print("Cevabınız Yanlış")
            
        self.questionIndex +=1
        self.loadQuesiton()

            

        
    def loadQuesiton(self):
        if len(self.questions)==(self.questionIndex):
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print(f"Skorunuz {self.score}")

    def displayProgress(self):
        totalQuesiton=len(self.questions)
        questionnumber=self.questionIndex +1


        if questionnumber > totalQuesiton:
            print('Quiz Bitti')
        else:
            print(f"Question {questionnumber} of {totalQuesiton}".center(100,'*'))

            
            

quiz=Quiz(questions)
quiz.loadQuesiton()
