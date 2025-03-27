import os  # Dosya işlemleri için

#  Özel hata sınıfları (Custom Exceptions)
class SiparisBulunamadiHatasi(Exception):
    """Girilen sipariş numarası sistemde yoksa hata fırlatır"""
    pass

class GecersizTutarHatasi(Exception):
    """Sipariş tutarı negatif girilirse hata fırlatır"""
    pass


#  **Sipariş Sınıfı (OOP)**
class Siparis:
    def __init__(self, siparis_no, musteri_ad, urun_listesi, kargo_ucreti=20):
        """
        Sipariş oluşturur.
        :param siparis_no: int - Sipariş numarası
        :param musteri_ad: str - Müşteri ismi
        :param urun_listesi: list - [(Ürün adı, fiyat), ...] şeklinde ürün listesi
        :param kargo_ucreti: int - Kargo ücreti (default: 20 TL)
        """
        self.siparis_no = siparis_no
        self.musteri_ad = musteri_ad
        self.urun_listesi = urun_listesi
        self.kargo_ucreti = kargo_ucreti
        self.toplam_tutar = self.siparis_tutar_hesapla()

    def siparis_tutar_hesapla(self):
        """
        Ürünlerin toplam tutarını hesaplar ve kargo ücretini ekler.
        Eğer tutar negatifse özel hata fırlatır.
        """
        toplam = sum(fiyat for _, fiyat in self.urun_listesi) + self.kargo_ucreti
        if toplam < 0:
            raise GecersizTutarHatasi("Sipariş tutarı negatif olamaz!")
        return toplam

    def siparis_bilgisi(self):
        """Siparişin detaylarını string olarak döndürür"""
        urunler_str = ", ".join([f"{urun} ({fiyat} TL)" for urun, fiyat in self.urun_listesi])
        return f"Sipariş No: {self.siparis_no} | Müşteri: {self.musteri_ad} | Ürünler: {urunler_str} | Toplam: {self.toplam_tutar} TL"


#  **Sipariş Yönetim Sistemi (Dosya İşlemleri ve Yönetim)**
class SiparisYonetim:
    DOSYA_ADI = "siparisler.txt"

    def __init__(self):
        """Dosya varsa yükle, yoksa yeni oluştur"""
        if not os.path.exists(self.DOSYA_ADI):
            with open(self.DOSYA_ADI, "w", encoding="utf-8") as file:
                file.write("")

    def siparis_ekle(self, siparis: Siparis):
        """Siparişi dosyaya kaydeder"""
        with open(self.DOSYA_ADI, "a", encoding="utf-8") as file:
            file.write(f"{siparis.siparis_no},{siparis.musteri_ad},{siparis.toplam_tutar}\n")

    def siparis_oku(self, siparis_no):
        """Dosyadan siparişi okur ve bulamazsa hata fırlatır"""
        with open(self.DOSYA_ADI, "r", encoding="utf-8") as file:
            siparisler = file.readlines()

        for siparis in siparisler:
            no, musteri, toplam = siparis.strip().split(",")
            if int(no) == siparis_no:

                raise SiparisBulunamadiHatasi(f"Sipariş No {siparis_no} bulunamadı!")


            return f"Sipariş No: {no} | Müşteri: {musteri} | Toplam: {toplam} TL"



#  **Test Senaryosu (Kullanıcı Simülasyonu)**
def main():
    # Sipariş Yönetim Sistemi
    yonetim = SiparisYonetim()

    # Yeni Siparişler Ekleyelim
    siparis1 = Siparis(101, "Ahmet Kaya", [("Laptop", 15000), ("Mouse", 300)])
    siparis2 = Siparis(102, "Sude Girişimci", [("Telefon", 18000), ("Kılıf", 200)])

    # Siparişleri Dosyaya Kaydet
    yonetim.siparis_ekle(siparis1)
    yonetim.siparis_ekle(siparis2)

    # Siparişleri Okuyalım
    try:
        print(yonetim.siparis_oku(101))  # Ahmet'in siparişi
        print(yonetim.siparis_oku(999))  # Olmayan bir sipariş numarası (Hata fırlatacak)
    except SiparisBulunamadiHatasi as e:
        print(f"Hata: {e}")


if __name__ == "__main__":
    main()
