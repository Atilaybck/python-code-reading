# loops_coding_ex1.py

# Soru 1:
# "renkler" adında bir liste oluştur. İçinde 3 farklı renk olsun (örnek: "kırmızı", "mavi", "yeşil").
# Daha sonra bu liste üzerinde for döngüsü kullanarak her rengi ekrana yazdır.



renkler = ["kırmızı", "mavi", "yeşil"]
for renk in renkler:
    print("Renk:", renk)
# Çıktı:
# Renk: kırmızı
# Renk: mavi
# Renk: yeşil
# ---------------------------------------


# Soru 2:
# 1’den 5’e kadar olan sayıları while döngüsüyle yazdır. (5 dahil olacak)



sayi = 1
while sayi <= 5:
    print("Sayı:", sayi)
    sayi += 1

# Açıklama:
# sayi değişkeni 1 olarak başlar.
# while döngüsü, sayi 5'ten küçük veya eşit olduğu sürece çalışır.
# Her turda ekrana sayi yazdırılır ve sayi 1 artırılır.
# sayi değeri 6 olduğunda koşul sağlanmaz ve döngü durur.

# Çıktı:
# Sayı: 1
# Sayı: 2
# Sayı: 3
# Sayı: 4
# Sayı: 5
# ---------------------------------------


# Soru 3:
# 0’dan 10’a kadar olan sayılar içinde sadece çift olanları ekrana yazdır (range ve if ile yap)



for i in range(11):
    if i % 2 == 0:
        print("Çift sayı:", i)
# Çıktı:
# Çift sayı: 0
# Çift sayı: 2
# Çift sayı: 4
# Çift sayı: 6
# Çift sayı: 8
# Çift sayı: 10
# ---------------------------------------

# Soru 4:
# 1’den 10’a kadar olan sayılar içinde, 5’e geldiğinde döngüyü durdur (break kullan)

for i in range(1, 11):
    if i == 5:
        break
    print("Sayı:", i)
# Çıktı:
# Sayı: 1
# Sayı: 2
# Sayı: 3
# Sayı: 4
# ---------------------------------------


# Soru 5:
# 1’den 10’a kadar olan sayılar içinde, 5’i atla ve diğerlerini yazdır (continue kullan)



for i in range(1, 11):
    if i == 5:
        continue
    print("Sayı:", i)
# Çıktı:
# Sayı: 1
# Sayı: 2
# Sayı: 3
# Sayı: 4
# Sayı: 6
# Sayı: 7
# Sayı: 8
# Sayı: 9
# Sayı: 10
# ---------------------------------------


# Soru 6:
# Bir for döngüsü yaz, 0’dan 2’ye kadar dönen. Döngü bittikten sonra "Döngü tamamlandı." yaz.



for i in range(3):
    print("i:", i)
else:
    print("Döngü tamamlandı.")
# Çıktı:
# i: 0
# i: 1
# i: 2
# Döngü tamamlandı.
# ---------------------------------------


# Soru 7:
# İç içe iki döngü kur. Dış döngü 1-2, iç döngü 1-3 arasında döner. Satır ve sütun yaz.



for i in range(1, 3):
    for j in range(1, 4):
        print(f"{i}. satır, {j}. sütun")
# Çıktı:
# 1. satır, 1. sütun
# 1. satır, 2. sütun
# 1. satır, 3. sütun
# 2. satır, 1. sütun
# 2. satır, 2. sütun
# 2. satır, 3. sütun
# ---------------------------------------


# Soru 8:
# for döngüsü içinde kod yazma, ama yapı kurulu olsun. Hata almamak için pass kullan.



for i in range(3):
    pass
# Çıktı: (hiçbir şey yazdırmaz)
# ---------------------------------------


# Soru 9:
# 1’den 10’a kadar olan sayılar arasında 3’e tam bölünenleri yazdır.



for i in range(1, 11):
    if i % 3 == 0:
        print("3'e bölünen:", i)
# Çıktı:
# 3'e bölünen: 3
# 3'e bölünen: 6
# 3'e bölünen: 9
# ---------------------------------------


