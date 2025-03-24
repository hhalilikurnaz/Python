


#class
#obje (instance)
import datetime


class Person:
    #attribute
    adress='No information'
    now=datetime.datetime.now()
    def __init__(self, name, year):
        # self'in anlamı: classtan türetilen herhangi bir objeyi tanımlıyor
        self.name = name
        self.year = year
        # init metodu neden constructor: oluşturulan her bir obje için mutlaka çalıştırıldığı için
        print('init metodu çalıştı')
    # instance methods
    def intro(self):#self diyerek tanımlanan objenin referansı oalrak veriyoruz
        print("Hello There!"+self.name)

    def calculateAge(self):
        yas=(self.now.year-self.year)
        print(f"Yaşınız {yas}")

# object(instance)
p1 = Person("Halil", 1990)
p2 = Person("Sude", 2003)

print(p1)
print(p2)
#accessing object attributes
print(f"name : {p1.name} year : {p1.year},adress {p1.adress}")
#Updating objects
p1.name='Ahmet'
p1.adress='İstanbul'
print(p1.name,p1.year,p1.adress)
p1.intro()
p2.intro()
p1.calculateAge()
