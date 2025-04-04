#Bellekle yer işgal etmeyen bir iterator oluşturuyor

def cube():
    result=[]


    for i in range(5):
        result.append(i**3)

    return result

print(cube())


#bellek ğzerinde yer tutmayan bir yapı

def cube2():
    for i in range(5):
        yield i **3
        #yield bizim için bir değer üretiyor bunun kübünü alıyor ve bu değer bir yerde saklanmıyor 2.defa ulaşamıyorum

print(cube2()) 
generator=cube2()
iterator=iter(generator)
#generatorden bir iterator oluşturdum ve  ekrana bastırdım

print(next(iterator))
print(next(iterator))
print(next(iterator))

#Peki genaratorler sadece fonkisyonlar ile mi oluşuyor
liste=[ i for i in range(5)] #bu  gösterimi genarator olrak döndürmek istiyorsak
liste=(i for i in range(5)) #bu generatör oldu
print(liste)
print(next(liste))
print(next(liste))
print(next(liste))
