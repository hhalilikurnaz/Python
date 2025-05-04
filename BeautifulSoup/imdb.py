
from bs4 import BeautifulSoup
import requests

url='https://www.imdb.com/chart/top/?ref_=nv_mv_250'

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}
#burda tarayıcı gibi davranmak için headers dosyayı oluşturuyoruz 

html=requests.get(url,headers=headers).content #request modelin get 'i ile url ye bir talep göndericem
print(html)
#400lu hatalar kullanıcıyı ilgilendiriyor 

#bizim burda bir tarayıcı olarka bu sayfaya gidiyor olmamız lazım

#request modulule işimiz bitti artık beautifulsoup kütüphanesine geçiyoruz



soup=BeautifulSoup(html,"html.parser")
liste =soup.find("ul",{"class":"ipc-metadata-list"}).find_all("li",limit=15)

for item in liste:
    filmadi=item.find("h3",{"class":"ipc-title__text"}).text
    puan=item.find("span",{"class":"ipc-rating-star"}).text
    print(filmadi,puan)
