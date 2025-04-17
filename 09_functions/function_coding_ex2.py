# 🔹 Soru 26:
# Bir sayının karesini ve küpünü birlikte döndüren fonksiyon yaz.



def kare_ve_kup(sayi):
    return sayi ** 2, sayi ** 3

print(kare_ve_kup(3))  # Çıktı: (9, 27)
# ----------------------------------------------------------------


# 🔹 Soru 27:
# Bir kelimenin tersini döndüren fonksiyon yaz.



def ters_cevir(kelime):
    return kelime[::-1]

print(ters_cevir("python"))  # Çıktı: nohtyp
# ----------------------------------------------------------------


# 🔹 Soru 27:
# Bir sayı listesindeki tüm sayıların karesini alıp yeni bir liste döndüren fonksiyon yaz.



def kareler(liste):
    # Boş bir liste oluştur
    sonuc = []

    # Listedeki her sayıyı sırayla al
    for x in liste:
        # Sayının karesini al ve listeye ekle
        kare = x ** 2
        sonuc.append(kare)

    # Sonuç listesini döndür
    return sonuc

print(kareler([1, 2, 3, 4]))  # Çıktı: [1, 4, 9, 16]






