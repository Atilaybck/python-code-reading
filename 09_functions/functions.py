# ---------------------------------------
# 🔹 1. Fonksiyon Tanımı (def)

def selamla():
    print("Merhaba!")

# Fonksiyon tanımlanır ama çalışmaz.
# Çalışması için çağırmak gerekir:
selamla()  # Çıktı: Merhaba!

# ---------------------------------------


# ✅ Ekstra Örnek:

def hosgeldin():
    print("Hoş geldiniz!")

hosgeldin()  # Çıktı: Hoş geldiniz!

# Fonksiyonlar def ile tanımlanır ve çağrılmadan çalışmaz.
# ---------------------------------------



# 🔹 2. Parametreli Fonksiyon

def selam_ver(isim):
    print(f"Selam, {isim}!")

selam_ver("Ali")     # Çıktı: Selam, Ali!
selam_ver("Ayşe")    # Çıktı: Selam, Ayşe
# ---------------------------------------


# ✅ Ekstra Örnek:

def yas_soyle(isim, yas):
    print(f"{isim} {yas} yaşında.")

yas_soyle("Zeynep", 23)
# Çıktı: Zeynep 23 yaşında.

# Parametreli fonksiyonlar dışarıdan veri alır.
# ---------------------------------------



# 🔹 3. Varsayılan Parametre

def topla(a, b=5):
    print("Toplam:", a + b)

topla(3)       # Çıktı: Toplam: 8
topla(3, 2)    # Çıktı: Toplam: 5
# ---------------------------------------


# ✅ Ekstra Örnek:

def selam(isim="Ziyaretçi"):
    print(f"Merhaba {isim}!")

selam()            # Çıktı: Merhaba Ziyaretçi!
selam("Berke")     # Çıktı: Merhaba Berke!

# Varsayılan parametreler, değer girilmezse çalışır.
# ---------------------------------------



# 🔹 4. return ile Değer Döndürme

def carp(x, y):
    return x * y

sonuc = carp(4, 5)
print("Çarpım:", sonuc)  # Çıktı: Çarpım: 20
# ---------------------------------------


# ✅ Ekstra Örnek:

def kare(x):
    return x ** 2

print("Karesi:", kare(6))  # Çıktı: Karesi: 36

# return, sonucu dışarı aktarır. print ile yazdırılabilir.
# ---------------------------------------



# 🔹 5. Anahtar Kelime Argümanlar (Keyword Arguments)

def bilgi(ad, sehir):
    print(f"{ad} adlı kişi {sehir}'de yaşıyor.")

# Argümanların sırası önemli değil çünkü isimle eşleşiyor
bilgi(sehir="Ankara", ad="Zeynep")
# Çıktı: Zeynep adlı kişi Ankara'da yaşıyor.
# ---------------------------------------


# ✅ Ekstra Örnek:

def siparis_ozeti(urun, adet, fiyat):
    print(f"{adet} adet {urun}, tanesi {fiyat} TL")

siparis_ozeti(adet=3, fiyat=25, urun="Kahve")
# Çıktı: 3 adet Kahve, tanesi 25 TL
# ---------------------------------------



# 🔹 6. *args (çoklu konumsal argüman)

# *args, fonksiyona birden fazla sayıda konumsal (sıralı) argüman göndermeyi sağlar.
# Bu argümanlar fonksiyon içinde bir tuple gibi davranır.

def sayilar_toplami(*args):
    print("Gelen sayılar:", args)
    print("Toplam:", sum(args))

sayilar_toplami(1, 2, 3)
# Çıktı:
# Gelen sayılar: (1, 2, 3)
# Toplam: 6

sayilar_toplami(10, 20, 30, 40)
# Çıktı:
# Gelen sayılar: (10, 20, 30, 40)
# Toplam: 100

# ---------------------------------------


# ✅ Ekstra Örnek 1: Ortalama Hesaplama

def ortalama(*sayilar):
    if sayilar:
        print("Ortalama:", sum(sayilar) / len(sayilar))
    else:
        print("Hiç sayı girilmedi.")

ortalama(10, 20, 30)   # Çıktı: Ortalama: 20.0
ortalama()             # Çıktı: Hiç sayı girilmedi.

# ---------------------------------------


# ✅ Ekstra Örnek 2: En Büyük Sayıyı Bulma

def en_buyuk(*args):
    print("En büyük sayı:", max(args))

en_buyuk(4, 8, 2, 15, 3)
# Çıktı: En büyük sayı: 15

# ---------------------------------------


# ✅ Ekstra Örnek 3: İsimleri Yazdırma

