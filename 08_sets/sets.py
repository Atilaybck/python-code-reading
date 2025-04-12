# ---------------------------------------
# 🐍 Python - Sets (Kümeler)

# Sets, Python'da sırasız (unordered), benzersiz (unique) elemanlar içeren veri yapısıdır.
# Listelere benzer gibi görünür ama:
# 🔸 Elemanlar sıralı değildir (index yoktur)
# 🔸 Aynı eleman birden fazla kez olamaz (otomatik filtrelenir)
# 🔸 İçerik değiştirilebilir (mutable) ama içine sadece değiştirilebilen (hashable) veri tipleri eklenebilir

# Kullanım Alanı:
# - Tekrar eden verileri filtrelemek
# - Küme işlemleri (birleşim, kesişim, fark, simetrik fark) yapmak
# - 'in' ile hızlı üyelik kontrolü

# Tanımlama:
# my_set = {1, 2, 3}
# boş set için: my_set = set()

# ---------------------------------------
# 🔹 1. Set Oluşturma

meyveler = {"elma", "armut", "muz"}
bos_set = set()  # DİKKAT: {} yazarsan boş dictionary olur!

print(meyveler)  # Çıktı sırasız olabilir: {'muz', 'elma', 'armut'}
# ---------------------------------------



# 🔹 2. Eleman Ekleme

meyveler.add("çilek")       # Tek eleman ekler
meyveler.update(["kiraz", "kivi"])  # Birden fazla ekler

print(meyveler)
# Çıktı: {'çilek', 'armut', 'elma', 'muz', 'kiraz', 'kivi'}

# ---------------------------------------



# 🔹 3. Eleman Silme

meyveler = {"elma", "armut", "muz"}

meyveler.remove("elma")     # Eleman varsa siler, yoksa HATA (KeyError) verir
meyveler.discard("muz")     # Eleman varsa siler, yoksa HATA VERMEZ
meyveler.discard("ananas")  # "ananas" yok ama discard() bu durumu sessizce geçer

# pop(): Rasgele 1 eleman siler ve döner — ama set boşsa HATA verir!
if meyveler:
    eleman = meyveler.pop()
    print("Silinen:", eleman)
else:
    print("Set boş, pop yapılamaz!")

print(meyveler)  # Kalan elemanları gösterir

meyveler.clear()  # Tüm elemanları siler
print(meyveler)   # Çıktı: set()
# ---------------------------------------



# 🔹 4. Benzersizlik ve Sırasızlık

tekrarli = {"elma", "muz", "elma", "elma"}
print(tekrarli)  # Çıktı: {'muz', 'elma'} – tekrarlar otomatik silinir
# ---------------------------------------



# ---------------------------------------
# 🔹 5. Küme İşlemleri

A = {1, 2, 3}
B = {3, 4, 5}

print("Birleşim (union):", A.union(B))
# Çıktı: Birleşim (union): {1, 2, 3, 4, 5}

print("Kesişim (intersection):", A & B)
# Çıktı: Kesişim (intersection): {3}

print("Fark (difference):", A - B)
# Çıktı: Fark (difference): {1, 2}  → A'da olup B'de olmayanlar

print("Sembolik fark (symmetric_difference):", A ^ B)
# Çıktı: Sembolik fark (symmetric_difference): {1, 2, 4, 5}
# → Her iki kümede olup ortak olmayanlar
# ---------------------------------------



# 🔹 6. in ile Eleman Kontrolü

print(2 in A)       # True
print(6 in B)       # False
# ---------------------------------------



# 🔹 7. Set'i Listeye veya Tuple’a Çevirme

sayilar = {1, 2, 3}
liste = list(sayilar)
tuple_ = tuple(sayilar)

print(liste)   # [1, 2, 3] – sırası garanti değil
print(tuple_)  # (1, 2, 3)
