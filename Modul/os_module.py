import os #İşletim sistemiyle alakalı bilgileri sunar bize Ya da dosyalarla alakalı işlemler

result=dir(os)
print(result)

result=os.name #nt demek windows kullanıyorsun demek
print(result)

''' Klasör / Dizin Değiştirme
#os.chdir('C:\\')
os.chdir('..')
os.chdir('..')
#Klasör Oluşturma 
#os.mkdir("newdirectory")#aynı dizin içinde oluşturdum
#Etkin Dizin Öğrenme 
result=os.getcwd() #dosyanın olduğu konum

print(result)
'''
#İçine klasör oluşturma
#os.makedirs("newdirectory/yeniklasör")
#os.rename("newdirectory","yeniklasör") #klaör adı değiştiriceksek eğer
#os.rmdir("newdirectory") #klaösr silme
#Listeleme

#result=os.listdir()
#print(result)

#Filtreleme işlemi nasıl olucak peki
import datetime
for dosya in os.listdir():
    if dosya.endswith('.py'):

        print(dosya)

#result=os.stat("os_module.py")
#result=datetime.datetime.fromtimestamp(result.st_atime) #dosyanın oluşturulma tarihi
#result=datetime.datetime.fromtimestamp(result.st_atime) #acces time son erilişme tarihi
#result=datetime.datetime.fromtimestamp(result.st_mtime) #modifyden geliyor değiştirilme tarihi
#print(result)

#os.system("notepad.exe") #bu metodla istediğimiz bir programı çalıştırabiliriz


#path
#uzantılar üzerinde işlem yapıyor

result=os.path.abspath("dosya adı") #tam konumunu verir

#dosya yolunu öğrenmek  istiyorum ama dosya yolunu bilmiyorsam
result=os.path.dirname(os.path.abspath("dosya ismi"))

result=os.path.exists("dosya adı") #aradığım konumda bu dosya var mı
print(result)

#ulaştığımız alan klasör mü dosya mı 
result=os.path.isdir("dosya adı")
result=os.path.isfile("dosya adı ") #ulaştığımız alan dosya mı

#path bilgilerini birleştirmek istiyorsak
result=os.path.join("C:\\","deneme","deneme1")
print(result)


#path bilgilerini bölmek istiyorsak
result=os.path.split("C:\\")
print(result)

#dosyanın ismi ile uzantısını ayıran metod
result=os.path.splitext("dosya adı")
print(result)
