# 🐍 Python - Conditionals (Koşullu İfadeler)

Bu dosya, Python'da koşullu ifadelerin nasıl kullanıldığını açıklar.  
Kodlar `conditionals.py` içinde örneklerle gösterilmiştir.

---

## 📌 Kapsanan Başlıklar

1. if koşulu  
2. if-else yapısı  
3. elif (else if) yapısı  
4. İç içe koşullar (nested if)  
5. Tek satırlık koşul (ternary if)  
6. Boolean ifadelerle koşul  
7. pass kullanımı (koşul içinde)  
8. pass kullanımı (fonksiyon içinde)

---

## 1. if Koşulu

Sadece belirli bir koşul sağlandığında çalışacak kod bloğudur:

```python
sayi = 10
if sayi > 5:
    print("Sayı 5'ten büyüktür.")  # Çıktı: Sayı 5'ten büyüktür.
