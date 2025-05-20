#Selenium bir  web otomasyon kütüphanesidir

#selenium ile bir web sitesini ziyaret edip etkileşimde bulunabiliriz


#rutin olarak yaptıgımız bir işi selenium ile yaptırabiliyoruz 


#driver hangi tarayıcı ile çalışacğaız 

#driverı ilgili py dosyasının içine attım

from selenium import webdriver

import time 

driver=webdriver.Chrome()


url="https://www.hepsiburada.com/"

driver.get(url) #get metodu ile sayfanın açılmasını sağlıyoruz 

time.sleep(2)#sayfaya gittikten sonra 2 saniye bekletelim ve sonra sayfanın sitenin herneyse title kısmını yazdıralım
driver.maximize_window() #sayfa tam ekran olur 
#driver.save_screenshot("hepsiburada.com-homepage.png") #sayfanın ekran görüntüsünü alır 


#farklı sayfaya yönlendirmek istersek eğer
url="https://www.trendyol.com/"
driver.get(url)


print(driver.title)

if "trendyol" in driver.title:
    driver.save_screenshot("trendyol-trendyol.png")

time.sleep(2)
driver.back() #sayfayı geri alıyoruz yani hepsiburada'dan trenddyola git sonra geri hepsiburadaya gel sonra kapat oldu
#driver.forward() #sayfayı ileri alıyoruz 
driver.close()
