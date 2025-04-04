# LIMONOMI: Fiyat Tarama Sistemi

## Iterator, Generator, OOP, File Handling ve Error Management öğelerini bir arada kullanıyoruz

import os
import datetime

#Hata sınıfı

class FiyatVerisiEksikHatasi(Exception):
    pass


#Limon Verisi Yönetim sınıfı

class LimonVerisiYönetimi:

    LOG_DOSYASI="limon_log.txt"
    def __init__(self,fiyatlar):
        if not fiyatlar:
            raise FiyatVerisiEksikHatasi("Fiyat listesi boş")
        
        self.fiyatlar=fiyatlar

    
    def log_yaz(self,mesaj):
        with open(self.LOG_DOSYASI,"a",encoding="utf-8") as log:
            tarih=datetime.datetime.now().strftime("%Y-%m-%d %H:%M-%S")
            log.write(f"[{tarih}] {mesaj} \n")

        
    
    def iterator_ile_tarama(self):
        class LimonFiyatIterator:
            def __init__(self,fiyat_listesi):
                self.fiyat_listesi=fiyat_listesi
                self.index=0

            def __iter__(self):
                return self

            def __next__(self):

                if self.index < len(self.fiyat_listesi):

                    fiyat=self.fiyat_listesi[self.index]
                    self.index +=1
                    return f" Limon fiyatı {fiyat} TL"

                else :
                    raise StopIteration

            
        print("*******ITERATOR İLE TARAMA*******    ")
        for  bilgi in LimonFiyatIterator(self.fiyatlar):
            print(bilgi)


    def generator_ile_alarm_tarama(self):
        print("\n--- GENERATOR ile Alarm Tarama ---")
        kriz_sayacı=0

        def fiyat_generator():
            for fiyat in self.fiyatlar:
                if fiyat >34:
                    yield f"Dikkat Fiyat Çok yüksek {fiyat}"

                else:
                    yield f" Limon {fiyat} T"

        for veri in fiyat_generator():
            print(veri)
            self.log_yaz(veri)
            if "Dikkat" in veri :
                kriz_sayacı +=1

                if kriz_sayacı >=3:
                    kriz_mesajı="\U0001f6a8 KRİZ ALARMI: Art arda 3 gün fiyatta patlama!"
                    print(kriz_mesajı)
                    self.log_yaz(kriz_mesajı)
                    break

                else:
                    kriz_sayacı=0

try:
    fiyatlar = [30, 36, 37, 38, 31, 29]
    sistem = LimonVerisiYönetimi(fiyatlar)
    sistem.iterator_ile_tarama()
    sistem.generator_ile_alarm_tarama()
except FiyatVerisiEksikHatasi as e:
    print(f"HATA: {e}")
    with open("limon_log.txt", "a", encoding="utf-8") as log:
        log.write(f"[HATA] {e}\n")
