# ---------------------------------------
# 🔹 1. Basit if koşulu

sayi = 10

if sayi > 5:
    print("Sayı 5'ten büyüktür.")  # Çıktı: Sayı 5'ten büyüktür.

# ---------------------------------------
# 🔹 2. if-else yapısı

yas = 16

if yas >= 18:
    print("Reşitsiniz.")
else:
    print("Reşit değilsiniz.")  # Çıktı: Reşit değilsiniz.

# ---------------------------------------
# 🔹 3. elif (else if) yapısı

hava = "kapalı"

if hava == "güneşli":
    print("Güneş gözlüğünü tak.")
elif hava == "yağmurlu":
    print("Şemsiyeni al.")
elif hava == "kapalı":
    print("Hava biraz kararsız.")  # Çıktı: Hava biraz kararsız.
else:
    print("Hava durumunu bilmiyorum.")

# ---------------------------------------
# 🔹 4. İç içe koşullar (Nested if)

puan = 85

if puan >= 50:
    if puan >= 80:
        print("Notunuz: Pekiyi")  # Çıktı: Notunuz: Pekiyi
    else:
        print("Notunuz: Orta")
else:
    print("Kaldınız")

# ---------------------------------------
# 🔹 5. Tek satırda if (Ternary if)

sayi = 8
print("Çift sayı") if sayi % 2 == 0 else print("Tek sayı")  # Çıktı: Çift sayı

# ---------------------------------------
# 🔹 6. Boolean ifadelerle koşul

kullanici_aktif = True

if kullanici_aktif:
    print("Kullanıcı aktif.")  # Çıktı: Kullanıcı aktif.
else:
    print("Kullanıcı pasif.")

# ---------------------------------------
# 🔹 7. pass kullanımı

kontrol = False

if kontrol:
    pass  # Kod yazılmamış olsa bile syntax hatası alınmaması için kullanılır.
else:
    print("Kontrol false olduğu için burası çalıştı.")  # Çıktı: Kontrol false olduğu için burası çalıştı.
# ---------------------------------------


# 🔹 8. pass kullanımı – boş fonksiyon

def oturum_kontrol_et():
    # Fonksiyon henüz yazılmadı, hata almamak için pass kullanılır
    pass

print("Kod sorunsuz çalıştı.")  # Çıktı: Kod sorunsuz çalıştı.