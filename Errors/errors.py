#error => hata

#error handling=> hata yönetimi

print(a)# =>#Name Error
print('1a2')# =>Value Error
print(10/0)#>>ZeroDivisionError
print('denem'e) #>>Syntax Error
'''

x=int(input(' x : '))
y=int(input('y : '))
'''



while True :

    try:

        x=int(input(' x : '))
        y=int(input('y : '))
        print(x/y)
    except Exception as ex:
        print('Hatalı Bir Tuşlama Yaptınız  \n Hata adı :',ex)  #Hatalı Mesajın Özetini Girdiniz !

    else:
        print('Her Şey Yolunda')
        break
    finally :
        print('Try except Sonlandı ...')
       


x=10
if x>5:
    raise Exception("x 5'ten büyük değer alamaz!")
    


def check_password(psw):
    import re #regular expression su olsun bu olsun sunu içermesin falan diye kontrol ediyorum
    if len(psw) <8:
        raise Exception('Parola en az 7 karakter olmalıdır')

    elif not re.search("[a-z]",psw): #
        raise Exception("Parola küçük harf içermelidir")
    elif not re.search("[a-z]",psw):
        raise Exception("Parola küçük harf içermelidir")
        
    elif not re.search("[A-Z]",psw):
        raise Exception("Parola büyük harf içermelidir")
    elif not re.search("[0-9]",psw):
        raise Exception("Parola rakam harf içermelidir")
    elif not re.search("[_@$]",psw):
        raise Exception("Parola alpha numeric karakter  içermelidir")

    elif not re.search("\s",psw):
        raise Exception("Parola boşluk içermemelidir!")

    else:
        print("Geçerli Parola")


password="12345678"

try:
    check_password(password)

except Exception as e:
    print(e)
else:
    print("Geçerli Parola")

finally:
    print("Validation Tamamlandı")
    


class Person:
    def __init__(self,name,year):
        if (len(name))>10:
            raise Exception("Name alanı fazla karakter içeriyor")
        else:
            self.name=name
