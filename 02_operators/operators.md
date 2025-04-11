# 🐍 Python - Operators (Operatörler)

Bu dosya, Python'da kullanılan operatörleri örneklerle açıklar.  
Kodlar `operators.py` içinde yer almaktadır.

---

## 📌 Kapsanan Başlıklar

1. Aritmetik Operatörler  
2. Karşılaştırma Operatörleri  
3. Mantıksal Operatörler  
4. Atama Operatörleri  
5. Kimlik Operatörleri (`is`, `is not`)  
6. Üyelik Operatörleri (`in`, `not in`)  

---

## 1. Aritmetik Operatörler

Matematiksel işlemler için kullanılır.

| Operatör | Anlamı       | Örnek     | Sonuç  |
|----------|--------------|-----------|--------|
| `+`      | Toplama      | 10 + 3    | 13     |
| `-`      | Çıkarma      | 10 - 3    | 7      |
| `*`      | Çarpma       | 10 * 3    | 30     |
| `/`      | Bölme        | 10 / 3    | 3.33   |
| `//`     | Tam bölme    | 10 // 3   | 3      |
| `%`      | Mod alma     | 10 % 3    | 1      |
| `**`     | Üs alma      | 10 ** 3   | 1000   |

---

## 2. Karşılaştırma Operatörleri

İki değer arasındaki ilişkiyi kontrol eder, **True/False** döner.

| Operatör | Anlamı            | Örnek        | Sonuç   |
|----------|-------------------|--------------|---------|
| `==`     | Eşit mi?          | 5 == 10      | False   |
| `!=`     | Eşit değil mi?    | 5 != 10      | True    |
| `>`      | Büyük mü?         | 5 > 10       | False   |
| `<`      | Küçük mü?         | 5 < 10       | True    |
| `>=`     | Büyük/eşit mi?    | 5 >= 5       | True    |
| `<=`     | Küçük/eşit mi?    | 10 <= 10     | True    |

---

## 3. Mantıksal Operatörler

Koşullarla birlikte kullanılır, **True/False** döner.

| Operatör | Anlamı         | Örnek               | Sonuç   |
|----------|----------------|---------------------|---------|
| `and`    | Ve              | True and False      | False   |
| `or`     | Veya            | True or False       | True    |
| `not`    | Değil (tersi)   | not True            | False   |

Gerçek hayattan örnek:
```python
yas = 20
uygun = yas >= 18 and yas <= 30  # True
