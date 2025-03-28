'''
Bu sistem şunları yapacak:
 Yeni sipariş ekleyebiliriz.
 Siparişleri dosyaya kaydedeceğiz ve okuyabileceğiz.
 Sipariş toplam tutarını hesaplayacağız.
 Siparişleri süsleyen bir dekorator kullanacağız (loglama gibi).
 Hata kontrolü olacak (negatif fiyatlı ürün eklenirse hata verecek).'''

import time
import os 

#Hata sınıflarım(özel ben oluşturuyorum)

class SiparisbulunamadıHatasi(Exception):
    pass

class GecersizTutarHatasi(Exception):
    pass

#Decorator: Sipariş işlemlerini logloyan fonsksiyon

def siparis_logger(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        print(f"{func.__name__} fonskiyonu çalıştırılıyor..")
        result=func(*args,**kwargs)
        end_time=time.time()
        print(f"{func.__name__} Tamamlandı.İşlem süresi : {end_time-start_time} saniye")
        return result
    return wrapper

#Sipariş Sını 

class Siparis:
    def __init__(self,siparis_no,musteri_ad,urun_listesi,kargo_ucreti=20):
        """
        Sipariş nesnesi oluşturur.
        :param siparis_no: int - Sipariş numarası
        :param musteri_ad: str - Müşteri ismi
        :param urun_listesi: list - [(Ürün adı, fiyat), ...] şeklinde ürün listesi
        :param kargo_ucreti: int - Kargo ücreti (default: 20 TL)
        """
        #Sipariş nesnesini oluşturuyorum
        self.siparis_no=siparis_no
        self.musteri_ad=musteri_ad
        self.urun_listesi=urun_listesi
        self.kargo_ucreti=kargo_ucreti
        self.toplam_tutar=self.siparis_tutar_hesapla()


    def siparis_tutar_hesapla(self):
        """Ürünlerin toplam tutarını hesaplar ve kargo ücretini ekler."""
        toplam_urun_fiyat=sum([fiyat for _,fiyat in self.urun_listesi])
        toplam_tutar=toplam_urun_fiyat+int(self.kargo_ucreti)
        if toplam_tutar < 0:
            raise GecersizTutarHatasi("Sipariş tutarı negatif olamaz !")

        return toplam_tutar

    def siparis_bilgisi(self):
        """Siparişin detaylarını string olarak döndürür"""
        urunler_str = ", ".join([f'{urun} ({fiyat} TL.)' for urun, fiyat in self.urun_listesi])

        return f" Sipariş no {self.siparis_no} | Müşteri {self.musteri_ad}| Ürünler : {urunler_str} | Toplam : {self.toplam_tutar}  Türk Lirası"


#Sipariş yönetim sistemi(Dosya İşlemleri)
class SiparisYönetim:
    DOSYA_ADI="musteri_siparişleri.txt" #constant değişmez
    def __init__(self):
        #Dosy avarsa yükle yoksa yenisini oluştur!
        if not os.path.exists(self.DOSYA_ADI):
            with open(self.DOSYA_ADI,"w",encoding="utf-8") as file :
                file.write("")

    @siparis_logger #Decorator
    def siparis_ekle(self,siparis:Siparis):
        #"Siparişi Dosyaya kaydediyor."
        with open(self.DOSYA_ADI,"a",encoding="utf-8") as file:
            file.write(f"{siparis.siparis_no},{siparis.musteri_ad},{siparis.toplam_tutar}\n")


    def siparis_oku(self,siparis_no):
        #dosyadan siparişi oku ve bulmazsa hata tükür
        with open(self.DOSYA_ADI,"r",encoding="utf-8") as file:
            siparisler=file.readlines()

        for siparis in siparisler:
            no,musteri,toplam=siparis.strip().split(",")
            if int(no)==siparis_no:
                print("\033[32m Sipariş başarıyla getirildi!\033[0m")
                print("\033[34m Log:Sipariş Başarıyla Çekildi.\033[0m")

                with open("log.txt","a",encoding="utf-8") as log_file:
                    log_file.write(f"Sipariş no :{no} | Müşteri : {musteri} |Toplam: {toplam} TL\n")
                    log_file.write("Log: Sipariş Bilgisi dosyaya kaydedildi")
                
                return f"Sipariş no :{no} | Müşteri : {musteri} |Toplam: {toplam} TL"
        
        print("\033[31m Hata: Sipariş bulunamadı!\033[0m")  
        raise SiparisbulunamadıHatasi(f"\033[31m Sipariş No {siparis_no} bulunamadı!") #burada çünkü tüm siparişlere bakması lazım

    #  **Test Senaryosu (Gerçek Kullanım)**
def main():
    yonetim = SiparisYönetim()

    #  **Siparişleri Oluştur**
    siparisler = [
        Siparis(101, "Ahmet Kaya", [("Laptop", 15000), ("Mouse", 300)]),
        Siparis(102, "Sude Girişimci", [("Telefon", 18000), ("Kılıf", 200)]),
        Siparis(103, "Halil İşletmeci", [("Tablet", 10000), ("Kalem", 500), ("Çanta", 750)]),
        Siparis(104, "Mine Yazılımcı", [("Kulaklık", 1200), ("Mikrofon", 1500)]),
    ]

    #  **Siparişleri Dosyaya Kaydet**
    for siparis in siparisler:
        yonetim.siparis_ekle(siparis)

    print("\n **TÜM SİPARİŞLER KAYDEDİLDİ!** \n")

    #  **Siparişleri Tek Tek Okuyalım**
    for sip_no in [101, 102, 103, 104, 999]:  # 999 siparişi yok, hata verecek
        try:
            print(yonetim.siparis_oku(sip_no))
        except SiparisbulunamadıHatasi as e :

            print(f"Hata: {e}")

if __name__ == "__main__":

    main()
