#Inheritance User,Instructor,Student
#Compostion(İç içe nesneler):Course ,Lesson,Quiz
#Encapsulation : kapsülleme
#Polymorphism (Çok Biçimlilik)

import time #Bu modlülü ekliyorum zamanı da göstermek istediğimden

class User:
    def __init__(self,username,email):
        self.username=username
        self.email=email
        self._password="1234" #Protected sınıf içinden erişilebilir.Alt sınıflar erişebilir ama dışarıdan kullanma demek
        #Encapsulationun mantığının parçası ve gizliliği(access modifier'ları) temsil ediyor

#Pythondaki erişim türleri
#normal
#protected _var =>Dışarıdan erişme gerekirse alt sınıflarda kullanabilir
#private __var=> Adı değiştirilerek gizlenir(name mangling yapılır)

    def login(self,password):
        return self._password==password #Dışarıdan girilen password ile _password eşleşirse true döner

class Student(User):
    def __init__(self,username,email):
        super().__init__(username,email) #Constructor çağırır ve miras olan herşeyi aktif eder
        self.__enrolled_courses=[] #Encapsulation öğrencinin kayıt olduğu kurslar tutar dışarıdan erişilemez

    def enroll(self,course):
        self.__enrolled_courses.append(course)
        print(f"{self.username} {course.title} Dersine Katıldı" )


    def list_courses(self):
        for course in self.__enrolled_courses:
            print(f" {course}")

    def solve_quiz(self,course):
        if course.quiz:
            print(f" {course.title} Quiz Başlatılıyor...")
            course.quiz.start()
        else:
            print("Bu derste quiz yok")
    

class Instructor(User):
    def __init__(self,username,email):
        super().__init__(username,email)
        self.course=[] #Eğitmenin Verdiği Kurslar burada tutulur

    
    def add_course(self,course): #Eğitmenin yeni bir kurs eklemesini sağlar
        self.course.append(course)
        print(f" {course.title} kursu eklendi")

    
class Course:
    def __init__(self,title,description,instructor):
        self.title=title
        self.description=description
        self.instructor=instructor
        self.lessons=[]
        self.quiz=None


    def add_lesson(self,lesson):
        self.lessons.append(lesson)

    def add_quiz(self,quiz):
        self.quiz=quiz



class Lesson:
    def __init__(self,title,content):
        self.title=title
        self.content=content



class Question:
    def __init__(self,text,choices,answer,point=1):
        self.text=text
        self.choices=choices
        self.answer=answer
        self.point=point #neden 1 var default 1 puan olsun dedik


    def check_answer(self,user_answer):
        return self.answer.lower().strip()==user_answer.lower().strip()

    def __str__(self):
        return self.text #print(question) dediğimizde sadece soru metni çıksın


class Quiz:
    def __init__(self,title,time_limit=None): #time limit opsiyonel eğitmen quize zaman koymak istiyorsa diye ekledik buraya
        self.title=title
        self.questions =[]  #Soruları tutan nesne
        self.time_limit=time_limit #saniye cinsinden 

    def add_question(self,question):
        self.questions.append(question)

    def start(self):
        #Quizi başlatan yer

        score=0
        total_possible=0 #Maksimum alınabilecek puan diyoruz yani doğur cevap arttıkca artıcak benim puanımda


        print(f" \n Quiz : {self.title}")
        print("----------------")

        quiz_end=None #Başlangıçta tanımlıyoruz 
        quiz_start=time.time() #Quiz başladığı an 
        for i,q in enumerate(self.questions,1):#enumerate sayesinde hem indeks hem öge yani soru numarası ve soruyu aynı anda dönüyoruz
            now=time.time() #şuanki zamanı alıyor
            elapsed=now-quiz_start #quiz başladığından beri kaç saniye geçtiğini hespalar

            #Süre doldu mu dolmadı mı ?
            if self.time_limit and elapsed > self.time_limit:
                print("Süren doldu")
                break

            print(f"\n Soru : {i} : {q.text}")
            for option in q.choices:
                print(f" - {option}")

            start_time=time.time() #Cevabı vereceği zaman zaman sayacını başlatıyorum

            answer=input("Lütfen cevabınızı Giriniz ! ")

            end_time=time.time() #Cevabı aldık sayaç duracak artık

            #süreyi hesaplıyorum
            duration=round(end_time-start_time,2) #2.ci parametre virgülden sonra kaç basamak yazılacağını belirtiyor


            print(f" Geçen Süre : {duration}")


            if q.check_answer(answer):
                print("Doğru")
                score +=q.point


            else:
                print(f" Maalesef Yanloş Cevap.\n Doğru Cevap {q.answer}")

            total_possible +=q.point

        if not quiz_end:
            quiz_end=time.time()

        total_elapsed=round(quiz_end-quiz_start,2)
        print(f"Toplam Süre : {total_elapsed}")
        print(f" Quiz Bitti toplam puan {score}/{total_possible}")


        percentage=(score/total_possible)*100

        if percentage >=60:
            print(f"Tebrikler ! Başarı Oranı : %{round(percentage,2)} => GEÇTİN")
        else:
            print(f" Maalesef ! .. Başarı Oranı %{round(percentage,2)} => KALDIN")
        return score


# 🔹 Her şeyin test edildiği bölüm
def main():
        # Eğitmenler
    instructor1 = Instructor("MineG", "mine@egitim.com")
    instructor2 = Instructor("HalilB", "halil@tech.com")

    # Kurslar
    course1 = Course("Python 101", "Giriş seviyesinde Python kursu", instructor1)
    course2 = Course("Veritabanı Giriş", "SQL ve veri sorgulama teknikleri", instructor2)

    instructor1.add_course(course1)
    instructor2.add_course(course2)

    #  Dersler
    course1.add_lesson(Lesson("Değişkenler", "Python'da değişken tanımlama..."))
    course1.add_lesson(Lesson("Koşullar", "if-else blokları..."))
    course2.add_lesson(Lesson("SELECT Komutu", "Veri seçme işlemleri..."))
    course2.add_lesson(Lesson("JOIN'ler", "Tabloları birleştirme..."))

    #  Quizler
    quiz1 = Quiz("Python Quiz", time_limit=60)
    quiz1.add_question(Question("Python'da hangi veri tipi doğrudur?", ["list", "var", "array"], "list", point=3))
    quiz1.add_question(Question("Python'da döngü hangisidir?", ["loop", "for", "circle"], "for", point=4))
    course1.add_quiz(quiz1)

    quiz2 = Quiz("SQL Quiz", time_limit=90)
    quiz2.add_question(Question("Veri çekmek için hangi SQL komutu kullanılır?", ["SELECT", "PULL", "GET"], "SELECT", point=5))
    quiz2.add_question(Question("JOIN ne işe yarar?", ["Tabloları birleştirir", "Verileri siler", "Kayıt ekler"], "Tabloları birleştirir", point=5))
    course2.add_quiz(quiz2)

    # 👩‍🎓 Öğrenciler
    student1 = Student("Sude", "sude@ornek.com")
    student2 = Student("Elif", "elif@code.com")

    # 👩‍🎓 Öğrenciler kurslara kayıt oluyor
    student1.enroll(course1)
    student1.enroll(course2)
    student2.enroll(course2)

    #  Öğrenciler quiz çözmeye başlıyor
    student1.solve_quiz(course1)
    student2.solve_quiz(course2)


# Çalıştırmak için
if __name__ == "__main__":
     #bu ne demek python dosyasının doğrudan mı çalıştırıldığını yoksa başka bir dosta tarafından iç içe mi aktarıldığını (import) kontrol eder
    main()
