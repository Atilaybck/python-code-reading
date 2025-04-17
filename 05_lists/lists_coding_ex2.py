# 🔹 Soru 21: Bir sayı listesi oluştur, her elemanın karesini ekrana yazdır.



sayilar = [1, 2, 3, 4, 5]
for sayi in sayilar:
    print(sayi ** 2)
# Çıktı:
# 1
# 4
# 9
# 16
# 25
# ---------------------------------------


# 🔹 Soru 22: İçinde 5 eleman olan bir liste oluştur. Listenin son elemanını yazdır.



sayilar = [11, 22, 33, 44, 55]
print(sayilar[-1])  # Çıktı: 55
# ---------------------------------------


# 🔹 Soru 23: Bir liste oluştur. İçindeki çift sayıları yazdır.



sayilar = [10, 15, 20, 25, 30]
for sayi in sayilar:
    if sayi % 2 == 0:
        print(sayi)
# Çıktı:
# 10
# 20
# 30
# ---------------------------------------


# 🔹 Soru 24: Bir liste oluştur. İçindeki çift sayıları yazdır. Sonrasında bu çift sayıları bir listenin içine koy.



sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ciftler = []

for sayi in sayilar:
    if sayi % 2 == 0:
        print(sayi)
        ciftler.append(sayi)

print("Çift sayılar listesi:", ciftler)

# Çıktı:
# 2
# 4
# 6
# 8
# 10
# Çift sayılar listesi: [2, 4, 6, 8, 10]
# ---------------------------------------


# 🔹 Soru 25: Liste elemanlarının toplamını hesapla.



sayilar = [3, 6, 9, 12]
toplam = sum(sayilar)
print("Toplam:", toplam)  # Çıktı: Toplam: 30
# ---------------------------------------


# 🔹 Soru 26: Liste elemanlarının ortalamasını yazdır.



sayilar = [4, 8, 6, 2, 10]
ortalama = sum(sayilar) / len(sayilar)
print("Ortalama:", ortalama)  # Çıktı: Ortalama: 6.0
# ---------------------------------------


# 🔹 Soru 27: Listeyi string olarak birleştir ve araya virgül koy.



renkler = ["kırmızı", "mavi", "yeşil"]
metin = ", ".join(renkler)
print(metin)  # Çıktı: kırmızı, mavi, yeşil
# ---------------------------------------

# 🔹 Soru 28: İçinde hem string hem sayı olan bir liste oluştur. Her elemanın tipini yazdır.



karisik = ["elma", 42, True, 3.14]
for eleman in karisik:
    print(type(eleman))
# Çıktı:
# <class 'str'>
# <class 'int'>
# <class 'bool'>
# <class 'float'>
# ---------------------------------------


# 🔹 Soru 29: Bir listedeki tekrar eden elemanları yazdır.



liste = [1, 2, 3, 2, 4, 5, 1]
tekrarlar = []
for i in liste:
    if liste.count(i) > 1 and i not in tekrarlar:
        tekrarlar.append(i)
print(tekrarlar)  # Çıktı: [1, 2]
# ---------------------------------------


# 🔹 Soru 30: Liste elemanlarını küçükten büyüğe sırala ve ardından en küçük ve en büyük değeri yazdır.



sayilar = [33, 11, 55, 22, 44]
sayilar.sort()
print("En küçük:", sayilar[0])      # Çıktı: En küçük: 11
print("En büyük:", sayilar[-1])     # Çıktı: En büyük: 55
# ---------------------------------------


# 🔹 Soru 31: İç içe liste (nested list) oluştur. İçinden belirli bir elemana ulaş.



matris = [[1, 2], [3, 4], [5, 6]]
print(matris[1][1])  # Çıktı: 4
# ---------------------------------------


# 🔹 Soru 32: 1 ile 10 arasındaki tek sayılardan oluşan bir liste oluştur.



tekler = []
for i in range(1, 11):
    if i % 2 != 0:
        tekler.append(i)
print(tekler)  # Çıktı: [1, 3, 5, 7, 9]
# ---------------------------------------


# 🔹 Soru 33: Listedeki stringlerin uzunluklarını yazdır.



isimler = ["Ali", "Berke", "Ayşe"]
for isim in isimler:
    print(len(isim))
# Çıktı:
# 3
# 5
# 4
# ---------------------------------------



# 🔹 Soru 34: İçinde hem string hem int olan bir liste oluştur. Sadece string olanları yazdır.



karisik = ["elma", 42, "muz", 3.14, "armut"]
for eleman in karisik:
    if isinstance(eleman, str):
        print(eleman)
# Çıktı:
# elma
# muz
# armut
# ---------------------------------------


# 🔹 Soru 35: Kullanıcıdan 3 giriş al ve bir listeye kaydet. Ardından yazdır.
# Not: input() yerine örnek veri kullandık.



kullanicilar = []
kullanicilar.append("Ali")
kullanicilar.append("Veli")
kullanicilar.append("Ayşe")
print(kullanicilar)  # Çıktı: ['Ali', 'Veli', 'Ayşe']
# ---------------------------------------


# 🔹 Soru 36: Listeyi ters çevirerek yeni bir liste oluştur.



renkler = ["kırmızı", "mavi", "yeşil"]
ters = renkler[::-1]
print(ters)  # Çıktı: ['yeşil', 'mavi', 'kırmızı']
# ---------------------------------------


# 🔹 Soru 37: Listedeki elemanları hem index hem değer olarak yazdır.



sehirler = ["İstanbul", "Ankara", "İzmir"]
for i in range(len(sehirler)):
    print(i, ":", sehirler[i])
# Çıktı:
# 0 : İstanbul
# 1 : Ankara
# 2 : İzmir
# ---------------------------------------


# 🔹 Soru 38: Liste içindeki elemanların hepsini tek bir string haline getir.



kelimeler = ["Bugün", "hava", "güzel"]
cumle = " ".join(kelimeler)
print(cumle)  # Çıktı: Bugün hava güzel
# ---------------------------------------


# 🔹 Soru 39: Listedeki en küçük ve en büyük değerin farkını hesapla.



sayilar = [10, 25, 5, 40, 15]
fark = max(sayilar) - min(sayilar)
print("Fark:", fark)  # Çıktı: Fark: 35
# ---------------------------------------


# 🔹 Soru 40: Listedeki tüm elemanların toplamının çift olup olmadığını kontrol et.



sayilar = [4, 6, 8, 2]
toplam = sum(sayilar)
if toplam % 2 == 0:
    print("Toplam çift")  # Çıktı: Toplam çift
else:
    print("Toplam tek")
# ---------------------------------------