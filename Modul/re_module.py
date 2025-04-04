import re 
import time



def regex_oyunu():
    print(" Oyuna Hoşgeldiniz")
    time.sleep(1)
    print("Her Soruda verilen desene uygun bir örnek girmen gerekiyor")
    time.sleep(1)
    print("Hazırsan başlıyoruz")
    time.sleep(1)

    sorular=[
        {
            "soru":"geçerli bir e-mail adresi gir (örnek: isim@site.com)",
            "pattern": r"^[\w\.-]+@[\w\.-]+\.\w+$" 
        },
        {
            "soru": "📞 Geçerli bir telefon numarası gir (örnek: 05XX1234567)",
            "pattern": r"^05\d{9}$"
        },
        {
            "soru": "🚗 Bir araç plakası gir (örnek: 34ABC123)",
            "pattern": r"^\d{2}[A-Z]{1,3}\d{2,4}$"
        },
        {
            "soru": "💳 Bir kredi kartı numarası gir (16 haneli, boşluksuz)",
            "pattern": r"^\d{16}$"
        },
        {
            "soru": "🔒 En az 8 karakterli, 1 büyük harf, 1 küçük harf ve 1 rakam içeren şifre gir",
            "pattern": r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$"
        },
    ]

    for index,soru in enumerate(sorular,1):

        print(f"\n{index}. Soru: {soru['soru']}")
        cevap=input("Cevabın :")
        if re.fullmatch(soru['pattern'],cevap):
            print("Bravo...")
        else:
            print("Adam akıllı gir")


    print("\n Oyun bitti! Yeni desene göre oyunlar için beni çağırabilirsin!")

regex_oyunu()
