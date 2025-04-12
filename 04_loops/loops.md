# 🐍 Python - Loops (Döngüler)

Bu dosya, Python'da döngülerin nasıl kullanıldığını açıklar.  
Kodlar `loops.py` içinde örneklerle gösterilmiştir.

---

## 📌 Kapsanan Başlıklar

1. for döngüsü  
2. while döngüsü  
3. range() fonksiyonu  
4. break ile döngüden çıkış  
5. continue ile döngü atlama  
6. else bloğu (for/while ile)  
7. İç içe döngü (nested loop)  
8. pass ifadesi  

---

## 1. for Döngüsü – Liste Üzerinde Gezinme

```python
meyveler = ["elma", "armut", "muz"]
for meyve in meyveler:
    print("Meyve:", meyve)
