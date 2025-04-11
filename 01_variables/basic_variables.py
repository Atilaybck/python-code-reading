# ---------------------------------------
# 🔹 1. Değişken Tanımlama (Variable Assignment)
isim = "Atılay"             # string (metin) türünde bir değişken
yas = 28                   # integer (tam sayı)
boy = 1.75                 # float (ondalıklı sayı)
aktif_mi = True            # boolean (doğru/yanlış değeri)
# ---------------------------------------


# 🔹 2. print() ile değişkenleri ekrana yazdırma
print("İsim:", isim)        # İsim: Atılay
print("Yaş:", yas)          # Yaş: 28
print("Boy:", boy)          # Boy: 1.75
print("Aktif mi?", aktif_mi)  # Aktif mi? True
# ---------------------------------------


# 🔹 3. type() ile veri tiplerini öğrenme
print("isim'in tipi:", type(isim))      # <class 'str'>
print("yas'ın tipi:", type(yas))        # <class 'int'>
print("boy'un tipi:", type(boy))        # <class 'float'>
print("aktif_mi'nin tipi:", type(aktif_mi))  # <class 'bool'>
# ---------------------------------------


# 🔹 4. Tek Satırda Çoklu Değişken Atama
a, b, c = 10, 20, 30
print("a:", a, "b:", b, "c:", c)         # a: 10 b: 20 c: 30
# ---------------------------------------


# 🔹 5. Type Casting (Veri Tipi Dönüştürme)

x = "123"           # string
y = int(x)          # string → int (123)
z = float(x)        # string → float (123.0)
t = str(yas)        # int → string ("28")

print("x:", x, "→", type(x))             # x: 123 → <class 'str'>
print("y:", y, "→", type(y))             # y: 123 → <class 'int'>
print("z:", z, "→", type(z))             # z: 123.0 → <class 'float'>
print("t:", t, "→", type(t))             # t: 28 → <class 'str'>
# ---------------------------------------


# 🔹 6. Sabit Tanımlama (Conventionally Constants)

PI = 3.14159     # Python’da sabit yoktur ama büyük harf kullanarak bu değişkenin sabit olduğu belirtilir
print("PI:", PI)   # PI: 3.14159
# ---------------------------------------


# 🔹 7. None Tipi (Boş Değer)

not_eksi = None
print("not_eksi:", not_eksi)            # not_eksi: None
print("not_eksi'nin tipi:", type(not_eksi))  # <class 'NoneType'>
# ---------------------------------------


# 🔹 8. Değişken İsimlendirme Kuralları

# ✅ Geçerli örnekler
user_name = "Ali"
_userAge = 30
user2 = "Zeynep"

# ❌ Geçersiz örnekler (bunları kullanma!)
# 2user = "Ayşe"   # Rakamla başlayamaz
# user-name = "Kemal"   # Tire (-) içeremez
# Türkçe karakterler kullanma: yaş = 20 → yerine yas kullan
# ---------------------------------------


# 🔹 9. isinstance() ile veri türü kontrolü

# isinstance(deger, veri_tipi) → True ya da False döner

# isim değişkeni bir 'str' (string) mi?
print(isinstance(isim, str))       # True → çünkü "Atılay" bir string

# yas değişkeni bir 'float' mı?
print(isinstance(yas, float))      # False → çünkü 28 bir integer (int), float değil

# boy değişkeni bir 'float' mı?
print(isinstance(boy, float))      # True → çünkü 1.75 bir float

# aktif_mi değişkeni bir 'bool' (boolean) mu?
print(isinstance(aktif_mi, bool))  # True → çünkü değeri True ve bu bool veri tipidir
# ---------------------------------------



# 🔹 10. id() Fonksiyonu (Bellekteki adresi öğrenme)
x = "Python"
print("x değişkeninin bellekteki yeri:", id(x))  # Örn: 140726702938096

# Aynı değere sahip değişkenler, aynı adrese sahip olabilir:
y = "Python"
print("x ve y aynı adreste mi?", id(x) == id(y))  # True
# ---------------------------------------


# 🔹 11. Değişken Gölgeleme (Overwriting)
degisken = 10
print(degisken, type(degisken))   # 10 <class 'int'>

degisken = "on"
print(degisken, type(degisken))   # on <class 'str'>

# Aynı isimli değişken yeniden tanımlanabilir.
# Bu esneklik, dinamik tipli dillerin (gibi Python) özelliklerindendir.