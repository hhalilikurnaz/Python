
def usalma(number):
    #taban kısmı burası
    


    def inner(power):
        #üst kısmıda burası
        return number **power

    return inner


two=usalma(2)
three=usalma(3)
print(two(3))
print(three(4))


def yetki_sorgula(page):#kullaıcı bir sayfaya gitmek istiyor diyelim yetki sorgulucaz
    def inner(role):
        if role =='Admin':
            return "{0} rolünün {1} sayfasına ulaşabilir".format(role,page)
        
        else:
            return "{0} rolünün {1} sayfasına ulaşamaz".format(role,page)
    return inner
user1=yetki_sorgula("Product Edit") #nereye erişmek istediğini burada alıyoruz
print(user1("Admin"))#hangi rolde olduğunu buraya alıp fosnkisyonu çalıştırıyoruz


def islem(islem_adi):
    def toplama(*args):
        #dışarıdan sınırsız saydıda arguman alsın
        toplam=0

        for i in args:
            toplam +=i
    return toplama

    def carpma(*args):
        carpim=1
        for i in args:

            carpım *=i

        return carpim

    if islem_adi=='toplama':
        return toplama

    else:
        return carpma


toplama=islem("toplama")
print(toplama(1,3,54,6554))

carpma=islem('carpma')
print(carpma(1,5,6,45))
