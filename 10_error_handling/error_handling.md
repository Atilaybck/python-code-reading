# 🐍 Python - Error Handling (Hata Yönetimi)

Bu dosya, Python'da **hataları yakalama ve yönetme** konusunu açıklar.  
Kod örnekleri `error_handling.py` dosyasında yer almaktadır.

---

## 📌 Kapsanan Başlıklar

1. Temel `try` / `except`  
2. Belirli hata türleri  
3. `else` ve `finally` blokları  
4. `raise` ile manuel hata fırlatma  
5. Gerçek hayat örnekleri (dosya açma)  
6. Çoklu hata türleri yakalama

---

## 🔹 1. Temel try / except Yapısı

```python
try:
    sayi = int(input("Bir sayı girin: "))
    print("Girilen sayı:", sayi)
except:
    print("Hata oluştu! Lütfen geçerli bir sayı girin.")
