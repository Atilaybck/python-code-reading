---

## 🔹 6. *args – Çoklu Konumsal Argümanlar

`*args`, bir fonksiyona **istenildiği kadar konumsal argüman** (sıralı değer) gönderilmesini sağlar.  
Fonksiyon içinde bu argümanlar bir **tuple (demet)** olarak tutulur.

### 🧪 Örnek:

```python
def sayilar_toplami(*args):
    print("Gelen sayılar:", args)
    print("Toplam:", sum(args))

sayilar_toplami(1, 2, 3)
# Çıktı:
# Gelen sayılar: (1, 2, 3)
# Toplam: 6
