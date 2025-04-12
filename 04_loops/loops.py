# ---------------------------------------
# 🔹 1. for döngüsü – Liste üzerinden gezinme

meyveler = ["elma", "armut", "muz"]

# Kod açıklaması:
# 'meyveler' listesinde 3 adet meyve var.
# 'for' döngüsü bu liste üzerinde sırayla gezinir.
# Her turda 'meyve' değişkeni, listedeki bir elemanı alır.

for meyve in meyveler:
    print("Meyve:", meyve)

# Çıktı:
# Meyve: elma
# Meyve: armut
# Meyve: muz
# ---------------------------------------


# 🔹 2. while döngüsü – Koşul sağlandıkça döner

sayi = 1

# Açıklama:
# sayi değişkeni 1’den başlar, 3’e kadar gider.
# Her seferinde ekrana yazdırılır ve 1 artırılır.
# sayi <= 3 koşulu sağlandığı sürece döngü devam eder.

while sayi <= 3:
    print("Sayı:", sayi)
    sayi += 1

# Çıktı:
# Sayı: 1
# Sayı: 2
# Sayı: 3
# ---------------------------------------


# 🔹 3. range() fonksiyonu – Belirli aralıkta döner

# Açıklama:
# range(5) → 0'dan başlar, 5’e kadar (5 hariç) döner

for i in range(5):
    print("i:", i)

# Çıktı:
# i: 0
# i: 1
# i: 2
# i: 3
# i: 4

# range(start, stop, step) kullanımı:
for i in range(1, 10, 3):
    print("Adım 3'lü:", i)

# Çıktı:
# Adım 3'lü: 1
# Adım 3'lü: 4
# Adım 3'lü: 7
# ---------------------------------------


# 🔹 4. break – Döngüyü erken bitirir

# Açıklama:
# Döngü normalde 1’den 5’e kadar gider.
# Ancak sayi 3 olduğunda break ile durdurulur.

for sayi in range(1, 6):
    if sayi == 3:
        break
    print("Break örneği:", sayi)

# Çıktı:
# Break örneği: 1
# Break örneği: 2
# ---------------------------------------


# 🔹 5. continue – O turu atlar, sonraki tura geçer

# Açıklama:
# sayi 3 olduğunda o tur atlanır.
# 3 ekrana yazdırılmaz.

for sayi in range(1, 6):
    if sayi == 3:
        continue
    print("Continue örneği:", sayi)

# Çıktı:
# Continue örneği: 1
# Continue örneği: 2
# Continue örneği: 4
# Continue örneği: 5
# ---------------------------------------


# 🔹 6. else – Döngü normal biterse çalışır

# Açıklama:
# Döngü 0,1,2 değerleri için çalışır.
# break kullanılmazsa else çalışır.

for i in range(3):
    print("i:", i)
else:
    print("Döngü tamamlandı.")

# Çıktı:
# i: 0
# i: 1
# i: 2
# Döngü tamamlandı.

# break ile else çalışmaz:
for i in range(3):
    if i == 1:
        break
    print("i:", i)
else:
    print("Bu yazı yazılmaz.")

# Çıktı:
# i: 0
# ---------------------------------------


# 🔹 7. İç içe döngü (nested loop)

# Açıklama:
# Dış döngü 2 kez döner (i = 1, 2)
# İç döngü 3 kez döner (j = 1, 2, 3)
# Toplamda 6 satır yazılır.

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


# 🔹 8. pass – Henüz yazılmamış döngü yapıları için

# Açıklama:
# Kod yazılmayacaksa ama yapı yazılmışsa syntax hatası almamak için pass kullanılır.

for i in range(3):
    pass  # Kod sonra eklenecek, şu an boş bırakıldı