# Soru 10:
# Kullanıcıdan bir sayı al ve 1’den o sayıya kadar olan tek sayıları yazdır.



sayi = int(input("Bir sayı girin: "))
for i in range(1, sayi + 1):
    if i % 2 != 0:
        print("Tek sayı:", i)
# Örnek Girdi: 7
# Çıktı:
# Tek sayı: 1
# Tek sayı: 3
# Tek sayı: 5
# Tek sayı: 7
# ---------------------------------------


# Soru 11:
# 0’dan 20’ye kadar olan sayılar içinde hem 2’ye hem 3’e tam bölünenleri yazdır.



for i in range(21):
    if i % 2 == 0 and i % 3 == 0:
        print("2 ve 3'e bölünen:", i)
# Çıktı:
# 2 ve 3'e bölünen: 0
# 2 ve 3'e bölünen: 6
# 2 ve 3'e bölünen: 12
# 2 ve 3'e bölünen: 18
# ---------------------------------------


# Soru 12:
# Kullanıcıdan bir sayı al. 1’den o sayıya kadar olan tüm sayıları topla.



sayi = int(input("Bir sayı girin: "))
toplam = 0
for i in range(1, sayi + 1):
    toplam += i
print("Toplam:", toplam)
# Örnek Girdi: 5
# Çıktı:
# Toplam: 15
# ---------------------------------------


# Soru 13:
# 10’dan geriye doğru 1’e kadar olan sayıları yazdır (tersten).



for i in range(10, 0, -1):
    print("Geri sayım:", i)
# Çıktı:
# Geri sayım: 10
# Geri sayım: 9
# ...
# Geri sayım: 1
# ---------------------------------------


# Soru 14:
# "merhaba" kelimesinin harflerini tek tek yazdır.



kelime = "merhaba"
for harf in kelime:
    print("Harf:", harf)
# Çıktı:
# Harf: m
# Harf: e
# Harf: r
# Harf: h
# Harf: a
# Harf: b
# Harf: a
# ---------------------------------------


# Soru 15:
# 0’dan 20’ye kadar olan sayılar içinde, sadece 5’in katı olanları yazdır.



for i in range(21):
    if i % 5 == 0:
        print("5'in katı:", i)
# Çıktı:
# 5'in katı: 0
# 5'in katı: 5
# 5'in katı: 10
# 5'in katı: 15
# 5'in katı: 20
# ---------------------------------------


# Soru 16:
# Kullanıcıdan bir metin al. Her harfi alt alta yaz.



metin = input("Bir metin girin: ")
for harf in metin:
    print(harf)
# Örnek Girdi: ali
# Çıktı:
# a
# l
# i
# ---------------------------------------


# Soru 17:
# 1’den 100’e kadar olan sayıların toplamını yazdır.



toplam = 0
for i in range(1, 101):
    toplam += i
print("Toplam:", toplam)
# Çıktı:
# Toplam: 5050
# ---------------------------------------


# Soru 18:
# 10 elemanlı bir liste oluştur (rakamlar). Her birini sırayla yazdır.
rakamlar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for r in rakamlar:
    print("Rakam:", r)
# Çıktı:
# Rakam: 0
# Rakam: 1
# ...
# Rakam: 9
# ---------------------------------------

# Soru 19:
# 1’den 20’ye kadar olan sayılar içinde, hem 2’ye hem 5’e tam bölünenleri bul.
for i in range(1, 21):
    if i % 2 == 0 and i % 5 == 0:
        print("2 ve 5'e bölünen:", i)
# Çıktı:
# 2 ve 5'e bölünen: 10
# 2 ve 5'e bölünen: 20
# ---------------------------------------

# Soru 20:
# Kullanıcıdan 5 sayı al, hepsini topla ve sonucu yazdır.
toplam = 0
for i in range(5):
    sayi = int(input(f"{i+1}. sayıyı girin: "))
    toplam += sayi
print("Toplam:", toplam)
# Örnek Girdi: 1, 2, 3, 4, 5
# Çıktı:
# Toplam: 15
# ---------------------------------------
