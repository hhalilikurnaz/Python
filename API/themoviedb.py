#themoviedb.org => film ve dizi arşivi
#themoviedb'nin sundugu apiyi uygulamamızda kullanıyoruz
#anahtar kelimeye göre sılara
#en popüler film listesi
#vizyondaki film listesi
# my api_key=e437a45b733c9e508cb14ebf6abde6fd

import requests

class theMovieDb:
    def __init__(self):
        self.api_url="https://api.themoviedb.org/3"
        self.api_key="eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlNDM3YTQ1YjczM2M5ZTUwOGNiMTRlYmY2YWJkZTZmZCIsIm5iZiI6MTc0Mzg0ODk2Mi42MzY5OTk4LCJzdWIiOiI2N2YxMDYwMjhiMWYzMmViNzlkOTY2NzYiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.x2fhTk7h8jJW-bY-xJZE_Q4g3BDcB96FEebfbVX9m-M"

    def getPopulars(self):
        url=f"{self.api_url}/movie/popular?language=en-US&page=1"
        headers={
            "Authorization": f"Bearer {self.api_key}",
            "accept": "application/json"
        }
        response=requests.get(url,headers=headers)
        
       
        print("Status",response.status_code)
        print("Data",response.json())
        return response.json()
    def getSearchResult(self,keyword):
        url=f"{self.api_url}/search/movie?query={keyword}&language=en-US&page=1"
        headers={
            "Authorization": f"Bearer {self.api_key}",
            "accept":"application/json"
        }
        response=requests.get(url,headers=headers)
        '''print("Status",response.status_code)
        print("Data",response.json())'''
        return response.json()



movieApi=theMovieDb()
while True:

    secim=input("1-Popular Movies \n2-Search Movies \n 3-Exit\nSeçim:")
    
    if secim=="3":
        break

    elif secim=="1":
        result=movieApi.getPopulars()

        if "results" in result:
            print("\n Popüler Filmler \n")
            for movie in result['results']:
                print(f"{movie['title']} ({movie['release_date']})")

        else:
            print("Film Verisi bulunamadı",result)

    elif secim=="2":
        keyword=input("Keyword:")
        movies=movieApi.getSearchResult(keyword)
        if "results" in movies:
            for movie in movies.get('results',[]):
                title=movie.get('title','Başlık bulunamadı')
                release_date=movie.get('release_date','Tarih Yok')
                overview=movie.get('overview','Açıklama Yok')
                print(" Başlık:", title)
                print(" Vizyon Tarihi:", release_date)
                print(" Konu:", overview)
                print("-" * 50)  # Görsellik için çizgi
    