def isimleri_yaz(*isimler):
    for isim in isimler:
        print(f"Merhaba, {isim}!")

isimleri_yaz("Ali", "Ayşe", "Zeynep")
# Çıktı:
# Merhaba, Ali!
# Merhaba, Ayşe!
# Merhaba, Zeynep!

# ---------------------------------------
# Not:
# - *args sadece konumsal (sıralı) argümanları alır
# - Fonksiyonlarda argüman sayısını sınırsız hale getirmek için kullanılır
# - args ismi değiştirilebilir (örn: *sayilar), ama genelde *args kullanılır
# ----------------------------------------------



# 🔹 7. **kwargs (çoklu anahtar-değer argümanı)

# **kwargs, fonksiyona istenildiği kadar anahtar=değer çiftleri göndermeyi sağlar.
# Fonksiyon içinde bu veriler bir sözlük (dict) olarak yakalanır.

def kisi_bilgisi(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} → {value}")

kisi_bilgisi(ad="Ali", yas=30, sehir="İzmir")
# Çıktı:
# ad → Ali
# yas → 30
# sehir → İzmir
# ---------------------------------------


# ✅ Ekstra Örnek 1: Profil Yazdırma

def profil(**bilgiler):
    print("Profil Bilgileri:")
    for k, v in bilgiler.items():
        print(f"- {k}: {v}")

profil(ad="Ayşe", meslek="Yazılımcı", medeni_hal="Bekar")
# Çıktı:
# Profil Bilgileri:
# - ad: Ayşe
# - meslek: Yazılımcı
# - medeni_hal: Bekar
# ---------------------------------------


# ✅ Ekstra Örnek 2: Varsayılanlar + kwargs

def mail_gonder(kime, konu="Genel", **detaylar):
    print(f"Mail gönderiliyor: {kime}")
    print(f"Konu: {konu}")
    for anahtar, deger in detaylar.items():
        print(f"{anahtar} → {deger}")

mail_gonder("mehmet@gmail.com", mesaj="Toplantı 14.00'te", onem="Yüksek")
# Çıktı:
# Mail gönderiliyor: mehmet@gmail.com
# Konu: Genel
# mesaj → Toplantı 14.00'te
# onem → Yüksek
# ---------------------------------------


# ✅ Ekstra Örnek 3: kwargs + args birlikte kullanımı

def detayli_bilgi(*args, **kwargs):
    print("Pozisyonel argümanlar:", args)
    print("Anahtar-değer argümanları:", kwargs)

detayli_bilgi("Python", "React", sehir="İstanbul", yil=2025)
# Çıktı:
# Pozisyonel argümanlar: ('Python', 'React')
# Anahtar-değer argümanları: {'sehir': 'İstanbul', 'yil': 2025}

# ---------------------------------------
# Notlar:
# - kwargs → "keyword arguments" ifadesinin kısaltmasıdır
# - kwargs ismi yerine başka isim de kullanılabilir (örn: **bilgi), ama genelde **kwargs yazılır
# - kwargs bir dict (sözlük) gibi davranır → .items(), .keys(), .values() ile işlenebilir
# ---------------------------------------



# 🔹 8. Fonksiyon İçinde Koşul ve Döngü

def tek_mi_cift_mi(sayi):
    if sayi % 2 == 0:
        print(f"{sayi} çift sayıdır.")
    else:
        print(f"{sayi} tek sayıdır.")

tek_mi_cift_mi(11)
tek_mi_cift_mi(24)

# ---------------------------------------
# ✅ Ekstra: Döngü ile

def tekleri_yaz(sayilar):
    for s in sayilar:
        if s % 2 == 1:
            print("Tek:", s)

tekleri_yaz([1, 2, 3, 4, 5])
# Çıktı: 1, 3, 5
# ---------------------------------------



# 🔹 9. Fonksiyonlar Arası Çağrı

def karesi(x):
    return x * x

def yazdir(x):
    sonuc = karesi(x)
    print(f"{x} sayısının karesi: {sonuc}")

yazdir(7)  # Çıktı: 7 sayısının karesi: 49

# ---------------------------------------



# 🔹 10. Docstring (Fonksiyon Açıklaması)

def bol(a, b):
    """
    Bu fonksiyon iki sayıyı böler.
    b sıfır olursa hata mesajı döner.
    """
    if b == 0:
        return "Hata: Sıfıra bölünemez!"
    return a / b

print(bol(10, 2))  # Çıktı: 5.0
print(bol(10, 0))  # Çıktı: Hata: Sıfıra bölünemez!

# Docstring'leri görmek için: help(bol) veya print(bol.__doc__)
