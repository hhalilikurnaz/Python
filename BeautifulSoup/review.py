
'''
 Neler Kullanacağız?
 requests
 BeautifulSoup
 OOP
 File
 Error handling

'''

import requests #internetten sayfa içeriğini çeker
from bs4 import BeautifulSoup #çekilen html sayfasını parçalayıp yorumları bulur 

url="https://www.sephora.com.tr/trends/"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}#Tarayıcı gibi davranmamız gerekiyor 

try:
    response=requests.get(url,headers=headers) #belirlediğimiz url'ye git ve get isteğini gönder tarayıcı gibi davrandığımızı sçyleyen headers da isteğe dahil et
    response.raise_for_status() #hata varsa istisna fırlat.Eğer sayfa bulunamadıysa (404), yetkisiz erişimse (403) veya sunucu hatasıysa (500) bu satır hata fırlatır.
    html_content=response.text
except requests.exception.RequestException as e :
    print("Sayfa Çekilemedi ",e)
    html_content=None 


#Html içeriğini yorumlayalım
soup=BeautifulSoup(html_content,"html.parser")

urunler=[] #ürünleri taşıyacağımız boş liste

#ürün kartlarını bul
product_cards=soup.find_all("div",class_="product-card__details") 
#Her ürün kartı bu class ile tanımlanıyor. Liste halinde hepsini aldık.

for card in product_cards:
    try:
        isim=card.find("a",class_="product-card__link").text.strip()
        link="https://www.sephora.com.tr"+card.find("a",class_="product-card__link")['href']
        #ürün linkini (href attribute),
        fiyat=card.find("div",class_="price__main").text.strip()

        urunler.append({
            "isim":isim,
            "link":link,
            "fiyat":fiyat
        }) #her bir ürünü sözlük olarak listeye ekledik 

    except Exception as e :
        print("Bir ürün işlenemedi",e)


with open("sephora_trend_urunleri.txt","w",encoding="utf-8") as dosya:
    for urun in urunler :
        dosya.write(f" Ürün:{urun['isim']}\n")
        dosya.write(f" Link:{urun['link']}\n")
        dosya.write(f" Fiyat:{urun['fiyat']}\n")
        dosya.write("-" * 40 + "\n")
