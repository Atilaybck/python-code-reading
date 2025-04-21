# list_comprehension_example.py

# ---------------------------------------
# 🔹 List Comprehension Nedir?

# Bir liste oluşturmak için kısa ve okunabilir bir yoldur.
# Normalde for döngüsüyle yazdığımız işlemleri tek satırda yapmamızı sağlar.

# ✅ Sözel Örnek:
# "0'dan 9'a kadar olan sayılar içinden sadece çift olanları bir listeye eklemek istiyorum."

# Uzun yöntem (geleneksel yol):
ciftler = []
for i in range(10):
    if i % 2 == 0:
        ciftler.append(i)

print("Uzun yöntem:", ciftler)  # Çıktı: [0, 2, 4, 6, 8]

# Kısa yöntem (List Comprehension ile):
ciftler = [i for i in range(10) if i % 2 == 0]
print("List Comprehension:", ciftler)  # Çıktı: [0, 2, 4, 6, 8]

# 🔍 Kodun işleyiş adımları:

# 1. range(10) → [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] oluşturur

# 2. Bu listedeki her eleman sırayla i değişkenine atanır

# 3. if i % 2 == 0 → i sayısı 2’ye tam bölünüyor mu? kontrol edilir
#    - Eğer evet → bu sayı listeye alınır
#    - Eğer hayır → o sayı atlanır

# 4. [i ...] kısmı:
#    - Bu ifade: “Şarta uyan i değerlerinden hangisi listeye eklenecek?” sorusuna cevap verir
#    - Burada `i` yazdığı için → doğrudan i’nin kendisi listeye eklenir

# 5. İşlem sırasıyla şöyle işler:
#    i = 0 → 0 % 2 == 0 → ✔ listeye ekle → [0]
#    i = 1 → 1 % 2 != 0 → ❌ atla
#    i = 2 → 2 % 2 == 0 → ✔ listeye ekle → [0, 2]
#    i = 3 → ❌
#    i = 4 → ✔ → [0, 2, 4]
#    ...
#    i = 9 → ❌

# 6. Sonuç: [0, 2, 4, 6, 8]

# 📌 Not: Eğer [i] yerine [i**2] yazsaydık, çift sayıların kareleri listeye eklenirdi.

# ---------------------------------------

# Başka Bir Örnek (Kısa yöntem (List Comprehension ile)):

# 🔹 Örnek: 0'dan 9'a kadar olan çift sayıların karelerini listele

kareler = [i**2 for i in range(10) if i % 2 == 0]
print("Çift sayıların kareleri:", kareler)  # Çıktı: [0, 4, 16, 36, 64]

# 🔍 Kodun işleyiş adımları:

# 1. range(10) → [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 2. Her sayı sırayla i'ye atanır

# 3. if i % 2 == 0 → sadece çift sayılar filtrelenir

# 4. [i**2 ...] kısmı:
#    - Şarta uyan her i'nin karesi (i**2) listeye eklenir

# 5. İşlem sırasıyla şöyle olur:
#    i = 0 → çift ✔ → 0**2 = 0     → listeye ekle → [0]
#    i = 1 → tek  ✖ → atla
#    i = 2 → çift ✔ → 2**2 = 4     → listeye ekle → [0, 4]
#    i = 3 → tek  ✖ → atla
#    i = 4 → çift ✔ → 4**2 = 16    → listeye ekle → [0, 4, 16]
#    i = 5 → tek  ✖ → atla
#    i = 6 → çift ✔ → 6**2 = 36    → listeye ekle → [0, 4, 16, 36]
#    i = 7 → tek  ✖ → atla
#    i = 8 → çift ✔ → 8**2 = 64    → listeye ekle → [0, 4, 16, 36, 64]
#    i = 9 → tek  ✖ → atla

# 6. Sonuç: [0, 4, 16, 36, 64]


# ---------------------------------------


# 🔹 Örnek 1: 1’den 5’e kadar sayıların kareleri

kareler = [x**2 for x in range(1, 6)]
print("Kareler:", kareler)  # Çıktı: [1, 4, 9, 16, 25]

# ---------------------------------------


# 🔹 Örnek 2: Metinleri büyük harfe çevir

isimler = ["ali", "ayşe", "zeynep"]
buyukler = [isim.upper() for isim in isimler]
print("Büyük harfli isimler:", buyukler)  # Çıktı: ['ALI', 'AYŞE', 'ZEYNEP']

# ---------------------------------------


# 🔹 Örnek 3: Sayıların tek mi çift mi olduğunu yaz

durumlar = ["çift" if x % 2 == 0 else "tek" for x in range(5)]
print("Tek/Çift durumları:", durumlar)  # Çıktı: ['çift', 'tek', 'çift', 'tek', 'çift']

# ---------------------------------------


# 🔹 Örnek 4: İç içe döngü (nested loop)

carpimlar = [i * j for i in range(1, 4) for j in range(1, 4)]
print("Çarpım tablosu (1-3 arası):", carpimlar)
# Çıktı: [1, 2, 3, 2, 4, 6, 3, 6, 9]

# ---------------------------------------
# ✅ Özet:
# - List Comprehension ile liste üretmek hem kolay hem hızlıdır.
# - Yapısı: [ifade for eleman in liste]
# - Şartlı filtreleme: [ifade for eleman in liste if şart]
# - if-else: [true_deger if şart else false_deger for eleman in liste]
