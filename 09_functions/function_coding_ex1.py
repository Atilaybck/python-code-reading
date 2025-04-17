# function_coding_ex.py

# 🔹 Soru 1:
# "Merhaba, dünya!" yazdıran bir fonksiyon yaz.



def merhaba():
    print("Merhaba, dünya!")

merhaba()  # Çıktı: Merhaba, dünya!
# ----------------------------------------------------------------



# 🔹 Soru 2:
# "Günaydın, dünya!" yazdıran bir fonksiyon yaz.



def gunaydin():
    print("Günaydın, dünya!")

gunaydin()  # Çıktı: Günaydın, dünya!
# ----------------------------------------------------------------


# 🔹 Soru 3:
# İsmini parametre olarak alıp "Merhaba <isim>!" yazan fonksiyonu yaz.



def karsila(isim):
    print(f"Merhaba {isim}!")

karsila("Berke")  # Çıktı: Merhaba Berke!
# ----------------------------------------------------------------


# 🔹 Soru 4:
# İsmini parametre olarak alıp "Güle güle <isim>!" yazan fonksiyonu yaz.



def vedalas(isim):
    print(f"Güle güle {isim}!")

vedalas("Ali")  # Çıktı: Güle güle Ali!
# ----------------------------------------------------------------


# 🔹 Soru 5:
# İki sayıyı toplayıp sonucu döndüren fonksiyon yaz.



def topla(a, b):
    return a + b

print(topla(4, 6))  # Çıktı: 10
# ----------------------------------------------------------------


# 🔹 Soru 6:
# İki sayı arasındaki farkı döndüren fonksiyon yaz.
def fark(a, b):
    return a - b

print(fark(10, 4))  # Çıktı: 6
# ----------------------------------------------------------------


# 🔹 Soru 7:
# Bir liste içindeki sayıların ortalamasını hesaplayan fonksiyon yaz.



def ortalama(liste):
    return sum(liste) / len(liste)

print(ortalama([10, 20, 30]))  # Çıktı: 20.0
# ----------------------------------------------------------------


# 🔹 Soru 8:
# Bir liste içindeki sayıların ortalamasını hesaplayan fonksiyon yaz. Ancak sonuç integer olsun.


def ortalama(liste):
    return int(sum(liste) / len(liste))

print(ortalama([10, 20, 30]))  # Çıktı: 20
# ----------------------------------------------------------------


# 🔹 Soru 9:
# Bir liste içindeki sayıların toplamını döndüren fonksiyon yaz.



def toplam(liste):
    return sum(liste)

print(toplam([5, 10, 15]))  # Çıktı: 30
# ----------------------------------------------------------------



# 🔹 Soru 10:
# Bir sayının tek mi çift mi olduğunu yazan fonksiyon yaz.
def tek_cift(sayi):
    if sayi % 2 == 0:
        print("Çift sayı")
    else:
        print("Tek sayı")

tek_cift(7)  # Çıktı: Tek sayı
# ----------------------------------------------------------------



# 🔹 Soru 11:
# Bir sayının negatif mi pozitif mi olduğunu yazan fonksiyon yaz.
def negatif_mi_pozitif_mi(sayi):
    if sayi < 0:
        print("Negatif")
    else:
        print("Pozitif")

negatif_mi_pozitif_mi(-3)  # Çıktı: Negatif
# ----------------------------------------------------------------



# 🔹 Soru 12:
# *args kullanarak gelen sayıların çarpımını hesaplayan fonksiyon yaz.
def carpim(*args):
    sonuc = 1
    for sayi in args:
        sonuc *= sayi
    return sonuc

print(carpim(2, 3, 4))  # Çıktı: 24


# Örneğin Açıklamalı Hali:
# *args kullanarak gelen sayıların çarpımını hesaplayan fonksiyon

def carpim(*args):
    # Başlangıç değeri 1 çünkü çarpma işleminde etkisiz elemandır
    sonuc = 1
    
    # args içindeki her sayıyı sırayla al ve çarp
    for sayi in args:
        sonuc *= sayi  # sonuc = sonuc * sayi

    # Çarpım sonucunu döndür
    return sonuc

# Fonksiyonu 2, 3, 4 ile çağırıyoruz
print(carpim(2, 3, 4))  # Çıktı: 24

# Açıklama:
# 1 × 2 = 2
# 2 × 3 = 6
# 6 × 4 = 24
# Sonuç → 24
# ----------------------------------------------------------------


# 🔹 Soru 13:
# *args kullanarak gelen sayıların en küçüğünü döndüren fonksiyon yaz.



def en_kucuk(*args):
    return min(args)

print(en_kucuk(7, 3, 9, 2))  # Çıktı: 2
# ----------------------------------------------------------------



# 🔹 Soru 14:
# **kwargs kullanarak bir kişinin bilgilerini yazdıran fonksiyon yaz.


