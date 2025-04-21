# ---------------------------------------
# 🔹 File Handling Nedir?

# File handling, Python ile dosya açma, okuma, yazma, oluşturma ve düzenleme işlemidir.

# Bilgisayardaki .txt, .csv gibi dosyalarla çalışmamızı sağlar.

# ✅ Ne işe yarar?
# - Kullanıcı verilerini dosyaya kaydetmek
# - Notları bir .txt dosyasına yazmak
# - Bir log dosyasına bilgi eklemek
# - Dış kaynaklı verileri analiz etmek

# ---------------------------------------

# ✅ Neden önemlidir?
# - Verileri kalıcı hale getirir (bellekte değil, diskte saklar)
# - Uygulamalarda kullanıcı verileri bu şekilde saklanır
# - Otomasyon ve veri işleme işlemlerinde temel bir adımdır

# Şimdi open(), read(), write() gibi fonksiyonlarla nasıl dosya işlemleri yapılır, onları göreceğiz.

# ---------------------------------------

# Bunlar Nerede Kullanılır Bir Örnek Verelim:

# 📌 Senaryo: Günlük Tutma Uygulaması

# Zeynep adında bir kullanıcı var. Her akşam bilgisayarını açıyor
# ve Python ile yazdığı küçük günlük uygulamasını çalıştırıyor.

# Program ona şöyle soruyor:
# "Bugün nasıl geçti?"

# Zeynep yazıyor:
# "Bugün hava çok güzeldi. Kitap okudum ve yürüyüşe çıktım."

# Bu yazdığı metin, bilgisayarında bir dosyaya kaydediliyor.
# Böylece ertesi gün tekrar açtığında, daha önce ne yazdığını okuyabiliyor.

# Kod aşağıda 👇
gunluk = input("Bugün nasıl geçti? ")

with open("gunluk.txt", "a") as dosya:
    dosya.write(gunluk + "\n")

print("Günlüğün kaydedildi!")

# ---------------------------------------

# Başka bir gün Zeynep uygulamayı tekrar açıyor
# ve önceki yazdıklarını okumak istiyor:

with open("gunluk.txt", "r") as dosya:
    print("📖 Önceki Günlükler:")
    print(dosya.read())

# ---------------------------------------

# ✅ Sonuç:
# Zeynep artık her gün düşüncelerini yazıyor.
# Yazdıkları bilgisayarında 'gunluk.txt' dosyasında saklanıyor.
# Uygulama kapansa bile veriler silinmiyor.

# İşte bu yüzden "file handling" önemli!


# ---------------------------------------
# 🔹 1. Dosya Açma (open)

# open() fonksiyonu bir dosyayı açar.
# "r" = read (okuma)
# "w" = write (yazma, varsa siler)
# "a" = append (sonuna ekleme)
# "x" = create (dosya yoksa oluşturur)

# Örnek: dosya.txt dosyasını okuma modunda aç
dosya = open("dosya.txt", "r")  # sadece okuma için açar
print(dosya.read())             # içeriği ekrana yazar
dosya.close()                   # dosyayı kapatır

# ---------------------------------------


# 🔹 2. Dosyaya Yazma (write)

# "w" modu: Dosya varsa içeriği siler, yoksa oluşturur
yeni_dosya = open("notlar.txt", "w")
yeni_dosya.write("Bugün Python dosya işlemlerini öğrendim.")
yeni_dosya.close()

# ---------------------------------------


# 🔹 3. Dosyaya Ekleme (append)

# "a" modu: Dosyanın SONUNA ekler, silmez
ekle = open("notlar.txt", "a")
ekle.write("\nYeni bir satır daha ekledim.")
ekle.close()

# ---------------------------------------


# 🔹 4. Dosya Satır Satır Okuma

dosya = open("notlar.txt", "r")
for satir in dosya:
    print(satir.strip())  # strip() → boşluk/satır sonunu temizler
dosya.close()

# ---------------------------------------


# 🔹 5. with Açılışı (Otomatik Kapatma)

# Dosyayı açar, iş bitince otomatik kapatır (close gerekmez)
with open("notlar.txt", "r") as f:
    icerik = f.read()
    print(icerik)

# ---------------------------------------


# 🔹 6. read(), readline(), readlines()

# read() → tüm içeriği okur
# readline() → tek satır okur
# readlines() → tüm satırları liste olarak verir

with open("notlar.txt", "r") as f:
    print(f.readline())     # ilk satır
    print(f.readlines())    # kalan tüm satırları liste olarak verir

# ---------------------------------------
# ✅ Özet:
# - open("dosya.txt", "r/w/a") ile dosya açılır
# - .read(), .write(), .readline(), .readlines() ile içerik işlenir
# - with open(...) as ...: → otomatik kapanan güvenli yöntem
