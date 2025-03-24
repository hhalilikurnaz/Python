#User > Temel kullanıcı sınıfı [İsim,Id,rol:operatör,teknisyen vb]
#Drone: Her biri ID’ye sahip, görev alabilen dronelar
#Mission: Bir gözetim/tespit görevi: [(bölge, hedef, süre, aciliyet)]
#ControlCenter: Droneları yöneten sistem, görevleri dağıtır,

#Kendi Custom Exceptionlarım olcak : DroneAlreadyAssignedError, MissionTimeoutError..
#Kullanacağım Error Handling :Kullanıcı görev dışında drone’a erişirse hataGörev süresi geçmişse MissionTimeoutError/Zaten görevde olan drone’a yeni görev atanırsa DroneAlreadyAssignedError

import re  #Şifre doğrulaması için regex
import time 
from typing import List


#----Özel Hatalar---

#Görevde Olan Bir Drone'u tekrar atamaya çalışırsak fırlatırlır
class DroneAlreadyAssignedError(Exception):
    pass

# Yanlış durumda bir drone göreve başlatılırsa
class DroneStatusError(Exception):
    pass

# Görev süresi aşıldığında tetiklenir
class MissionTimeoutError(Exception):
    pass

## Kullanıcı adı geçersizse
class InvalidUsernameError(Exception):
    pass

## Şifre geçersizse
class InvalidPasswordError(Exception):
    pass


# --- KULLANICI DOĞRULAMA FONKSİYONLARI -


def validate_username(username):
    if len(username) < 4:
        raise InvalidUsernameError("Kullanıcı adı en az 4 karakter olmalı")
    if not username.isalnum(): #isalnum() alfanumeric (@-/_ gibi ifadeler içerir)
        raise InvalidUsernameError("Kullanıcı adı yalnızca harf ve rakam içermelidir.")


def validate_password(password):
    if (len(password)) <6:
        raise InvalidPasswordError("Şifre en az 6 karakterden oluşmalıdır")

    if not re.search("[A-Z]",password):
        raise InvalidPasswordError("Şifre en az bir büyük harf içermeli.")
    elif not re.search("[a-z]",password):
        raise InvalidPasswordError("Şifre en az bir küçük harf içermeli.")
    elif not re.search("[0-9]",password):
        raise InvalidPasswordError("Şifre en az bir rakam içermeli.")

    elif not re.search("[_@/]",password):
        raise InvalidPasswordError("Şifre en az bir alfanumeric karakter içermeli.")

    if re.search(r"\s", password):
        raise InvalidPasswordError("Şifre boşluk içermemelidir.")

    
    # ------ Kullanıcı bilgileri ---- 
class User:
    def __init__(self,username,role):
        self.username=username
        self.role=role 

    
    def __str__(self):
        return f"{self.username} ({self.role})"

#Operatör sınıfı, user'dan türetildi

class Operator(User):
    def __init__(self,username):
        super().__init__(username,role='operator')


class Drone:
    def __init__(self,drone_id):
        self.drone_id=drone_id
        self.status='available' #'avaible','assigned','in_mission'

        self._battary_level=100 #protected 


    def __str__(self):
        return f"Drone {self.drone_id} {self.status} durumunda !"


    def assign_mission(self):
        if not self.status=='available':
            raise DroneAlreadyAssignedError(f"{self} zaten görevde !")

        self.status='assigned'
        print(f"{self} göreve atandı! ")

    def start_mission(self):
        if self.status != 'assigned':
            raise DroneStatusError(f"{self} görev başlatılamaz.Şu anki durum : {self.status}")

        self.status='in_mission'

        print(f" {self} göreve başladı")

    def finish_mission(self):
        self.status='available'
        print(f"{self} görevini başarı ile tamamladı")


#----- Görev Sınıfı

class Mission:
    def __init__(self,region,duration):
        self.region=region #Görev  bölgesi
        self.duration=duration #Görev srüesi 
        self.start_time=None #Gröevin ne zaman başlatıldığını tutmak için


    def start(self):
        self.start_time=time.time() # görev başladığı an zaman da başlıyor
        print(f"Görev Başlatıldı : {self.region} {self.duration} sn ") 


    def is_expired(self): #Görevin süresi dolmuşmu kontol eder
        if self.start_time is None:
            raise ValueError("Görev Henüz Başlatılmamış !")
        return (time.time() -self.start_time) > self.duration


    #----kontrol Merkezi

class ControlCenter:
    def __init__(self):
        self.drones:List[Drone]=[]

    def add_drone(self,drone):
        self.drones.append(drone)


    def assign_and_start_mission(self,operator,drone,mission):
        print(f"\n {operator} görev başlatıyor...")

        try:
            drone.assign_mission() #Görev Atama
            mission.start() #Görev başlat
            drone.start_mission() #Drone görevde

            time.sleep(mission.duration + 1) #Görev Süresini Bekliyoruz(simülasyon)

            if mission.is_expired():#Süre kontrolü
                raise MissionTimeoutError("Görev Süresi Aşıldı!")
            
            drone.finish_mission()

        except (DroneAlreadyAssignedError,DroneStatusError,MissionTimeoutError) as exc:
            print(f" HATA {exc}")


        
# kullanııcıı oluşturma -----

def create_user():
    try:
        username=input(" Kullanıcı adınızı Giriniz :")
        validate_username(username)


        password=input("Şifrenizi Giriniz :")
        validate_password(password)

        print(f"Giriş Başarılı Hoş geldin {username}")
        return Operator(username)


    except(InvalidUsernameError,InvalidPasswordError) as e :
        print("Hata !",e)
        return None




def main():
    #Programın ana akışı burada başlıyor
    control_center=ControlCenter()


    #Kullanıcı Girişi

    user=create_user()
    if not user :
        return
    

    #Drone Görevi oluştur
    drone1=Drone("Göktay")
    control_center.add_drone(drone1)

    mission1=Mission("KızılElma",duration=8)

    #Görev Başlat
    control_center.assign_and_start_mission(user,drone1,mission1)

#Çalıştırmak için 
if __name__ == "__main__":
    main()
