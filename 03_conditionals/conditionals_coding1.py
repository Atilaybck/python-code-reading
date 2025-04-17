# conditionals_coding_ex1.py

# 🔸 Soru 1: Bir sayı negatif mi pozitif mi kontrol et



sayi = -3

if sayi > 0:
    print("Pozitif")
elif sayi < 0:
    print("Negatif")
else:
    print("Sıfır")
# Yorum: Sayı sıfırdan büyükse pozitif, küçükse negatif, değilse sıfırdır.
# Çıktı: Negatif
# ---------------------------------------


# 🔸 Soru 2: Yaş bilgisine göre sinema bileti fiyatı



yas = 12

if yas < 7:
    print("Bilet: Ücretsiz")
elif yas <= 18:
    print("Bilet: 10 TL")
else:
    print("Bilet: 20 TL")
# Yorum: Yaşa göre farklı fiyatlandırma uygulanıyor.
# Çıktı: Bilet: 10 TL
# ---------------------------------------


# 🔸 Soru 3: Kullanıcı adı kontrolü



kullanici_adi = "admin"

if kullanici_adi == "admin":
    print("Yönetici girişi başarılı.")
else:
    print("Standart kullanıcı girişi.")
# Yorum: Belirli bir kullanıcı adı için özel mesaj verildi.
# Çıktı: Yönetici girişi başarılı.
# ---------------------------------------


# 🔸 Soru 4: Sayı çift mi tek mi?



sayi = 7

if sayi % 2 == 0:
    print("Çift sayı")
else:
    print("Tek sayı")
# Yorum: Mod alma işlemiyle sayının çift/tek olduğu kontrol edildi.
# Çıktı: Tek sayı
# ---------------------------------------


# 🔸 Soru 5: Not değerlendirme



not_ort = 72

if not_ort >= 85:
    print("Not: Pekiyi")
elif not_ort >= 70:
    print("Not: İyi")
elif not_ort >= 50:
    print("Not: Orta")
else:
    print("Not: Zayıf")
# Yorum: Belirli aralıklara göre not değerlendirmesi yapıldı.
# Çıktı: Not: İyi
# ---------------------------------------


# 🔸 Soru 6: Gün ismine göre mesaj ver



gun = "Cumartesi"

if gun == "Cumartesi" or gun == "Pazar":
    print("Hafta sonu!")
else:
    print("Hafta içi.")
# Yorum: Gün bilgisine göre hafta içi / hafta sonu ayrımı yapıldı.
# Çıktı: Hafta sonu!
# ---------------------------------------


# 🔸 Soru 7: Şifre uzunluğu kontrolü



sifre = "abc123"

if len(sifre) < 6:
    print("Şifre çok kısa.")
elif len(sifre) > 12:
    print("Şifre çok uzun.")
else:
    print("Şifre kabul edildi.")
# Yorum: Şifre uzunluğuna göre kullanıcı bilgilendiriliyor.
# Çıktı: Şifre kabul edildi.
# ---------------------------------------


# 🔸 Soru 8: Alışveriş tutarına göre indirim



tutar = 350

if tutar >= 500:
    print("20% indirim kazandınız.")
elif tutar >= 300:
    print("10% indirim kazandınız.")
else:
    print("İndirim yok.")
# Yorum: Belirli tutar aralıklarına göre indirim uygulanıyor.
# Çıktı: 10% indirim kazandınız.
# ---------------------------------------


# 🔸 Soru 9: Sıcaklığa göre kıyafet önerisi



sicaklik = 5

if sicaklik <= 0:
    print("Mont giy!")
elif sicaklik <= 15:
    print("Ceket giy!")
else:
    print("Tişört yeterli.")
# Yorum: Sıcaklık derecesine göre öneri veriliyor.
# Çıktı: Ceket giy!
# ---------------------------------------


# 🔸 Soru 10: Kullanıcı giriş yapmış mı kontrol et
# Bir kullanıcı sisteme giriş yapmış mı diye kontrol etmek istiyoruz.
# Eğer giriş yapmışsa "Hoş geldiniz" mesajı gösterilecek.
# Aksi halde kullanıcıdan giriş yapması istenecek.



giris_yapildi = False

if giris_yapildi:
    print("Hoş geldiniz.")
else:
    print("Lütfen giriş yapın.")
# Yorum: Boolean değere göre kullanıcı durumu kontrol ediliyor.
# Çıktı: Lütfen giriş yapın.
# ---------------------------------------


# 🔸 Soru 11: Ay numarasına göre hangi mevsim olduğunu bul
# Kullanıcı bir ay numarası giriyor (1–12 arası).
# Bu sayıya göre yılın hangi mevsiminde olduğumuzu söyleyen bir kod yazılıyor.



ay = 4

if ay in [12, 1, 2]:
    print("Kış")
elif ay in [3, 4, 5]:
    print("İlkbahar")
elif ay in [6, 7, 8]:
    print("Yaz")
else:
    print("Sonbahar")
