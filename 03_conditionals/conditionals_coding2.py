# 🔸 Soru 21: Girilen iki sayıdan hangisi daha büyük?
# Kullanıcıdan alınan iki sayıdan hangisinin büyük olduğunu karşılaştır.
# Eğer eşitse "Sayılar eşit" mesajı ver.



sayi1 = 15
sayi2 = 20

if sayi1 > sayi2:
    print("Birinci sayı daha büyük:", sayi1)
elif sayi2 > sayi1:
    print("İkinci sayı daha büyük:", sayi2)
else:
    print("Sayılar eşit.")
# Yorum: Büyük olan sayı ya da eşitlik durumu kontrol edildi.
# Çıktı: İkinci sayı daha büyük: 20
# ---------------------------------------


# 🔸 Soru 22: Giriş yapılan saat bilgisine göre selamlama mesajı ver
# Eğer saat 0–11 arasıysa günaydın, 12–17 arasıysa tünaydın, diğer durumlarda iyi akşamlar yazdır.



saat = 14

if saat < 12:
    print("Günaydın!")
elif saat < 18:
    print("Tünaydın!")
else:
    print("İyi akşamlar!")
# Yorum: Saat aralıklarına göre uygun selamlama verildi.
# Çıktı: Tünaydın!
# ---------------------------------------


# 🔸 Soru 23: Üç kenar uzunluğu verilen değerlerden üçgen oluşur mu?
# Üçgen oluşturma şartı: Her iki kenarın toplamı, üçüncü kenardan büyük olmalı.



a = 5
b = 6
c = 10

if a + b > c and a + c > b and b + c > a:
    print("Bu kenarlarla üçgen çizilebilir.")
else:
    print("Bu kenarlarla üçgen çizilemez.")
# Yorum: Üçgen kuralları doğru şekilde uygulandı.
# Çıktı: Bu kenarlarla üçgen çizilebilir.
# ---------------------------------------


# 🔸 Soru 24: Girilen sayı hem 3 hem 5’e bölünüyor mu?
# Eğer her ikisine bölünüyorsa mesaj yaz, sadece birine bölünüyorsa ona özel mesaj ver, ikisine de bölünmüyorsa belirt.



sayi = 30

if sayi % 3 == 0 and sayi % 5 == 0:
    print("Sayı hem 3'e hem 5'e bölünür.")
elif sayi % 3 == 0:
    print("Sayı sadece 3'e bölünür.")
elif sayi % 5 == 0:
    print("Sayı sadece 5'e bölünür.")
else:
    print("Sayı 3'e veya 5'e bölünmez.")
# Yorum: Mod işlemi ile çoklu koşullar kontrol edildi.
# Çıktı: Sayı hem 3'e hem 5'e bölünür.
# ---------------------------------------


# 🔸 Soru 25: Parola ve tekrar parolası aynı mı?
# Kullanıcı kayıt olurken girdiği iki parolanın birbirine eşit olup olmadığını kontrol et.



parola = "abc123"
tekrar = "abc123"

if parola == tekrar:
    print("Parolalar eşleşti.")
else:
    print("Parolalar farklı!")
# Yorum: String eşitliği ile doğrulama yapıldı.
# Çıktı: Parolalar eşleşti.
# ---------------------------------------


# 🔸 Soru 26: Sıcaklık değerine göre suyun hali nedir?
# Sıcaklık 0'ın altındaysa su donmuş, 100'ün üstündeyse buharlaşmış, aradaysa sıvı haldedir.



sicaklik = 25

if sicaklik <= 0:
    print("Su donmuş halde.")
elif sicaklik >= 100:
    print("Su buhar halinde.")
else:
    print("Su sıvı halde.")
# Yorum: Fiziksel sıcaklık aralıklarına göre suyun hali belirlendi.
# Çıktı: Su sıvı halde.
# ---------------------------------------


# 🔸 Soru 27: Girilen yıl artık yıl mı?
# Kural: 4’e tam bölünen ama 100’e tam bölünmeyen yıllar artık yıldır.
# Ancak 400’e tam bölünüyorsa yine artık yıldır.



yil = 2024

if (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0):
    print("Artık yıl.")
else:
    print("Artık yıl değil.")
# Yorum: Artık yıl kuralları doğrulandı.
# Çıktı: Artık yıl.
# ---------------------------------------


# 🔸 Soru 28: Kullanıcının puanına göre rozet belirle
# 0–49: Bronz, 50–79: Gümüş, 80–100: Altın



