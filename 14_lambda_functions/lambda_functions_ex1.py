# lambda_functions_ex1.py

# ---------------------------------------


# 🔹 Örnek 1: Bir sayının karesini alma


kare = lambda x: x ** 2
print("Karesi:", kare(6))  # Çıktı: 36

# ---------------------------------------

# 🔹 Örnek 2: İki sayıyı toplama


topla = lambda a, b: a + b
print("Toplam:", topla(4, 7))  # Çıktı: 11

# ---------------------------------------

# 🔹 Örnek 3: Sayının tek mi çift mi olduğunu söyleme


tek_mi = lambda x: "tek" if x % 2 == 1 else "çift"
print("7 sayısı:", tek_mi(7))  # Çıktı: tek
print("8 sayısı:", tek_mi(8))  # Çıktı: çift

# ---------------------------------------

# 🔹 Örnek 4: Listedeki her ismi büyük harfe çevirme


isimler = ["ali", "ayşe", "zeynep"]
buyukler = list(map(lambda isim: isim.upper(), isimler))
print("Büyük harfli isimler:", buyukler)  # Çıktı: ['ALI', 'AYŞE', 'ZEYNEP']

# ---------------------------------------

# 🔹 Örnek 5: 10'dan büyük olan sayıları filtreleme


sayilar = [5, 12, 3, 20, 8]
buyukler = list(filter(lambda x: x > 10, sayilar))
print("10'dan büyük sayılar:", buyukler)  # Çıktı: [12, 20]
