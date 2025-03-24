liste=['1','2','5a','10b','abc','10','50']

#1: Liste elemanları içindeki sayısal değerleri bulunuz.

for x in liste:
    try:


        result=int(x)
        print(result)
    except ValueError:
        continue

#mantık şu 1 ve 2 yazdırcak ama 5a yı 10 b yi yazdıramayacğaı için devam edicek abc de yazdıramıcak 10 ve sonra 50 yazdıracak


#2:Kullanıcı 'q' değerini girmedikçe aldığınız her inputun sayı olduguna emin oldugundan emin olun aksi takdirde hata mesajı yazınız

while True:
    sayi=input('Sayı:')
    if(sayi=='q'):
        break
    
    

    try:
        result=float(sayi)
        print('Girdiğiniz Sayı : ',result)
        break
    except ValueError:
        print('Geçersiz Sayı')
        continue

#3:Girilen paralo içinde türkçe karakter hatası veriniz 


turkce_karakterler='şçğüöıİ'
def checkPassword(parola):

    for i in parola:


        if i in turkce_karakterler:
            raise TypeError('Parola Türkçe Karakterler İçeremez')
        else:
            pass
    print('geçerli Parola')

parola=input('Parola')

try:
    checkPassword(parola)
except TypeError as err:
    print(err)

#3 Faktöriyel fonkisiyonu oluşturup fonksiyona gelen değerler için hata mesajları verin.

def faktoriyel(x):
    x=int(x)

    if x<0:
        raise ValueError('Negatif Değer')
    

    result=1


    for i in range(1,x+1):
        result *=i
    
    return result


for x in [5,10,20,-3,'10a']:
    try:
        y=faktoriyel(x)

    except ValueError as err:
        print(err)
        continue

    print(y)
