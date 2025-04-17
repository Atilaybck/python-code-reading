# tuples_coding_ex1.py

# 🔸 Soru 1: 3 farklı meyveden oluşan bir tuple oluştur ve ekrana yazdır.

meyveler = ("elma", "armut", "muz")
print(meyveler)
# Yorum: Tuple, () ile tanımlandı.
# Çıktı: ('elma', 'armut', 'muz')
# ---------------------------------------

# 🔸 Soru 2: Bir tuple'daki ilk ve son elemana eriş.

renkler = ("kırmızı", "yeşil", "mavi")
print(renkler[0])    # İlk eleman
print(renkler[-1])   # Son eleman
# Yorum: Pozitif ve negatif indexlerle erişim sağlandı.
# Çıktı: kırmızı, mavi
# ---------------------------------------

# 🔸 Soru 3: Tuple'ın ilk iki elemanını dilimleyerek yazdır.

sayilar = (10, 20, 30, 40)
print(sayilar[:2])
# Yorum: Slicing ile 0 ve 1. index'teki elemanlar alındı.
# Çıktı: (10, 20)
# ---------------------------------------

# 🔸 Soru 4: Tuple'daki bir elemanı değiştirmeye çalış, sonucu gözlemle.

renkler = ("kırmızı", "yeşil", "mavi")
# renkler[0] = "turuncu"  # HATA: Tuple değiştirilemez
# Yorum: Tuple sabittir, elemanları değiştirilemez.
# Çıktı: TypeError (yorum satırına alınmıştır)
# ---------------------------------------

# 🔸 Soru 5: Bir tuple'da "kırmızı" kaç kere geçiyor ve "mavi" hangi index'te?

renkler2 = ("kırmızı", "yeşil", "kırmızı", "mavi")
print(renkler2.count("kırmızı"))
print(renkler2.index("mavi"))
# Yorum: count() ve index() metodları kullanıldı.
# Çıktı: 2, 3
# ---------------------------------------

# 🔸 Soru 6: Tek elemanlı bir tuple oluştur ve türünü yazdır.

tek = ("elma",)
print(type(tek))
# Yorum: Virgül varsa tuple'dır, yoksa string olur.
# Çıktı: <class 'tuple'>
# ---------------------------------------

# 🔸 Soru 7: Tuple içindeki tüm renkleri for döngüsü ile yazdır.

renkler = ("kırmızı", "yeşil", "mavi")

for renk in renkler:
    print("Renk:", renk)
# Yorum: for döngüsü ile tuple elemanları üzerinde gezildi.
# Çıktı: kırmızı, yeşil, mavi
# ---------------------------------------

# 🔸 Soru 8: İç içe tuple yapısından şehir ismini al.

bilgi = ("Ali", 28, ("Ankara", "Türkiye"))
print(bilgi[2][0])
# Yorum: Nested tuple'dan istenilen alt eleman çekildi.
# Çıktı: Ankara
# ---------------------------------------

# 🔸 Soru 9: Tuple ve liste farkını göster.

liste = [1, 2, 3]
tuple_ = (1, 2, 3)

liste[0] = 10
print("Liste:", liste)
# tuple_[0] = 10  # HATA: Tuple değiştirilemez
# Yorum: Listeler değiştirilebilirken, tuple'lar değiştirilemez.
# Çıktı: Liste: [10, 2, 3]
# ---------------------------------------
