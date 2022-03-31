# Digunakan untuk mengetest command-command sebelum dimasukan kedalam file utama

import time

n = int(input("Panjang list:"))

local = time.localtime()
current = time.strftime("%S", local)
print(current)

hasil = int(current) % n
print(hasil)