'''
myString='Hello'
print(type(myString))
#fonksiyonları class içine tanımlamıyoruz

def sayHello(name=' user '):
    print('Hello \t\t\n'+name)

isim=input('İsminizi Giriniz : ')
sayHello(isim)


def total(num1,num2):
    return num1+num2
sayi1=int(input('Lütfen sayı Giriniz :'))
sayi2=int(input('Lütfen sayi giriniz '))

result=total(sayi1,sayi2)
print(result)

import datetime
now = datetime.datetime.now().year  # Şu anki yıl

def yasHesapla(dogumYili):
    return now - dogumYili  # Girintileme doğru olmalı

year = int(input('Lütfen Doğum Yılınızı Giriniz: '))
result = yasHesapla(year)
print(result)
'''
'''
def changeName(n):
    n='ada'
name='yigit'
changeName(name)
print(name)

def change(n):
    n[0]='istabul'

sehirler=['ankara','izmir','mersin']
n=sehirler[:] #slicing işlemi kopyalama işlemi #: demek içindeki tüm noktalrı at demek
change(sehirler)
print(sehirler)
'''
'''
#1-2-3-4-5 tane parametre kullanıyorum mesela burada peki ya 6 parametre kullanıcaksam
def add(a,b,c=10,d=10,e=10):
    return sum((a,b,c))


print(add(10,23))

#istediğimiz kadar parametre gönderebileceğimiz şekilde oluyor.fonksiyona parametre vermek istemiyorsak eğer

def add(*params): #tupple
    return sum((params))

#fonkisyona gönderdiğim parametreler bir veri tipi olsa ve sayısı belli değilse ne yapıcam ?

'''
'''
def displayUser(**args):#gönderdiğimiz parametrelerin bir tupple değişkeni değilde dict değişkeni olmasını istediğimden iki tane ** koyuyoruz
    for key,value in args.items():
        print('{} is {}'.format(key,value))

displayUser(name='Çınar',age=2,city='İstanbul')
displayUser(name='ali',age=2,city='mersin',phone='1651656')
displayUser(name='sude',age=2,city='yozgat',phone='1651656',email='xxxx@gmail.com')
'''
'''
def myFunc(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50,key1='calu',key2='valu2')
'''

def yazdir(kelime,adet):
    print(kelime*adet)

yazdir('merhaba\n',10)
    

#Kendisine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyon

def listeyeCevir(*args):
    liste=[]
    for arg in args:
        liste.append(arg)
    return liste

result=listeyeCevir(10,20,30,40,50,'merhaba')
print(result)

#Gönderilen 2 sayı arasındaki bütün asal sayıları bulma



def asalsayılarıBul(sayi1,sayi2):
    for sayi in range(sayi1,sayi2+1):
        if sayi>1:
            for i in range(2,sayi):

                if (sayi%i==0):
                    break
            else:

                
                print(sayi)
sayi1=int(input('Sayı 1 :'))
sayi2=int(input('Sayı 2 :'))

asalsayılarıBul(sayi1,sayi2)

#kendisine gönderilen bir sayının tam bölenlerini yazdıran fonksiyon

def tamBolenler(number):
    tamBolenler=[]
    for i in range(2,number):
        if(number%i==0):
            tamBolenler.append(i)
    return tamBolenler
    

number=int(input('Lütfen Bir sayı giriniz :'))
print(tamBolenler(number))

#bu fonksiyon oluşturma şekli

def square(number):
    return number**2
#buda başka bir fonksiyon gösterme şekli
def squareAlma(number): return number**2

numbers=[1,2,3,4,5]
#map metodunda kullancak oldugumuz fonksiyonu ve içine göndereceğimiz listeyi yazıyoruz parametre olarak

result=map(square,numbers)
print(result)

#mapten dönen sonucu listeye çevirmemiz lazım ama çünkü map bir adres döndürüyor bize liste döndürmesi lazım
result=list(result)
print(result)

#peki ben mapin içine ismi olmayan bir fonksiyon tanımlayabiliyor mmuyum
#sadece bir kere kullancağoım bir işlem için lambda expression diyoruz

result=list(map(lambda num : num**2,numbers))
print(result)

#map metodu bir build in fonksiyonu pythonla birlikte geliyor bize
#dizinin elamanlarının hepsini fonkisyona gönderiyor .Bütün elemanlarıyla işlem yapıyoruz

#ben filter işlemide yapmak istiyorum mesela o zaman napcaz nasıl yapcaz

def check_even(num):
    return num%2==0
result=list(filter(check_even,numbers))
print(result)


#Tanımlamış olduğumuz değişkenlerin loca ve global olarak nasıl inceleneceğine bakıcaz

#global scope
x='global x'
def function():
    #local scope
    x='local x'
    print(x)

function()
print(x)

#Ben x'i globalken fonksiyonla değiştirdim local yaptım ama çağırdığımda ekrana gelen çıktı hala global oldugu neden değişmedi peki ?
#Çünkü fonksiyonlar yeni bir tanımla analanı kullanıyor.
#fonksiyon içinde tanımla yapmadıysam fonkisyon bir üstteki fonksiyon için global olan kapsamı kullanıyor.

###########
name='Halil' #global

def changeName(new_name):
    #local fonkisyon içinde tanımlanmış
    name=new_name
    print(name)

changeName('Sude')
print(name)

######## iç içe fonksiyonalrda ne olucak

name='global string'

def greeting():
    name='çınar'#enclosing

    def hello():
        name='Sude' #local
        print('hello\n'+name)


    hello()

greeting()


#kodlar en içten dışa doğru gider pythonda 
#en iç=local - sonra bir dışa çıkar bulamazsa enclosing-orda da bulamazsa global-orda da yoksa built in

#############
x=50
def test(x):
    global x 
    print(f"x : {x}")

    x=100
    print(f"changed x to {x}")

test()
print(x)

#fonkisyonun çalışması dışarıda tanımlanan değişenin değiştirilmesi mümkün olamuyor ama
# bunu yapabiliiz dışarıda tanımladığımız değişkeni fonksiyon içinde global .... değişken adı olarak yazar isek
