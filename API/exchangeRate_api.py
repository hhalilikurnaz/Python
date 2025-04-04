#ExchangeRate -Apı kullanarak bir uygulama yapıcaz

import requests
import json

bozulan_doviz=input("Bozulan Döviz Türü :").upper()#usd 
alinan_döviz=input("Alınan Döviz Türü:").upper() #TRY
miktar=int(input(f"Ne Kadar  {bozulan_doviz} Bozdurmak istiyorsunuz :"))


api_key="4f91e4e723e4d43e35425bfb"
api_url=f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{bozulan_doviz}"



sonuc=requests.get(api_url)
print(sonuc.text)

#Json tarafından gelen stringi okumak için python objesine çevirmemiz lazım

sonuc_json=json.loads(sonuc.text)

#print(sonuc_json["conversion_rates"][alinan_döviz])
print("1 {0}={1} {2}".format(bozulan_doviz,sonuc_json['conversion_rates'][alinan_döviz],alinan_döviz))  
print("{0} {1}={2} {3}".format(miktar,bozulan_doviz,miktar*sonuc_json['conversion_rates'][alinan_döviz],alinan_döviz))
