#beatiful soup'un yaptığı işlem biz bir html iskeleti veriyoruz 
#herhangi bir web sayfasından alacak olduğumuz html isteğini istediğimiz şekilde
html_doc="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>İlk web saydam</title>
</head>
<body>
<h1 id="header">
        Python Kursu
    </h1>
    <div class="grup1">
        <h2>
            Programlama
        </h2>
        <ul>
            <li>Menü 1 </li>
            <li>Menü 2 </li>
            <li>Menü 3 </li>
            <li>Menü 4 </li>
        </ul>

    </div>

    <div class="grup2">
        <h2>
            Moduller
        </h2>
        <ul>
            <li>Menü 1 </li>
            <li>Menü 2 </li>
            <li>Menü 3 </li>
            <li>Menü 4 </li>
        </ul>

    </div>
   
</body>

</html>

"""


from bs4 import BeautifulSoup

#BeatifulSoup bizden bir tane markup istiyor html istiyor

soup=BeautifulSoup(html_doc,'html.parser') #html dokumanına uygun bir parser (analiz) yapsın diyoruz

result=soup.prettify() #html dokumanımızı düzenleme işlemi yapıyor 
result=soup.title #etiketle beraber geliyoruz
result=soup.title.name #etiket içerisindeki title geliyor 
print(result)

result=soup.h1
print(result)


result=soup.find_all('h2') #verdiğimiz etiket ismiyle bütün h2 etiketlerini bana getirir
print(result)


result=soup.div #bütün divleri yazdrır ekrana
print(result)
#mesela spesifikte seçebiliyoruz yani mesela divin içinden 2.ul etiketi al
result=soup.find_all('div')[1].ul.find_all('li')
print(result)

result=soup.div.findChildren() #bütün alt elemanları getir 
print(result)
