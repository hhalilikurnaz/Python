#Lımonimi : Fiyat Tarama Sistemi
#Hm Iterator hem de generator yapılırını görücez


#1.Iterator kullanımı



class LimonFiyatIterator:
    def __init__(self,fiyat_listesi):
        #Gelen fiyat bilgisini al ve indexi sıfırla
        self.fiyat_listesi=fiyat_listesi
        self.index=0

    def __iter__(self):
        #iterator nesnesi olarak kendini döndürür
        return self

    def __next__(self) :
        #Eğer index listedeki elemandan küçükse devam et
        if self.index < len(self.fiyat_listesi):
            fiyat=self.fiyat_listesi[self.index]
            self.index +=1 #indexi bir arttır
            return f"Limon Fiyat : {fiyat} TL"

        else:
            raise StopIteration


#Kullanımı
fiyatlar = [30, 28, 31, 35, 40]
print("--- ITERATOR ile Tarama ---")
limon_iter = LimonFiyatIterator(fiyatlar)
for bilgi in limon_iter:
    print(bilgi)


#Generator kullanımı
def limon_fiyat_generator(fiyat_listesi):
    #her bir fiyastı döndür ama fonksiyon belirtme
    for fiyat in fiyat_listesi:

        yield f" Taranıyor ... Limon {fiyat} TL"


# Kullanım:
print("\n--- GENERATOR ile Tarama ---")
for satir in limon_fiyat_generator(fiyatlar):
    print(satir)
