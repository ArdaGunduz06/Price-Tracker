import datetime

print("Ardanın Özel Asistanı")

tarih = datetime.datetime.now()
kullaniciadi = input(print("Kullanıcı Adı:"))
kullanicişifre = input(print("Şifre:"))

if kullaniciadi == "arda" and kullanicişifre == "1234":
    print("Hoşgeldiniz Efendim")

else:
    print("Yanlış Şifre")
    quit()

banasorusor = input(print("Bana soru sorun efendim:")).lower()


def banasorusor1(cevap):
    print(cevap)


if banasorusor == ("adın ne senin"):
    banasorusor1("Adım Jarvis")

elif banasorusor == ("saat kaç"):
    print(f'Şuan saat:{tarih}')

elif banasorusor == ("nasılsın"):
    banasorusor1("İyiyim")

elif banasorusor == ("bana espri yaparmısın",):
    banasorusor1("En güzel yemek yapan Ceren hangisidir? :TENCERE")

elif banasorusor == ("görüşürüz",):
    banasorusor1("Görüşürüz", )

elif banasorusor == ("nerde yaşıyosun",):
    banasorusor1("Ankara")

elif banasorusor == ("ben nerde okuyorum",):
    banasorusor1("Gölbaşı Anadolu Lisesinde")

elif banasorusor == ("gelecekde nerce olacaksın"):
    banasorusor1("Yanında")

else:
    banasorusor1("Beni daha buna kodlamadın :")
#Gelişim aşamasında Döngüler Fonksiyonlar ve Makine Öğreninimi ile geri dönecek...
#Arda Gündüz