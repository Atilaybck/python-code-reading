# 🐍 Python - Sets (Kümeler)

Bu dosya, Python'da **sets (kümeler)** veri yapısının nasıl kullanıldığını açıklar.  
Kod örnekleri `sets.py` dosyasında yer almaktadır.

---

## 📌 Kapsanan Başlıklar

1. Set oluşturma  
2. Eleman ekleme (`add`, `update`)  
3. Eleman silme (`remove`, `discard`, `pop`, `clear`)  
4. Set özellikleri (benzersizlik ve sırasızlık)  
5. Küme işlemleri (`union`, `intersection`, `difference`, `symmetric_difference`)  
6. Eleman kontrolü (`in`)  
7. Set'i liste veya tuple'a dönüştürme

---

## 1. Set Oluşturma

```python
meyveler = {"elma", "armut", "muz"}
bos_set = set()  # {} yazarsan dict olur, dikkat!
