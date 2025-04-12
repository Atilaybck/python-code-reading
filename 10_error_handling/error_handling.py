# ---------------------------------------
# 🔹 Temel try / except Örneği

try:
    sayi = int(input("Bir sayı girin: "))
    print("Girilen sayı:", sayi)
except:
    print("Hata oluştu! Lütfen geçerli bir sayı girin.")

# ---------------------------------------
# 🔍 Örnek Çıktılar:

# 👉 Durum 1: Kullanıcı geçerli bir sayı girerse
# Girdi:
# Bir sayı girin: 42
# Çıktı:
# Girilen sayı: 42

# 👉 Durum 2: Kullanıcı geçersiz bir değer girerse
# Girdi:
# Bir sayı girin: abc
# Çıktı:
# Hata oluştu! Lütfen geçerli bir sayı girin.

# Açıklama:
# - `int("42")` başarılıdır → except çalışmaz
# - `int("abc")` ValueError verir → except bloğu devreye girer
# ---------------------------------------


# ✅ Ekstra Örnek:

try:
    sonuc = 5 / 0
except:
    print("Bir hata oluştu!")  # Çıktı: Bir hata oluştu!

# Bu kullanımda hangi hatanın oluştuğu belirtilmez.
# Daha profesyonel kullanım için hata türünü yakalamak gerekir.
# ---------------------------------------

# 🔹 2. Belirli Hata Türlerini Yakalama

# Hangi türde hata bekliyorsak, ona özel 'except' kullanabiliriz.

try:
    print(10 / 0)
except ZeroDivisionError:
    print("Hata: Sıfıra bölme yapılamaz!")  # Çıktı: Hata: Sıfıra bölme yapılamaz!

try:
    sayi = int("abc")
except ValueError:
    print("Hata: Geçersiz sayı!")  # Çıktı: Hata: Geçersiz sayı!
# ---------------------------------------


# ✅ Ekstra Örnek:

try:
    liste = [1, 2, 3]
    print(liste[5])
except IndexError:
    print("Hata: Liste dışında bir index çağrıldı.")  # Çıktı: Hata: Liste dışında...
# ---------------------------------------

# 🔹 3. else ve finally Kullanımı

# else → Hata yoksa çalışır
# finally → Her durumda çalışır (hata olsa da)

try:
    x = int(input("Bir sayı girin: "))
except ValueError:
    print("Hata: Geçersiz sayı.")
else:
    print("Başarılı giriş:", x)
finally:
    print("İşlem tamamlandı.")  # Her zaman çalışır
# ---------------------------------------


# ✅ Ekstra Örnek:

try:
    print("Kod çalışıyor...")
except:
    print("Hata oluştu!")
else:
    print("Hiçbir hata yok.")  # Çıktı: Kod çalışıyor... → Hiçbir hata yok.
finally:
    print("Kodun sonuna gelindi.")  # Her zaman çalışır
# ---------------------------------------



# 🔹 4. raise ile Hata Fırlatma (Kendi hatamızı oluşturmak)

def bol(a, b):
    if b == 0:
        raise ZeroDivisionError("Sıfıra bölünemez!")  # manuel hata
    return a / b

try:
    bol(10, 0)
except ZeroDivisionError as hata:
    print("Yakalanan hata:", hata)
# Çıktı: Yakalanan hata: Sıfıra bölünemez!
# ---------------------------------------




# 🔹 5. Dosya Hatası (Gerçek Hayat Örneği)

try:
    with open("veri.txt", "r") as dosya:
        print(dosya.read())
except FileNotFoundError:
    print("Hata: Dosya bulunamadı!")

# Dosya yoksa program hata vermez, except'e düşer.
# ---------------------------------------




# 🔹 6. Çoklu except Kullanımı

try:
    sayi = int(input("Bir sayı girin: "))
    print("Sonuç:", 10 / sayi)
except ValueError:
    print("Hata: Sayı girmelisin!")
except ZeroDivisionError:
    print("Hata: Sıfıra bölme yapılamaz.")

# ---------------------------------------
# ✅ Ekstra: Hata mesajını yakalamak

try:
    1 / 0
except ZeroDivisionError as e:
    print("Hata mesajı:", e)  # Çıktı: Hata mesajı: division by zero

# ---------------------------------------

# 🔍 Özet:
# try     → hata olabilecek kodlar
# except  → hata varsa burası çalışır
# else    → hata yoksa çalışır
# finally → her durumda çalışır
# raise   → manuel hata fırlatma
