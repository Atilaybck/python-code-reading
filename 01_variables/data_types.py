# ---------------------------------------
# 🔹 1. int (Integer) – Tam Sayılar
sayi1 = 10
sayi2 = -45
print("sayi1:", sayi1, "→", type(sayi1))   # sayi1: 10 → <class 'int'>
print("sayi2:", sayi2, "→", type(sayi2))   # sayi2: -45 → <class 'int'>

# ---------------------------------------
# 🔹 2. float – Ondalıklı Sayılar
pi = 3.14
boy = 1.82
print("pi:", pi, "→", type(pi))           # pi: 3.14 → <class 'float'>
print("boy:", boy, "→", type(boy))        # boy: 1.82 → <class 'float'>

# ---------------------------------------
# 🔹 3. str (String) – Metin
isim = "Atılay"
mesaj = 'Merhaba'
print("isim:", isim, "→", type(isim))     # isim: Atılay → <class 'str'>
print("mesaj:", mesaj, "→", type(mesaj))  # mesaj: Merhaba → <class 'str'>

# Çok satırlı string
cok_satirli = """Bu bir
çok satırlı
string örneğidir."""
print("cok_satirli:", cok_satirli, "→", type(cok_satirli))  
# <class 'str'>

# ---------------------------------------
# 🔹 4. bool (Boolean) – Doğru / Yanlış
aktif = True
admin = False
print("aktif:", aktif, "→", type(aktif))    # aktif: True → <class 'bool'>
print("admin:", admin, "→", type(admin))    # admin: False → <class 'bool'>

# ---------------------------------------
# 🔹 5. NoneType – Boş Değer
sonuc = None
print("sonuc:", sonuc, "→", type(sonuc))    # sonuc: None → <class 'NoneType'>

# ---------------------------------------
# 🔹 6. complex – Karmaşık Sayılar
sayi_karma = 3 + 4j
print("sayi_karma:", sayi_karma, "→", type(sayi_karma))  # 3+4j → <class 'complex'>

# Gerçek ve sanal kısmı ayrı alınabilir:
print("Gerçek kısmı:", sayi_karma.real)     # 3.0
print("Sanal kısmı:", sayi_karma.imag)      # 4.0

# ---------------------------------------
# 🔹 7. isinstance() ile Tür Kontrolü

print(isinstance(boy, float))        # True
print(isinstance(mesaj, str))        # True
print(isinstance(aktif, int))        # True → çünkü bool, int sınıfından türemiştir!
print(isinstance(sonuc, type(None))) # True → NoneType kontrolü

# ---------------------------------------
# 🔹 8. Ekstra: Sayısal Türler Arası Dönüşüm

sayi = 5
print("int:", sayi, "→", type(sayi))       # int: 5 → <class 'int'>

sayi = float(sayi)
print("float:", sayi, "→", type(sayi))     # float: 5.0 → <class 'float'>

sayi = complex(sayi)
print("complex:", sayi, "→", type(sayi))   # complex: (5+0j) → <class 'complex'>
