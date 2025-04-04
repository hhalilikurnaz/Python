#Tarih veya zamanla alakalı bir işlem yapıcaksak bunu kullanıyoru<z

from datetime import datetime #datetimedan speksifik bir şey import etmek istediğimizde
from datetime import timedelta
şimdi=datetime.now()
print(şimdi)

result=şimdi.year
print(result)
result=şimdi.day
print(result)

result=datetime.ctime(şimdi) #günü ayı zamanı string güzel açıklamalı yazıyor
print(result)

result=datetime.strftime(şimdi,'%Y %B %A')
print(result)


t='21 April 2019 hour 10:12:30'
result = datetime.strptime(t,'%d %B %Y hour %H:%M:%S')
print(result)

#kendimiz tarih vermek istersek eğer

birtday=datetime(2002,1,19,9,30,00)
result=datetime.timestamp(birtday)
print(result) #saniye bilgisini veriyor
result=datetime.fromtimestamp(0)
print(result) #1970den itibaren pc miladını o gün olarak alıyor
result=şimdi-birtday #timedelta objesi döndürüyor bize


result=result.days #timedeltadan gelen toplam gün getirisi
print(result)


result=şimdi+timedelta(days=10) #gelecekti zamanlar için işlem
print(result)


#Geri Sayım Sayacı (Countdown timer)

import time 
def geri_sayim(saniye):
    while saniye >0:
        print(f" Kalan Süre : {saniye}")
        saniye -=1

    print("Süren Doldu")

geri_sayim(5)


#Süre Ölçme

baslangıc=time.time()

for i in range(10000):
    pass

bitis=time.time()
print(f" İşlem süresi {bitis-baslangıc} saniye ")


#Belirli bir Tarihe Kalan süreyi gösterme

gelecek_tarih=datetime(2025,4,20,15,0,0)
şimdi=datetime.now()

fark=gelecek_tarih-şimdi
print(f" Kalan Süre {fark}")
print(f" Gün : {fark.days} , Saniye : {fark.seconds}")


