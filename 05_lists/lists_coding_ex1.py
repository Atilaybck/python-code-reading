# lists_coding.py

# 🔹 Soru 1: "araba" isimli bir liste oluştur ve içine 3 marka ekle. İlk elemanı yazdır.



araba = ["Toyota", "BMW", "Ford"]
print(araba[0])  # Çıktı: Toyota
# ---------------------------------------


# 🔹 Soru 2: "araba" listesine "Mercedes" markasını sona ekle.



araba.append("Mercedes")
print(araba)  # Çıktı: ['Toyota', 'BMW', 'Ford', 'Mercedes']
# ---------------------------------------


# 🔹 Soru 3: Listenin 2. sırasına "Audi" ekle.
araba.insert(1, "Audi")



print(araba)  # Çıktı: ['Toyota', 'Audi', 'BMW', 'Ford', 'Mercedes']
# ---------------------------------------


# 🔹 Soru 4: "BMW" elemanını listeden sil.



araba.remove("BMW")
print(araba)  # Çıktı: ['Toyota', 'Audi', 'Ford', 'Mercedes']
# ---------------------------------------


# 🔹 Soru 5: Listenin son elemanını sil ve ekrana yazdır.



son = araba.pop()
print("Çıkan marka:", son)  # Çıktı: Çıkan marka: Mercedes
print(araba)  # Çıktı: ['Toyota', 'Audi', 'Ford']
# ---------------------------------------


# 🔹 Soru 6: "Ford" yerine "Hyundai" yaz.



araba[2] = "Hyundai"
print(araba)  # Çıktı: ['Toyota', 'Audi', 'Hyundai']
# ---------------------------------------


# 🔹 Soru 7: Listedeki eleman sayısını yazdır.



print(len(araba))  # Çıktı: 3
# ---------------------------------------


# 🔹 Soru 8: Listede "Toyota" var mı kontrol et.



print("Toyota" in araba)  # Çıktı: True
# ---------------------------------------



# 🔹 Soru 9: Listeyi döngüyle yazdır.



for marka in araba:
    print("Marka:", marka)
# Çıktı:
# Marka: Toyota
# Marka: Audi
# Marka: Hyundai
# ---------------------------------------



# 🔹 Soru 10: Sayılardan oluşan bir liste oluştur ve sırala.



sayilar = [8, 3, 1, 6, 4]
sayilar.sort()
print(sayilar)  # Çıktı: [1, 3, 4, 6, 8]
# ---------------------------------------


# 🔹 Soru 11: Listeyi tersine çevir.



sayilar.reverse()
print(sayilar)  # Çıktı: [8, 6, 4, 3, 1]
# ---------------------------------------


# 🔹 Soru 12: Listedeki tüm elemanları sil.



sayilar.clear()
print(sayilar)  # Çıktı: []
# ---------------------------------------


# 🔹 Soru 13: 1'den 5'e kadar olan sayılarla liste oluştur. 3. elemanı yazdır.



sayilar = [1, 2, 3, 4, 5]
print(sayilar[2])  # Çıktı: 3
# ---------------------------------------


# 🔹 Soru 14: "renkler" isimli bir liste oluştur. İlk 2 elemanı yazdır.



renkler = ["kırmızı", "mavi", "yeşil"]
print(renkler[:2])  # Çıktı: ['kırmızı', 'mavi']
# ---------------------------------------


# 🔹 Soru 15: Bir listeyi kopyalayıp değiştirmeden eski halini koru ve bunu yazdır. Sonrasında bu kopyaya sarı rengi ekle.



kopya_renkler = renkler.copy()
renkler.append("sarı")
print("Orijinal:", kopya_renkler)  # Çıktı: ['kırmızı', 'mavi', 'yeşil']
print("Güncel:", renkler)  # Çıktı: ['kırmızı', 'mavi', 'yeşil', 'sarı']
# ---------------------------------------


# 🔹 Soru 16: 5 elemanlı bir sayı listesi oluştur. En büyük sayıyı yazdır.



sayilar = [12, 45, 3, 22, 9]
print(max(sayilar))  # Çıktı: 45



# 🔹 Soru 17: Sayılar listesindeki en küçük sayıyı yazdır.



print(min(sayilar))  # Çıktı: 3
# ---------------------------------------


# 🔹 Soru 18: Aynı listeden ortanca (3. sıradaki) değeri yazdır.



print(sayilar[2])  # Çıktı: 3
# ---------------------------------------


# 🔹 Soru 19: "kelimeler" listesi oluştur. Her kelimeyi büyük harfli yazdır.



kelimeler = ["merhaba", "python", "liste"]
for kelime in kelimeler:
    print(kelime.upper())
# Çıktı:
# MERHABA
# PYTHON
# LISTE
# ---------------------------------------


# 🔹 Soru 20: "kelimeler" listesi oluştur. Her kelimeyi büyük harfli yazdır. Sonrasında da bu kelimeleri farklı bir liste içine al ve yazdır. 



kelimeler = ["atilay", "berke", "çetinkaya"]
buyukler = []

for i in kelimeler:
    büyük = i.upper()
    buyukler.append(büyük)

print(buyukler)
# Çıktı: ['ATILAY', 'BERKE', 'ÇETİNKAYA']
# ---------------------------------------
