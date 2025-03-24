#inheritance(Kalıtım) demek : Miras alma

#Person => nameilastname,age,eat(),run(),drink()
#Student,Teacher sınıfları oluşturcak olsam persondaki herşeyin içinde olmasını istesem napıcam
#Student(Person),Teacher(Person) olarak algılanacak

#Animal=> DOg(),Cat()



class Person():

    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

        print('Person Created1')


    def who_am_i(self):
        print('I am '+self.fname+self.lname)


class Student(Person):#Personun sahip olduğu bütün özellikler artık burada da var
    def __init__(self,fname,lname,number):
        Person.__init__(self,fname,lname)#Neden bunuda çağırdık çünkü personun özellikleri olabilir ve student bunlar miras alabilir
        print('Student Created')
        self.number=number
    def who_am_i(self): #Override
        print('I am a Student')


class Teacher(Person):
    def __init__(self,fname,lname,branş):
        super().__init__(fname,lname)#Bu daha kullanıslı hem de self parametresinden kurtulmus olduk
        self.branş=branş



    def who_am_i(self):
        print(f" {self.fname} {self.lname} {self.branş} Öğretmeniyim")


p1=Person('Sude','Kurnaz')

s1=Student('Halil','Kurnaz',151)

print(f"{s1.fname} {s1.lname} {p1.fname} {p1.lname} ' ı Seviyor ")

p1.who_am_i()
s1.who_am_i()
t1=Teacher('Halil','Özübek','Kimya')
t1.who_am_i()



myList=[1,2,3]
myString='Halil Sudeyi Seviyor'
print(len(myList))
print(len(myString))
print(type(myList))
print(type(myString))

class Movie():
    def __init__(self,title,director,duration):
        self.title=title
        self.director=director
        self.duration=duration
        print('Movie objesi oluşturuldu')

    def __str__(self):
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duration


    def __del__(self):
        print('Film Silindi!')



n=Movie('film adı','yönetmen adı',120)


print(str(myList))
print(str(n))

print(len(myList))
print(len(n)) #len metodunuda ben ekledim classa

#Dahada fazla özel metod pythonun kendi sitesinde mevcut bakıp kullanabiliyorum