# Yorum: Ay numarasına göre mevsim eşleştirildi.
# Çıktı: İlkbahar
# ---------------------------------------


# 🔸 Soru 12: Sınavdan geçen öğrencileri belirle
# Öğrencinin aldığı puan 50 ve üzeriyse "Geçtiniz" yazsın.
# 50'nin altındaysa "Kaldınız" mesajı verilsin.



puan = 45

if puan >= 50:
    print("Geçtiniz")
else:
    print("Kaldınız")
# Yorum: 50 ve üzeri puan geçme olarak kabul ediliyor.
# Çıktı: Kaldınız
# ---------------------------------------


# 🔸 Soru 13: E-posta adresinde @ karakteri var mı?
# Kullanıcının girdiği e-posta adresinin geçerli olup olmadığını anlamak için
# içinde "@" karakteri olup olmadığı kontrol ediliyor.



eposta = "ornekmail.com"

if "@" in eposta:
    print("Geçerli e-posta")
else:
    print("Geçersiz e-posta")
# Yorum: E-posta geçerliliği basit kontrolle yapıldı.
# Çıktı: Geçersiz e-posta
# ---------------------------------------


# 🔸 Soru 14: Kullanıcının yaşına ve üyelik durumuna göre giriş izni ver
# Kişi hem 18 yaşından büyük olmalı hem de üyelik bilgisi True olmalı.
# İkisi de sağlanırsa giriş izni verilir.



yas = 25
uye = True

# Not: "uye" zaten True/False (bool) bir değer olduğu için, 
# if içinde doğrudan "if uye:" şeklinde kullanılabilir.
# Bu, "if uye == True:" ile aynıdır.

if yas >= 18 and uye:
    print("Giriş izni verildi.")
else:
    print("Giriş reddedildi.")
# Yorum: Hem yaş hem üyelik şartı sağlanmalı.
# Çıktı: Giriş izni verildi.
# ---------------------------------------


# 🔸 Soru 15: Ürünün stokta olup olmadığını kontrol et
# Stok miktarı 0'dan büyükse ürün vardır.
# 0 veya daha azsa stok bitmiştir mesajı yazılır.



stok = 0

if stok > 0:
    print("Ürün mevcut")
else:
    print("Stokta yok")
# Yorum: Stok miktarına göre mesaj gösterildi.
# Çıktı: Stokta yok
# ---------------------------------------


# 🔸 Soru 16: Mesaj kısa mı uzun mu kontrol et
# Mesajın karakter uzunluğu 10'dan azsa kısa mesajdır.
# Aksi halde uzun mesaj kabul edilir.



mesaj = "Merhaba!"

if len(mesaj) < 10:
    print("Kısa mesaj")
else:
    print("Uzun mesaj")
# Yorum: Mesaj uzunluğu basit bir if ile kontrol edildi.
# Çıktı: Kısa mesaj
# ---------------------------------------


# 🔸 Soru 17: Sayı 0 ile 100 aralığında mı?
# Girilen sayının 0 ile 100 arasında olup olmadığı kontrol edilir.



sayi = 105

if 0 <= sayi <= 100:
    print("Geçerli aralıkta")
else:
    print("Geçersiz sayı")
# Yorum: Aralık kontrolü için karşılaştırmalar birleştirildi.
# Çıktı: Geçersiz sayı
# ---------------------------------------


# 🔸 Soru 18: Kullanıcı adı ve şifre doğru mu kontrol et
# Kullanıcı adı ve şifre doğruysa giriş yapılır.
# Herhangi biri yanlışsa hata mesajı gösterilir.



kullanici = "ali"
sifre = "1234"

if kullanici == "ali" and sifre == "1234":
    print("Giriş başarılı")
else:
    print("Hatalı kullanıcı adı veya şifre")
# Yorum: Hem kullanıcı adı hem şifre doğru olmalı.
# Çıktı: Giriş başarılı
# ---------------------------------------


# 🔸 Soru 19: Puanı harf notuna çevir
# Öğrencinin puanına göre A, B, C ya da düşük notlardan biri verilir.



puan = 92

if puan >= 90:
    print("Harf Notu: A")
elif puan >= 80:
    print("Harf Notu: B")
elif puan >= 70:
    print("Harf Notu: C")
else:
    print("Harf Notu: D veya F")
# Yorum: Puan aralıklarına göre harf notu verildi.
# Çıktı: Harf Notu: A
# ---------------------------------------


# 🔸 Soru 20: Ücretsiz kargo hakkı kazanılmış mı kontrol et
# Eğer sepet tutarı 200 TL ve üzerindeyse ücretsiz kargo hakkı kazanılır.
# Aksi halde kargo ücreti ödenir.



sepet_tutari = 199

if sepet_tutari >= 200:
    print("Kargo ücretsiz")
else:
    print("Kargo ücreti uygulanır")
# Yorum: Belirli bir tutarın altındaki siparişlerde kargo ekleniyor.
# Çıktı: Kargo ücreti uygulanır
# ---------------------------------------

