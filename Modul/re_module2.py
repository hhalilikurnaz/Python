#Regular Expression

import re
#Genel olarak bize arama sonucunda sonuç döndürür 
#arama kriterlerini re ile geliştirebiliyoruz
#sadece pythona özel bir ifade değil
# re module 

result=dir(re)
print(result)

#re module

str='Halil Çok Yakışıklı:Gereğinden Fazla Yakışıklı | 40 cm'
#re.findall() 
result=re.findall("Halil",str)
print(result)

#re.split()
result=re.split(":",str)
print(result)

#re.sub() substring
result=re.sub(" ","/",str)
print(result)
'''
#re.search()
result=re.search('Yakışıklı',str)
print(result)
result=result.span() #konumunu aldık
print(result)
result=result.start()
print(result)
result=result.end()
print(result)
result=result.group()
print(result)
'''
result=re.findall("[^0-9]",str) #rakam haricindeki bütün karakterleri bize buluyor
print(result)

# . - Her hangi bir tek karakteri belirtir
#.. - Her hangi bir çift karakteri belirtir

result=re.findall("...",str)
print(result)

#^ - Beliritlen karakterle başlıyor mu
# ^a -A ile başlıyor mu

result=re.findall("^a",str)
print(result)

#$ belirtilen karakterle bitiyor mu
result=re.findall("p$",str)
print(result)

#bir karakterin sıfır ya da daha fazla sayıda olmasını kontrol eder

result=re.findall("Hali*l",str)
print(result)

# + - Bir karakterin bir ya da daha fazla sayıda olmasını kontrol eder
result=re.findall("Hali+l",str)
print(result)

#? -  0 ya da 1 kez tekrarlamasını kontrol eder
result=re.findall("Sud?",str)
print(result)

# {} karakter sayısını ifade eder
result=re.findall("aa{2}",str) # a karakterinin arkasına a karakteri 2 kez tekrarlanmalı
print(result)
result=re.findall("alil{1,2}",str)
print(result)

# | or işareti alternatif seçeneklerden birinin gerçekleşmesi gerekir

result=re.findall("Halil|Yakılışlı",str)
print(result)


#() gruplamak için kullanılır
result=re.findall("(h|a|l)il",str)
print(result)

#(a|b|c)xz=> a,b,c karakterlrinin arkasına xz gelmelidir


# \- Özel karakterleri aramamızı sağlar
#\$a => $ karakterinin arkasına a karakterini arar.Yani $re exp. engine tarafından yorumlanmazSsd

#\ Özel karakter
result=re.findall("\AHalil",str) #verilen karakter kelimenin en başında mı
print(result)
result=re.findall("Halil\Z",str)
print(result)

str='Halil Çok Yakışıklı:Gereğinden Fazla Yakışıklı | 40 cm'
#veerilen karakter kelimenin en başında mı yoksa sonunda mı
result=re.findall(r"\bHalil",str) #basşında mı
print(result)
result=re.findall(r"cm\b",str) #sonunda mı
print(result)
#\B başta ya da sonra \B olursa başta değil mi sonda değil mi
#\d 0-9 arası rakam gönderiyor bakıyor içindemi diye
#\D değil mi rakam içermiyor mu 
#\s boşluk karakteri arar
#\S Boşluk karakteri dışında arıyorsak
#w alfabatik karakterler,rakamlar ve alt çizgi karakterleri.
