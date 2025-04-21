# lambda_functions.py

# ---------------------------------------
# 🔹 Lambda Function Nedir?

# Lambda, Python'da küçük ve isimsiz (anonim) fonksiyonlar tanımlamak için kullanılır.

# Normalde bir fonksiyon tanımlamak için "def" kullanırız:
def topla(a, b):
    return a + b

print(topla(2, 3))  # Çıktı: 5

# Ama bu işlemi çok kısa bir şekilde lambda ile de yapabiliriz:
topla_lambda = lambda a, b: a + b
print(topla_lambda(2, 3))  # Çıktı: 5

# 🔍 Açıklama:
# lambda a, b: a + b
# - a, b → parametreler
# - a + b → fonksiyonun yaptığı işlem
# - lambda ifadesi, bu işlemi bir isim vermeden tanımlar
# - top-level'de topla_lambda ismini biz veriyoruz

# ✅ Lambda fonksiyonlar genellikle:
# - Tek satırlık fonksiyonlar içindir
# - map(), filter(), sort() gibi fonksiyonlarla birlikte sıkça kullanılır
# - Kodun daha sade ve kısa olmasını sağlar
# ---------------------------------------

#Gerçek Hayattan Küçük Bir Seneryo:

# 🔹 Senaryo: Bir liste var, her sayının karesini almak istiyoruz

sayilar = [1, 2, 3, 4, 5]

# Normal yöntem:
def kare_al(x):
    return x ** 2

kareler = list(map(kare_al, sayilar))
print(kareler)  # Çıktı: [1, 4, 9, 16, 25]

# Lambda ile:
kareler_lambda = list(map(lambda x: x ** 2, sayilar))
print(kareler_lambda)  # Çıktı: [1, 4, 9, 16, 25]

# 🔍 Açıklama:
# map() → listedeki her elemana belirli bir işlemi UYGULAR

# map() bu senaryoda ne yapıyor?

# 1. sayilar = [1, 2, 3, 4, 5] → elimizde bir sayı listesi var

# 2. lambda x: x ** 2 → bu fonksiyon, verilen sayının karesini alıyor

# 3. map(lambda x: x ** 2, sayilar)
#    → listedeki her sayıyı sırayla alıyor ve karesini hesaplıyor:
#       - 1 → 1*1 = 1
#       - 2 → 2*2 = 4
#       - 3 → 3*3 = 9
#       - 4 → 4*4 = 16
#       - 5 → 5*5 = 25

# 4. Bu sonuçları map() fonksiyonu verir, ama liste değildir
#    → Bu yüzden list(...) içine alarak sonuçları listeye çeviriyoruz

# 📌 Sonuç:
# [1, 4, 9, 16, 25] → yani her sayının karesi olan yeni bir liste

# map(), listedeki her elemanı TEK TEK alıp verdiğin işlemi uygulayan bir araçtır.
# Döngü yazmadan hızlıca işlem yapmamıza olanak sağlar.

