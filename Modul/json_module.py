#Veri iletişimi için gerekli çok kullanılıyoe veri alışverişinde

#Json'a yazmak json.dump(data,file) Python objesini dosyaya yazar
#--> SON'a yazmak	json.dump(data, file)	json.dump(list, file)
'''
            with open("users.json", "w") as file:
                 json.dump(list, file) '''

#Json'dan okumak json.load(file) Json dosyasıbı pythona çevirir

#--->>JSON'dan okumak	json.load(file)	users = json.load(file)
'''
with open("users.json", "r") as file:
    users = json.load(file)
'''

#Stringden jsona json.loads(string) json stringini dict yapar

#--->>String’ten JSON’a	json.loads(string)	user = json.loads(user)

#Jsondan stringe json.dumps(dict) dict'i json string yapar 

#-->>JSON’dan string’e	json.dumps(dict)	json.dumps(user.__dict__)

#Mimari Harita 
'''
Kullanıcı       → input()                         
↓
Veri kontrolü   → kullanici_kontrol()             
↓
Kullanıcı modeli → User                           
↓
Veri yönetimi   → UserRepository (register, login)
↓
Kalıcı kayıt    → json.dump / json.load           
         
'''

import time 
import re
import getpass
import json
import os

def kullanıcı_kontrol(username,password,email):
    password=password.strip()
    if len(username)<3 or not username.isalnum():
        print("Kullanıcı adı en az 3 karakter olmalı ve sadece harf/rakam içermelidir")
        return False
    
    if (len(password)) < 8:
       raise Exception("Şifre en az 8 karakterli olmalı")
    elif not re.search("[a-z]",password): 
        raise Exception("Parola küçük harf içermelidir")
    elif not re.search("[a-z]",password):
        raise Exception("Parola küçük harf içermelidir")
        
    elif not re.search("[A-Z]",password):
        raise Exception("Parola büyük harf içermelidir")
    elif not re.search("[0-9]",password):
        raise Exception("Parola rakam harf içermelidir")
    elif not re.search(r"[!@#$%^&*()_+=\-{}\[\]:;\"'<>,.?/~`]",password):
        raise Exception("Parola alpha numeric karakter  içermelidir")


        
    else:
        print("Geçerli Parola")
    
    email_pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(email_pattern,email):
        print("Geçerisz e-posta adresi formatı")
        return False
    
    print("Tüm Bilgiler Uygun Kayıt işlemine Geçilebilir")
    return True
        

class User:
    def __init__(self,username,password,email):
        self.username=username
        self.password=password
        self.email=email   

class UserRepository:
    def __init__(self):
        self.users=[]
        self.isLoggedIn=False
        self.currentUser={}

        #load user from .json file
        self.loadUserS() #bu metodu UserRepository oluşturulduğu anda çağır .Json dosyasından kullanıcıları  çeker


    def loadUserS(self):
        if os.path.exists('user.json'):#Dosya varsa açar içinden kullanıcıları okur
            with open("users.json","r",encoding="utf-8") as file:
                for user in users:
                    user=json.loads(user)#Liste içindeki userı usera dönüştürücem
                    newUser=User(username=user['username'],password=user['password'],email=user['email'])
                    self.users.append(newUser)
              
        print(self.users)
    
    def register(self,user:User):
        for user in self.users:
            if user.email==email:
                print("Bu Email Zaten kayıtlı")
            
                return
        yeni_user=User(username,password,email)
        self.users.append(yeni_user)
        #self.savetoFile() #bir kayıt işkemi yaptıgımızda bütün listeyi vburaya atıcaz

        print("Kayıt Başarıyla Tamamlandı")
        self.savetoFile()
        time.sleep(1)
        
    def login(self,email,password):
        if self.isLoggedIn:
            print('Zatan Giriş Yapılmış')
        else:

            for user in self.users:
                if user.email==email and user.password==password:
                    printf(f" Giriş Başarılı.Hoşgeldin {username}")
                    isLoggedIn=True
                    self.currentUser=user
                    return True
                print("Email veya şifre hatalı")
                return False


    def logout(self):
        self.isLoggedIn=False
        self.currentUser={}
        print("Çıkış Yapıldı...")


    def identity(self):
        if self.isLoggedIn:
            print(f"username : {self.currentUser.username}")
        
        else:
            print("Giriş Yapılmadı")


    def savetoFile(self):
        #her classas tek tek oluşup o classı dict yapısına çeviriyorum
        list=[]
        for user in self.users:
            list.append(json.dumps(user.__dict__)) #bu metod user classını tamamen sözlük yapısına çeviriyor
        with open('users.json','w',encoding='utf-8') as file:
            #json.dump(self.users) #objeyi kayıt edilebilir şeye çevirir
            json.dump(list,file) #dump'ın içine direkt class bilgisi atamadığımız için önce oluşturduğumuz class bilgisini bir sözlük yapısına çeviricez

    
        

repo=UserRepository()


while True:
    print('MENÜ'.center(50,'*'))
    secim=input('1-Register\n 2- Login\n 3-Logout \n 4- Identity\n 5-Exit\n Seçiminiz :')
    if secim=='5':
        break
    else:
        if secim=='1':
             #register
             username=input("Kullanıcı Adı :").strip()
             password = input("Şifre : ").strip()
             email=input('Email :').strip()
             user=User(username=username,password=password,email=email)
             if kullanıcı_kontrol(username,password,email):
                print(f"Kayıt Başarılıyla Yapılıyor... {username}")
                time.sleep(2)
                repo.register(user)
                time.sleep(1)
                print(f"Kaydınız Başarılı Bir Şekilde  yapıldı {email} \t {username}")
             else:

                print("Bilgiler Uygun Değil tekrardan deneyiniz..")

             
             
        elif secim=='2':
            #login
            email=input('Email :')
            password=input("Şifre : ")
            if repo.login(email,password):
                time.sleep(1)
                print("Sisteme Giriş yapıldı")
            else:
                print("Giriş Başarısız Email ya da Şifre Hatalı")
        elif secim=='3':
            repo.logout()
            
        elif secim=='4':
            #identity display username
            repo.identity()
            
        else:
            print("Yanlış seçim")
