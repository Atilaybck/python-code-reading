# ---------------------------------------
# 🔹 1. Aritmetik Operatörler
a = 10
b = 3

print("Toplama:", a + b)          # Toplama: 13
print("Çıkarma:", a - b)          # Çıkarma: 7
print("Çarpma:", a * b)           # Çarpma: 30
print("Bölme:", a / b)            # Bölme: 3.3333333333333335
print("Tam bölme:", a // b)       # Tam bölme: 3
print("Mod alma:", a % b)         # Mod alma: 1
print("Üs alma:", a ** b)         # Üs alma: 1000
# ---------------------------------------



# 🔹 2. Karşılaştırma Operatörleri
x = 5
y = 10

print("x == y:", x == y)          # x == y: False
print("x != y:", x != y)          # x != y: True
print("x > y:", x > y)            # x > y: False
print("x < y:", x < y)            # x < y: True
print("x >= 5:", x >= 5)          # x >= 5: True
print("y <= 10:", y <= 10)        # y <= 10: True
# ---------------------------------------



# 🔹 3. Mantıksal Operatörler
s1 = True
s2 = False

print("s1 and s2:", s1 and s2)    # s1 and s2: False
print("s1 or s2:", s1 or s2)      # s1 or s2: True
print("not s1:", not s1)          # not s1: False

# Gerçek örnek:
yas = 20
uygun = yas >= 18 and yas <= 30
print("Yaş uygun mu?", uygun)     # Yaş uygun mu?: True
# ---------------------------------------



# 🔹 4. Atama Operatörleri
sayi = 10
sayi += 5
print("+= sonrası:", sayi)        # += sonrası: 15

sayi *= 2
print("*= sonrası:", sayi)        # *= sonrası: 30

sayi -= 10
print("-= sonrası:", sayi)        # -= sonrası: 20

sayi /= 4
print("/= sonrası:", sayi)        # /= sonrası: 5.0
# ---------------------------------------



# 🔹 5. Kimlik Operatörleri (is / is not)

# a ve b aynı listeyi gösterir (aynı nesne)
a = [1, 2, 3]
b = a

# c, içeriği aynı olan ama farklı bir nesne
c = [1, 2, 3]

# == → içerik aynı mı?
print("a == b:", a == b)        # a == b: True
print("a == c:", a == c)        # a == c: True

# is → aynı nesne mi? (bellekteki adres)
print("a is b:", a is b)        # a is b: True → çünkü b = a
print("a is c:", a is c)        # a is c: False → çünkü c yeni bir liste

# is not → aynı nesne değil mi?
print("a is not c:", a is not c)  # a is not c: True

# ---------------------------------------
# 🔍 Açıklama:
# '==' içerikleri karşılaştırır. [1, 2, 3] == [1, 2, 3] → True
# 'is' ise nesnelerin bellekteki yerini karşılaştırır.
# a ve b aynı nesneye işaret ettiği için 'a is b' → True
# a ve c içerik olarak aynı olsa da farklı nesneler → 'a is c' → False

# Dilersen id() fonksiyonu ile bellek adreslerini görebilirsin:
print("id(a):", id(a))     # Örnek: 140706790058240
print("id(b):", id(b))     # Aynı: 140706790058240
print("id(c):", id(c))     # Farklı: 140706790059328

# ---------------------------------------
# 🔹 6. Üyelik Operatörleri (in / not in)
meyveler = ["elma", "armut", "muz"]

print("elma in meyveler:", "elma" in meyveler)             # elma in meyveler: True
print("çilek not in meyveler:", "çilek" not in meyveler)   # çilek not in meyveler: True
