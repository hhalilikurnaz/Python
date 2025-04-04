#Iterable Üzerinde dolaşılabilen nesne
#Iterator next() metodu ile bir sonraki öğeye geçebilen nesne.

liste=[1,2,3,4,5]
for i in liste:
    print(i)


iterator=iter(liste)
'''
print(iterator)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
'''


while True:
    try:
        element=next(iterator)
        print(element)

    except StopIteration:
        break
#bu kadar işlemi neden yapıyoruz ? for döngüsüyle de oluyor zaten dimi
#for döngüsü basit işler için.Iteratör sınıfı karmaşık ver iüretimi için ideal
#bellekte tüm veriyi tutar     belleği verimli kullanır
#sabit döngülerde güzel.        özelleşttirilebilir davranışlar sağlar

class Mynumbers:
    def __init__(self,start,stop):
        self.start=start
        self.stop=stop
    def __iter__(self):
        return self

    def __next__(self):
        if self.start <=self.stop:
            x=self.start
            self.start +=1

            return x
        else:
            raise StopIteration
    
list=Mynumbers(20,50)
myiter=iter(list)

for x in list:
    print(x)

while True:
    try:

        element=next(myiter)
        print(element)
    except StopIteration:
        break
