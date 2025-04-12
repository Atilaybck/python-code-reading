# ---------------------------------------
# 🔹 1. Liste Oluşturma

meyveler = ["elma", "armut", "muz"]
sayilar = [1, 2, 3, 4, 5]
karisik = ["elma", 3, True]

# ---------------------------------------
# 🔹 2. Liste Elemanlarına Erişim

print(meyveler[0])     # Çıktı: elma
print(meyveler[-1])    # Çıktı: muz

# ---------------------------------------
# 🔹 3. Liste Dilimleme (slicing)

print(meyveler[0:2])   # Çıktı: ['elma', 'armut']
print(meyveler[:2])    # Çıktı: ['elma', 'armut']
print(meyveler[1:])    # Çıktı: ['armut', 'muz']

# ---------------------------------------
# 🔹 4. Listeye Eleman Ekleme

meyveler.append("çilek")
print(meyveler)        # Çıktı: ['elma', 'armut', 'muz', 'çilek']

meyveler.insert(1, "kiraz")
print(meyveler)        # Çıktı: ['elma', 'kiraz', 'armut', 'muz', 'çilek']

# ---------------------------------------
# 🔹 5. Eleman Silme

# remove(): değere göre siler
meyveler.remove("muz")
print(meyveler)        # Çıktı: ['elma', 'kiraz', 'armut', 'çilek']

# pop(): son elemanı siler ve döner
son = meyveler.pop()
print("Çıkan eleman:", son)      # Çıktı: Çıkan eleman: çilek
print(meyveler)                  # Çıktı: ['elma', 'kiraz', 'armut']

# del: index'e göre siler
del meyveler[1]
print(meyveler)                  # Çıktı: ['elma', 'armut']

# ---------------------------------------


# 🔹 6. Eleman Değiştirme
sayilar[2] = 10
print(sayilar)                   # Çıktı: [1, 2, 10, 4, 5]

# ---------------------------------------


# 🔹 7. Liste Uzunluğu 
print(len(sayilar))              # Çıktı: 5

# ---------------------------------------


# 🔹 8. Liste İçinde Arama

print("armut" in meyveler)       # Çıktı: True
print("muz" not in meyveler)     # Çıktı: True

# ---------------------------------------

# 🔹 9. Döngü ile Liste Üzerinde Gezinme

for meyve in meyveler:
    print("Meyve:", meyve)

# Çıktı:
# Meyve: elma
# Meyve: armut

# ---------------------------------------
# 🔹 10. Liste Metotları

sayilar = [4, 2, 1, 5, 3]

sayilar.sort()
print("Sıralı:", sayilar)        # Çıktı: [1, 2, 3, 4, 5]

sayilar.reverse()
print("Ters:", sayilar)          # Çıktı: [5, 4, 3, 2, 1]

kopya = sayilar.copy()
print("Kopya:", kopya)           # Çıktı: [5, 4, 3, 2, 1]

sayilar.clear()
print("Temizlenmiş liste:", sayilar)  # Çıktı: []
