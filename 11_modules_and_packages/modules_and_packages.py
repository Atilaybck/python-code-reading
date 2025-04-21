# ---------------------------------------
# 🔹 1. Modül Nedir?

# Modül, içinde Python kodları (fonksiyonlar, değişkenler, vs.) bulunan .py uzantılı dosyadır.
# Bir modülü başka bir dosyada kullanmak için "import" ederiz.

# Örnek: selam.py
def merhaba():
    print("Selam! Bu bir modülden geldi.")

# ---------------------------------------
# 🔹 2. Modül Nasıl Kullanılır?

# Farklı bir dosyada (örneğin main.py) şöyle kullanılır:

import selam  # selam.py dosyasını içe aktarır

selam.merhaba()  # Çıktı: Selam! Bu bir modülden geldi.

# ---------------------------------------
# 🔹 3. Hazır (Built-in) Modül Kullanımı

# Python kendi içinde bazı modüllerle gelir. Örneğin math modülü:

import math

print(math.sqrt(16))   # Çıktı: 4.0 (karekök)
print(math.pi)         # Çıktı: 3.14159...

# ---------------------------------------
# 🔹 4. Belirli Bir Fonksiyonu Alma

from math import sqrt  # math modülünden sadece sqrt (karekök alma) fonksiyonunu alır

print(sqrt(49))  # Çıktı: 7.0

# Böylece sadece ihtiyacın olan fonksiyonu alırsın, "math." yazmana gerek kalmaz.

# ---------------------------------------
# 🔹 5. Alias (Kısa İsim Verme)

import math as m # math modülünü "m" ismiyle kısaltarak içe aktarır

print(m.pow(2, 3))  # Çıktı: 8.0 (2 üzeri 3)

# Bu şekilde modüle kısa isim vererek kullanımı kolaylaştırırsın.

# Örnek 1: math modülü
import math as m
print(m.sqrt(16))     # Çıktı: 4.0
print(m.pi)           # Çıktı: 3.14159...

# Örnek 2: pandas modülü (veri analizi için)
import pandas as pd
data = pd.DataFrame({"Ad": ["Ali", "Ayşe"], "Yaş": [30, 25]})
print(data)

# Örnek 3: numpy modülü (matematiksel işlemler için)
import numpy as np
arr = np.array([1, 2, 3])
print(np.mean(arr))   # Çıktı: 2.0

# Örnek 4: matplotlib.pyplot (grafik çizimi)
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()

# ---------------------------------------
# 🔹 6. Paket Nedir?

# Paket = Klasör + __init__.py + modüller
# Paket, içinde birden çok modül barındıran klasördür.

# Örnek dosya yapısı:
# proje/
# ├── paketim/
# │   ├── __init__.py
# │   └── mesaj.py
# └── main.py

# mesaj.py:
def goster():
    print("Paket içinden merhaba!")

# main.py:
from paketim import mesaj

mesaj.goster()  # Çıktı: Paket içinden merhaba!

# ---------------------------------------
# ✅ Özet:
# - Modül: .py dosyasıdır.
# - Paket: Modül içeren klasördür.
# - import: Modül veya paket içeriğini kullanmak için kullanılır.
# - from ... import ... → sadece ihtiyacın olanı alır.
# - as → modüle kısa isim verir.
