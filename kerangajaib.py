# File ini berisikan fungsi-fungsi yang digunakan untuk menjalankan program kerang ajaib

'''
Persamaan dasar LCG --> x[n+1] = (x[n]*a +b) mod m
Loop akan diulang minimal 7 kali sehingga didapatkan angka yang random
        a dan b = merupakan integer bebas yang bersifat konstan
        x[n] = nilai awal, pada program ini akan digunakan detik saat program dijalankan
        m   = pembagi, sebisa mungkin bersifat prima

'''

# Subprogram Pertanyaan kepada Kerang Ajaib
# procedure kerangajaib()
'''
Deskripsi :
Prosedur kerangajaib berfungsi untuk mendapatkan jawaban dari kerangajaib. Pengguna akan diminta untuk menginputkan suatu pertanyaan,
lalu kerang ajaib akan menjawab secara acak (random).

Kamus :
    answerlist : array of string
    length : int
    local : time.struct_time
    current : string
    a, b, m, count : int
    loop : bool
    
'''
# Algoritma 
import time
from csvlistfunction import *

# Fungsi Kerang Ajaib
def kerangajaib():
    answerlist = ['Bisa jadi(?)', 'Kubilang tidak ya tidak', 'Menurut kamu sendiri?', "Hidup maneh kumaha maneh", "Yo ndak tau, kok tanya saya?", "Ah sudahlah",
            "Pertanyaan tersebut diluar kapasitas kemampuan.", "Kerang ajaib menolak untuk menjawab.", 'Kerang ajaib has left the chat.']
    
    # Menghitung panjang list answerlist
    length = lengthlist(answerlist)

    input("Apa pertanyaanmu? ")

    # Mendapatkan program dilaksanakan pada detik ke berapa
    local = time.localtime()
    print(type(local))
    current = time.strftime("%S", local)

    # Random Number menggunkaan metode LCG
    # Loop akan diulang sebanyak minimal 7 kali, x[0] yang digunakan adalah variabel 'current'
    # Jika dalam 7 kali, nilai yang dihasilkan lebih dari (length-1), maka loop akan dilakukan kembali
    a = 6
    b = 17
    m = 11
    count = 0
    loop = True
    current = int(current)                  # mengubah current dari string menjadi integer
    while (count < 7 or loop == True):
        if (count >= 7 and (0 <= result <= (length-1))):
            loop = False
        else:
            result = ((current*a)+b)%m
            current = result                    # hasil perhitungan akan dimasukan kembali sebagai input
            count +=1
    
    # Program randomize memanfaatkan detik yang terus bertambah dan metode LCG, sehingga nilai yang didapatkan terus berubah
    print(answerlist[result])
