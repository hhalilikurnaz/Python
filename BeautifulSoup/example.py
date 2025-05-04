import requests
from bs4 import BeautifulSoup

url="https://www.hepsiburada.com/laptop-notebook-dizustu-bilgisayarlar-c-98"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}

try:

    response=requests.get(url,headers=headers,timeout=5)
    print(response.status_code)
    html=response.content


    soup=BeautifulSoup(html,"html.parser")


    liste=soup.find_all("li",{"class":"productListContent"},limit=10) #li dediğimiz liste bunun altında istedğimiz özellikleri alabiliriz 


    print(liste)
except requests.exceptions.RequestException as e :
    print("Hata Oluştu",e)

