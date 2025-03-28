#neden kullanıyoruz
#bir fonksiyona bir özellik istediğimiz aman kullanıyoru
#bir özelliği birkaç yerde kullanmak istiyorsak
#DAHA AZ KOD YAZMAK

def my_decorator(func):
    def wrapper():
        print("Fonkisyondan önce olan işlemler...")
        func()
        print("Fonksiyondan sonraki işlemler...")

    return wrapper

#Özellik eklemek istediğim fonksiyonlar
@my_decorator #say helloyu decorator'e gönderiyor
def sayHello():
    print("hello")

def sayGreeting():
    print("Greeting")

'''
sayHello=my_decorator(sayHello)
sayHello()
sayGreeting=my_decorator(sayGreeting)
sayGreeting()'''
sayHello()

#sayHellonun içerisne parametre atıcaksam öncelikle wwapperin içindeki çğarıdığım decoratör 'ün içindeki funsitonun içine atıcam parametreyi

import time #iki fonksiyonun ne kadar sürede çalıştığını görmekm istiyorum

import math

def calculate_time(func):
    def wrapper(*args,**kwargs):



        start=time.time()#şimdiki saniye bilgisi
        time.sleep(1)  #fonksiyonu 1 saniye uyutuyoruz
        func(*args,**kwargs)
        finish=time.time()
        print(" fonksiyon "+func.__name__+str(finish-start)+"saniye sürdü")
    return wrapper
@calculate_time
def usalma(a,b):
   

    print(math.pow(a,b))
    
@calculate_time
def faktoriyel(num):
    
   
    print(math.factorial(num))
    

usalma(2,3)
faktoriyel(4)
