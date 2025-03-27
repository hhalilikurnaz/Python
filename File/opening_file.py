#dosya açmak veya oluşturmak için open() fonkisyonu kullanılır.
#Kullanımı : open(dosya_adi,dosya_erişme_modu)
#dosya_erişme_moud => Dosyayı hangi amaçla açtığımızı belirtir

#"w"(Write) yazma modu.Dosyayı konumda oluşturur >>Dosyayam bilgi eklicez-- Son eklediğimiz bilgi yer alır

file=open("newfile.txt","w") #dosya  var olan dizinin içinde olması gerekiyor yoksa  hata alıyoruız 
file.close()

#  *** Dosya konumunu oluşturur
#**** ,Mevcut içerik varsa siler üzerine yazar

file=open("C:/Users/hibra/OneDrive/Masaüstü/pythonfile.txt","w",encoding='utf-8') #bu  türkçe karakterleri tanıması için yazılımıs bir encoding
file.write("Halil Sudeyi Seviyor")
file.close()

#"a"(Append) ekleme.Dosya konumda yoksa oluşturur --Dosya öncesinde daha önce olan veri üstüne ekleme yapıyoruz

file=open("pythonfile.txt","a",encoding='utf-8')
file.write("Halil Sudeyi SEviyorr")
file.close()
#"x"(Create) oluşturma.Dosya zaten varsa hata verir
file=open("pythonfile.txt","x",encoding='utf-8') #Dosya var hata verdi

#"r"(Read) okuma .Dosya konumda yoksa hata verir
