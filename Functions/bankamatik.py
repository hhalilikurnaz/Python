#Bankamatik uygulaması
hesapA={
    'ad':'Halil İbrahim ',
    'soyad':'Kurnaz',
    'bakiye':3000,
    'ek hesap':6000,
    'hesap no':'145689'
}

hesapB={
    'ad': 'Sude',
    'soyad': 'Yıldız',
    'bakiye': 1500,
    'ek hesap': 3500,
    'hesap no':'145697'
}

hesapC={
    'ad': 'Ece',
    'soyad': 'Demir',
    'bakiye': 4200,
    'ek hesap': 2000,
    'hesap no':'145698'


}

hesapD={
    'ad': 'Ayşe',
    'soyad': 'Güneş',
    'bakiye': 2750,
    'ek hesap': 2250,
    'hesap no':'145699'

}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye']>= miktar):
        hesap['bakiye']-=miktar
        print('Paranızı Alabilirsiniz!')
    else:
        toplam=hesap['bakiye']+hesap['ek hesap']
        print(f"Bakiyeniz Yetersiz.İsterseniz  Ek hesap bakiyenizden kullanablirsiniz.\n Ek hesap bakiyeniz {hesap['ek hesap']}.Toplam bakiyeniz {toplam}\n Ek Hesap Bakiyenizi Kullanmak İstiyorsanız Lütfen 0' Basınız")
        secim=int(input('Lütfen Bir Seçim yapınız:'))
        if(secim==0):
            if(toplam>=miktar):
                bakiye=hesap['bakiye']
                ekhesapKullanılacakMiktar=miktar-bakiye
                hesap['bakiye']=0
                hesap['ek hesap'] -= ekhesapKullanılacakMiktar
                print(f"Paranızı alabilirsiniz.\n Kalan Bakiyeniz toplam {(toplam-miktar)}")
            else:
                print(f"{hesap['hesap no']}  \t nolu hesabınızda {hesap['bakiye']} bulunmaktadır")
        else:
            print('Üzgünüz Bakiyeniz Yetersiz!')

    
def bakiyeSorgula(hesap):
    print(f" {hesap['hesap no']} nolu hesabınızda {hesap['bakiye']} TL Bulunmaktadır.Ek Hesabınızda ise {hesap['ek hesap']}tL Bulunmaktadır")

paraCek(hesapA,4000)
paraCek(hesapA,1000)
bakiyeSorgula(hesapA)
