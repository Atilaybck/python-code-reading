# ---------------------------------------
# 🔹 1. Tuple Oluşturma

renkler = ("kırmızı", "yeşil", "mavi")
sayilar = (1, 2, 3, 4)

# Tuple, () parantez ile tanımlanır ve listeler gibi sıralıdır ama değiştirilemez (immutable)
# ---------------------------------------



# 🔹 2. Tuple Elemanlarına Erişim

print(renkler[0])      # Çıktı: kırmızı
print(renkler[-1])     # Çıktı: mavi
# ---------------------------------------



# 🔹 3. Tuple Dilimleme (Slicing)

renkler = ("kırmızı", "yeşil", "mavi")
# Index'ler:     0         1         2

# Dilimleme: tuple[start:stop] → stop dahil edilmez

print(renkler[0:2])  
# 0. index: 'kırmızı'
# 1. index: 'yeşil'
# 2. index: alınmaz
# Çıktı: ('kırmızı', 'yeşil')

print(renkler[:2])  
# Başlangıç belirtilmemiş → 0'dan başlar
# 2. index'e kadar alır (hariç)
# Çıktı: ('kırmızı', 'yeşil')

print(renkler[1:])  
# 1. index: 'yeşil'
# 2. index: 'mavi'
# Bitiş belirtilmemiş → sona kadar devam eder
# Çıktı: ('yeşil', 'mavi')
# ---------------------------------------



# 🔹 4. Tuple’lar Neden Sabittir?

# renkler[0] = "turuncu"   # HATA: TypeError → çünkü tuple değiştirilemez
# ---------------------------------------



# 🔹 5. count() ve index()

renkler2 = ("kırmızı", "yeşil", "kırmızı", "mavi")

print(renkler2.count("kırmızı"))   # Çıktı: 2 → kaç kez geçiyor?
print(renkler2.index("mavi"))      # Çıktı: 3 → ilk geçtiği index
# ---------------------------------------



# 🔹 6. Tek Elemanlı Tuple Tanımı

tek = ("elma",)         # Virgül şart!
not_tuple = ("elma")    # Bu tuple değil, sadece string

print(type(tek))        # <class 'tuple'>
print(type(not_tuple))  # <class 'str'>
# ---------------------------------------



# 🔹 7. Tuple ile Döngü

renkler = ("kırmızı", "yeşil", "mavi")

for renk in renkler:
    print("Renk:", renk)

# Çıktı:
# Renk: kırmızı
# Renk: yeşil
# Renk: mavi
# ---------------------------------------



# 🔹 8. İç İçe Tuple (Nested)

bilgi = ("Ali", 28, ("Ankara", "Türkiye"))
print(bilgi[2])             # Çıktı: ('Ankara', 'Türkiye')
print(bilgi[2][0])          # Çıktı: Ankara
# ---------------------------------------



# 🔹 9. Tuple ve Liste Farkı
liste = [1, 2, 3]
tuple_ = (1, 2, 3)

liste[0] = 10        # Değiştirilebilir
print(liste)         # Çıktı: [10, 2, 3]

# tuple_[0] = 10     # HATA: TypeError → değiştirilemez
