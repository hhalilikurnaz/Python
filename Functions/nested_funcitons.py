'''
#fonksiyonlar bir objedir
def greeting(name):
    print('hello',name)

greeting('Halil')
print(greeting('Sude'))

sayHello=greeting
 #atama işlemi bilginin tutundugu adrese 
print(sayHello)
print(greeting)

'''

#encapsulation
def outer(num1):
    print('outer')
    def inner_increment(num1):
        print('inner')
        return num1+1
    num2=inner_increment(num1) #innerı çağırabilmek için dıştaki fonksiyonda da çağırmamız lazım
    print(num1,num2)

    
outer(10)#sadece outer fonkisyonu çalışacak içindeki fonksiyon çağrılmadı


def factorial(number):
    if not isinstance(num,int):
        raise TypeError(f"Number {number} must be an integer ")
    
    def inner_factorial(number):
        if number <=0:
            return 1
        
        return number * inner_factorial(number-1)

    return inner_factorial(number)
