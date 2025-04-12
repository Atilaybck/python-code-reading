# ---------------------------------------
# 🔹 1. Sözlük Oluşturma (Dictionary)

ogrenci = {
    "ad": "Ali",
    "soyad": "Yılmaz",
    "yas": 21,
    "aktif": True
}

# Sözlükler süslü parantez {} ile tanımlanır.
# Her eleman "anahtar": değer şeklindedir.
# ---------------------------------------



# 🔹 2. Değerlere Erişim

print(ogrenci["ad"])     # Çıktı: Ali

# get() metodu ile hata almadan erişim yapılabilir
print(ogrenci.get("yas"))        # Çıktı: 21
print(ogrenci.get("okul", "Bilinmiyor"))  # Çıktı: Bilinmiyor (default değer)
# ---------------------------------------



# 🔹 3. Eleman Ekleme ve Güncelleme

ogrenci["okul"] = "Anadolu Lisesi"       # yeni ekleme
ogrenci["yas"] = 22                      # mevcut değeri güncelleme

print(ogrenci)
# Çıktı:
# {'ad': 'Ali', 'soyad': 'Yılmaz', 'yas': 22, 'aktif': True, 'okul': 'Anadolu Lisesi'}
# ---------------------------------------



# 🔹 4. Eleman Silme

ogrenci.pop("aktif")       # 'aktif' anahtarını siler
print(ogrenci)

# del komutu ile de silinebilir:
del ogrenci["soyad"]
print(ogrenci)

# Çıktı:
# {'ad': 'Ali', 'yas': 22, 'okul': 'Anadolu Lisesi'}
# ---------------------------------------



# 🔹 5. keys(), values(), items()

print(ogrenci.keys())      # Çıktı: dict_keys(['ad', 'yas', 'okul'])
print(ogrenci.values())    # Çıktı: dict_values(['Ali', 22, 'Anadolu Lisesi'])
print(ogrenci.items())     # Çıktı: dict_items([('ad', 'Ali'), ('yas', 22), ('okul', 'Anadolu Lisesi')])
# ---------------------------------------



# 🔹 6. Döngü ile Sözlükte Gezinme

for anahtar in ogrenci:
    print("Anahtar:", anahtar, "→ Değer:", ogrenci[anahtar])

# Çıktı:
# Anahtar: ad → Değer: Ali
# Anahtar: yas → Değer: 22
# Anahtar: okul → Değer: Anadolu Lisesi

# items() ile key ve value birlikte alınabilir:
for k, v in ogrenci.items():
    print(f"{k} → {v}")

# Çıktı:
# ad → Ali
# yas → 22
# okul → Anadolu Lisesi
# ---------------------------------------



# 🔹 7. in ile Anahtar Kontrolü

print("yas" in ogrenci)       # Çıktı: True
print("soyad" in ogrenci)     # Çıktı: False

# ---------------------------------------



# 🔹 8. clear(), copy()

kopya = ogrenci.copy()
print("Kopya sözlük:", kopya)

ogrenci.clear()
print("Temizlenmiş sözlük:", ogrenci)

# Çıktı:
# Kopya sözlük: {'ad': 'Ali', 'yas': 22, 'okul': 'Anadolu Lisesi'}
# Temizlenmiş sözlük: {}
