def not_hesapla(satir):
    satir = satir[:-1]  # sondaki \n silinir
    liste1 = satir.split(":")
    ogrenciAdi = liste1[0]
    liste = liste1[1].split(',')

    print(liste[0])
    print(liste[1])
    print(liste[2])

    not1 = int(liste[0])
    not2 = int(liste[1])
    not3 = int(liste[2])

    ortalama = (not1 + not2 + not3) / 3

    


    if ortalama >=90 and ortalama <=100:
        harf='AA'
    elif ortalama >=85 and ortalama<=89:
        harf='BA'
    elif ortalama >=70 and ortalama<=84:
        harf='BB'
    elif ortalama >=60 and ortalama<=69:
        harf='CB'
    elif ortalama >=45 and ortalama<=60:
        harf='CC'
    else:
        harf='DD'

    return ogrenciAdi + ': ' + harf + '\n'


def notları_oku():

    with open("sinav_notları.txt","r",encoding='utf-8') as file:
        for satir in file:
            print(not_hesapla(satir))

def notları_gir():
    ad=input("Öğrenci Adı :")
    soyad=input("Öğrenci Soyadı :")
    not1=int(input("Notunuzu Giriniz :"))
    not2=int(input("Notunuzu Giriniz :"))
    not3=int(input("Notunuzu Giriniz :"))



    with open("sinav_notları.txt","a",encoding="utf-8") as file:
        file.write(ad+ '' + soyad + ':'+str(not1)+','+','+str(not2)+','+str(not3)+'\n')

def notları_kaydet():
    with open('sinav_notları.txt','r',encoding='utf-8') as file :

        for i in file :
            liste.append(not_hesapla(i))

    
    with open('sonuclar.txt','w',encoding='utf-8') as file2 :
        for i in liste:
            file2.write(i)





def exit():
    pass





while True:
    print(".... Hoşgeldiniz.....")
    print("1-Notları oku \n 2-Notu Gir \n 3-Notları Kayıt Edin \n 4-Çıkış")
    işlem = input("Lütfen Seçiminizi Giriniz !")

    match işlem:
        case "1":
            print("Notları Oku")
            notları_oku()
            

        case "2":
            print("Not Gir")
            notları_gir()
            

        case "3":
            print("Notları Kaydet Edin")
            notları_kaydet()
            

       
            

        case "4":
            print("Çıkış Yapılıyor...")
            exit()
            break


        case _:
            print("Geçersiz işlem yaptınız !")

