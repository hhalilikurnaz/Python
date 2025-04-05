#RestApi nedir = web üzerinden veri alışverişi yapmaya yarayan bir sitemdir
#Get -> veri Alırsın
##POST ->Yeni Veri Gönderirsin
###PUT/PATCH->Mevcut veriyi günceller
####Delete -> Veriyi siler
#MYToken --your key


import requests
import time
import json


class Github:
    def __init__(self,username):
        self.api_url='https://api.github.com'
        self.token='your token'
        self.username=username

    def getUser(self):
        response=requests.get(self.api_url+"/users/"+self.username)
        
        return response.json() #python tarafında kullanabileceğimiz bir sözlük dict yapısına çevriliyor

    def getRepositories(self):
        response=requests.get(self.api_url+'/users/'+self.username+'/repos')
        if response.status_code==404:
            print(f"{username} bulunamadı")
        return response.json()

    def createRepository(self,name):
        headers={ #headers mantıgı githu'a ben yetkiliyim diyoruz
            "Authorization": f"Bearer {self.token}", #Bearer tokeni taşıyan kişi yani ben
            "Accept": "application/json" #GitHub REST v3 API’sinin döndüreceği formatı belirtiyor. (tavsiye edilen)
        }
        
        response=requests.post(self.api_url+'/user/repos',headers=headers,json={
            "name": name,
            "description": "A mysterious repo full of autumn magic and cozy code",
            "homepage": "https://github.com",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True



        })#gönderdiğimiz extra parametre token
        return response.json()

    def deleteRepository(self,repo_name):
        url=f"{self.api_url}/repos/{self.username}/{repo_name}"
        headers={
            "Authorization":f"Bearer {self.token}",
            "Accept":"application/json"
        }
        response=requests.delete(url,headers=headers)
        if(response.status_code==204):
            print(f"{repo_name} Başarıyla silindi")
        else:
            print(f"{repo_name} Silinemedi")
            print(response.json())

username=input("Lütfen kullanıcı adınızı Giriniz :")
github=Github(username)

while True:
    print("1-Find User \n2-Get Repositories\n3-Create Repository\n4-Exit\n5 Delete Repository :")
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


        case "5":
            repo_name=input("Silmek İstediğiniz Repo Adı :")
            result=github.deleteRepository(repo_name)
            print(result)
        case _:

            print(f"Hatalı Seçim Yaptınız {secim}")
            break
