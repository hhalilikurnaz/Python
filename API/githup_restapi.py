#RestApi nedir = web üzerinden veri alışverişi yapmaya yarayan bir sitemdir
#Get -> veri Alırsın
##POST ->Yeni Veri Gönderirsin
###PUT/PATCH->Mevcut veriyi günceller
####Delete -> Veriyi siler



import requests
import time
import json


class Github:
    def __init__(self):
        self.api_url='https://api.github.com'
        self.token='your token'

    def getUser(self,username):
        response=requests.get(self.api_url+"/users/"+username)
        
        return response.json() #python tarafında kullanabileceğimiz bir sözlük dict yapısına çevriliyor

    def getRepositories(self,username):
        response=requests.get(self.api_url+'/users/'+username+'/repos')
        if response.status_code==404:
            print(f"{username} bulunamadı")
        return response.json()

    def createRepository(self,name):
        
        response=requests.post(self.api_url+'/user/repos?access_token='+self.token+json={
            "name": name,
            "description": "A mysterious repo full of autumn magic and cozy code 🍂🎃",
            "homepage": "https://github.com",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True



        })#gönderdiğimiz extra parametre token
        return response.json()
    
github=Github()

while True:
    print("1-Find User \n2-Get Repositories\n3-Create Repository\n4-Exit :")
    secim=input("Seçiminiz:").strip()

    match secim:

        case "1":
            username=input('Username:')
            
            

            for _ in range(3):


                print("Kullanıcı bulunuyor...")
                time.sleep(1)
            result=github.getUser(username)
            print(f"Kullanıcı bulundu {result['name']},\n public repos :{result['public_repos']}, \n Followers{result['followers']}")
            

            
            
        case "2":
            username=input("Username:").strip()
            result=github.getRepositories(username)
            
            for _ in range(3):
                    print("Repository'ler listeleniyor...")
                    time.sleep(1)
            for repo in result:
                print(f"📁 Repo: {repo['name']} \n Link: {repo['html_url']}\n")


            
            
        case "3":
            name=input('Repository name :')
            result=github.createRepository(name)
            for _ in range(4):
                print("Yeni repository oluşturuluyor...")
                time.sleep(1)
            print(result)
            
            
            #repository oluştururken bir login işlemi olması gerekiyor herhangi bir kişi benim hesabımda repo oluşturamaz
            

        case "4":
            print("Çıkış Yapılıyor")
            break
        case _:

            print(f"Hatalı Seçim Yaptınız {secim}")
            break
