class FıleCannotCreate(Exception):
    pass

class KotuDosyaHatası(Exception):
    pass

class CannorReadingError(Exception):
    pass


try:


    with open("deneme2.txt","w",encoding='utf-8') as file :
        # Dosyaya yazılacak içerik
        file.write("Merhaba Sude!\n")
        file.write("Bu satır Python'un 'write' fonksiyonuyla eklendi.\n")
        file.write("Dosya işlemleri başlasın, kodlar aksın!\n")
        file.write("Okuma fonksiyonları için hazırız \n")
except FıleCannotCreate as e :
    print(f"Hata {e}")


try:
    with open("deneme2.txt","r+",encoding='utf-8') as file :#burada 3+ hem okuma hem yazma modunu temsil ediyor
       #burada merhaba sudenin üzerine deneme yazdıgımız için denemeyi yazdı kalanını doldurdu bu metod üzerine yazıyor eklemiyor eklemek istriyorsak append a+ kullanarak yazabiliriz

       file.write("deneme \n")
       file.seek(0) #Yazdıktan sonra başa al
       print(file.read())


       
       

except CannorReadingError as err:
    print(f"Hata {err}")



try:
    with open("deneme2.txt","r+",encoding='utf-8') as file :#burada 3+ hem okuma hem yazma modunu temsil ediyor
       #burada merhaba sudenin üzerine deneme yazdıgımız için denemeyi yazdı kalanını doldurdu bu metod üzerine yazıyor eklemiyor eklemek istriyorsak append a+ kullanarak yazabiliriz
       
      # file.write("deneme \n")
      # file.seek(0) #Yazdıktan sonra başa al
       print(file.read())


       #Sayfa sonunda güncelleme

    with open("deneme2.txt","a+",encoding='utf-8') as file:
        file.write("Bu da sonradan eklendi!\n")
        file.seek(0)
        print(file.read())
       

except CannorReadingError as err:
    print(f"Hata {err}")