def kisi_bilgi(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")

kisi_bilgi(ad="Zeynep", yas=28, sehir="Ankara")
# Çıktı:
# ad: Zeynep
# yas: 28
# sehir: Ankara

#Örneğin Açıklaması:
# **kwargs sayesinde fonksiyona istediğimiz sayıda anahtar-değer çifti gönderebiliriz.
# Fonksiyon bu çiftleri bir sözlük gibi alır:
# kwargs = {"ad": "Zeynep", "yas": 28, "sehir": "Ankara"}

# for k, v in kwargs.items() döngüsü bu sözlüğü dolaşır:
# 1. tur: k = "ad", v = "Zeynep"
# 2. tur: k = "yas", v = 28
# 3. tur: k = "sehir", v = "Ankara"
# **kwargs kullanarak bir kişinin bilgilerini yazdıran fonksiyon
# ----------------------------------------------------------------



# 🔹 Soru 15:
# **kwargs kullanarak bir ürünün bilgilerini yazdıran fonksiyon yaz.
def urun_bilgi(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} → {v}")

urun_bilgi(ad="Bilgisayar", fiyat=15000, marka="Asus")
# Çıktı:
# ad → Bilgisayar
# fiyat → 15000
# marka → Asus
# ----------------------------------------------------------------



# 🔹 Soru 16:
# Fonksiyon içinde başka bir fonksiyonu çağırarak karenin alanını yazdır.



def kare(x):
    return x * x

def alan_yazdir(x):
    print("Alan:", kare(x))

alan_yazdir(5)  # Çıktı: Alan: 25
# ----------------------------------------------------------------



# 🔹 Soru 17:
# Fonksiyon içinde başka bir fonksiyonu çağırarak küp hacmini yazdır.
def kup(x):
    return x ** 3

def hacim_yazdir(x):
    print("Küp hacmi:", kup(x))

hacim_yazdir(3)  # Çıktı: Küp hacmi: 27
# ----------------------------------------------------------------



# 🔹 Soru 18:
# Parametre almayan, ama "Hoş geldin!" yazan bir fonksiyon yaz.



def hos_geldin():
    print("Hoş geldin!")

hos_geldin()  # Çıktı: Hoş geldin!
# ----------------------------------------------------------------



# 🔹 Soru 19:
# Parametre almayan, ama "İyi akşamlar!" yazan bir fonksiyon yaz.



def iyi_aksamlar():
    print("İyi akşamlar!")

iyi_aksamlar()  # Çıktı: İyi akşamlar!
# ----------------------------------------------------------------



# 🔹 Soru 19:
# Varsayılan parametre kullanan ve "Merhaba <isim>" yazan bir fonksiyon yaz.



def selam(isim="Ziyaretçi"):
    print(f"Merhaba {isim}!")

selam()            # Çıktı: Merhaba Ziyaretçi!
selam("Atılay")     # Çıktı: Merhaba Atılay!
# ----------------------------------------------------------------



# 🔹 Soru 20:
# Varsayılan parametre kullanan ve "Hoşça kal <isim>" yazan bir fonksiyon yaz.



def veda(isim="Arkadaş"):
    print(f"Hoşça kal {isim}!")

veda()          # Çıktı: Hoşça kal Arkadaş!
veda("Merve")   # Çıktı: Hoşça kal Merve!
# ----------------------------------------------------------------



# 🔹 Soru 21:
# Bir kelimeyi parametre olarak alıp, büyük harflerle yazdıran bir fonksiyon yaz.



def buyuk_yaz(kelime):
    print(kelime.upper())

buyuk_yaz("merhaba")  # Çıktı: MERHABA
# ----------------------------------------------------------------



# 🔹 Soru 22:
# Bir sayı listesinden sadece çift olanları döndüren fonksiyonu yaz.



def ciftleri_getir(liste):
    # Boş bir liste oluştur
    ciftler = []

    # Listedeki her elemanı sırayla kontrol et
    for x in liste:
        # Eğer sayı 2 ile tam bölünüyorsa (çiftse)
        if x % 2 == 0:
            # Bu sayıyı ciftler listesine ekle
            ciftler.append(x)

    # Sonuç olarak ciftler listesini döndür
    return ciftler

print(ciftleri_getir([1, 2, 3, 4, 5, 6]))  # Çıktı: [2, 4, 6]
# ----------------------------------------------------------------



# 🔹 Soru 23:
#Bir string'in kaç karakterden oluştuğunu döndüren fonksiyon yaz.



def uzunluk(kelime):
    return len(kelime)

print(uzunluk("Python"))  # Çıktı: 6
# ----------------------------------------------------------------


# 🔹 Soru 24:


# Bir sayı listesindeki en büyük sayıyı döndüren fonksiyon yaz.



def en_buyuk(liste):
    return max(liste)

print(en_buyuk([4, 10, 8]))  # Çıktı: 10
# ----------------------------------------------------------------


# 🔹 Soru 25:
# *args kullanarak gönderilen sayılar arasından en büyüğünü bulan fonksiyon yaz.

def hmm(*sayilar):
    return max(sayilar)

print(hmm(10, 20))  # Çıktı: 20