puan = 83

if puan >= 80:
    print("Altın rozet kazandınız!")
elif puan >= 50:
    print("Gümüş rozet kazandınız!")
else:
    print("Bronz rozet kazandınız.")
# Yorum: Puan aralığına göre kullanıcıya ödül rozeti verildi.
# Çıktı: Altın rozet kazandınız!
# ---------------------------------------


# 🔸 Soru 29: Yaş grubuna göre etiket ver
# 0–12: Çocuk, 13–17: Genç, 18–64: Yetişkin, 65+: Yaşlı



yas = 30

if yas <= 12:
    print("Çocuk")
elif yas <= 17:
    print("Genç")
elif yas <= 64:
    print("Yetişkin")
else:
    print("Yaşlı")
# Yorum: Yaşa göre sınıflandırma yapıldı.
# Çıktı: Yetişkin
# ---------------------------------------


# 🔸 Soru 30: Doğru cevap sayısına göre sınav sonucu ver
# 20 soruluk sınavda:
# 16–20 doğru: Başarılı
# 10–15 doğru: Orta
# 0–9 doğru: Başarısız

dogru_sayisi = 12

if dogru_sayisi >= 16:
    print("Sonuç: Başarılı")
elif dogru_sayisi >= 10:
    print("Sonuç: Orta")
else:
    print("Sonuç: Başarısız")
# Yorum: Doğru cevap sayısına göre sınav sonucu yazıldı.
# Çıktı: Sonuç: Orta
# ---------------------------------------


# 🔸 Soru 31: Kullanıcının yaptığı alışverişin VIP olup olmadığını kontrol et
# 1000 TL ve üzeri alışveriş yapan kullanıcıya "VIP müşteri" mesajı ver.



alisveris_tutari = 1250

if alisveris_tutari >= 1000:
    print("VIP müşteri")
else:
    print("Standart müşteri")
# Yorum: Belirli bir harcama eşiğine göre müşteri türü belirlendi.
# Çıktı: VIP müşteri
# ---------------------------------------


# 🔸 Soru 32: Günlük adım sayısına göre geri bildirim ver
# 10.000 ve üzeri: Harika!
# 5.000–9.999: İyi gidiyorsun!
# 5.000'in altı: Daha fazla hareket etmelisin.

adim_sayisi = 4500

if adim_sayisi >= 10000:
    print("Harika! Hedefine ulaştın.")
elif adim_sayisi >= 5000:
    print("İyi gidiyorsun, az kaldı.")
else:
    print("Daha fazla hareket etmelisin.")
# Yorum: Günlük adım sayısına göre motivasyon mesajı verildi.
# Çıktı: Daha fazla hareket etmelisin.
# ---------------------------------------


# 🔸 Soru 33: Kullanıcıdan alınan şikayet puanına göre değerlendirme yap
# 1–2: Çok kötü, 3–4: Orta, 5: İyi


puan = 4

if puan == 5:
    print("Mükemmel hizmet!")
elif puan >= 3:
    print("İdare eder.")
else:
    print("Memnun kalınmadı.")
# Yorum: Puan aralığına göre hizmet memnuniyeti belirlendi.
# Çıktı: İdare eder.
# ---------------------------------------


# 🔸 Soru 34: Girilen şifre hem harf hem sayı içeriyor mu?
# Eğer şifre hem harf hem sayı barındırıyorsa kabul edilir.


sifre = "abc123"

if any(harf.isalpha() for harf in sifre) and any(harf.isdigit() for harf in sifre):
    print("Şifre geçerli.")
else:
    print("Şifre hem harf hem sayı içermeli.")
# Yorum: Karakter türleri kontrol edilerek geçerlilik sağlandı.
# Çıktı: Şifre geçerli.
# ---------------------------------------


# 🔸 Soru 35: Kullanıcı doğum yılına göre yaşını hesapla ve reşitlik kontrolü yap
# Eğer kullanıcı 18 yaşından büyükse "Reşitsiniz" yaz, değilse "Reşit değilsiniz".



dogum_yili = 2008
mevcut_yil = 2025
yas = mevcut_yil - dogum_yili

if yas >= 18:
    print("Reşitsiniz.")
else:
    print("Reşit değilsiniz.")
# Yorum: Yaş hesaplandıktan sonra reşitlik kontrolü yapıldı.
# Çıktı: Reşit değilsiniz.
# ---------------------------------------
