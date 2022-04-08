# File ini berisikan fungsi-fungsi yang digunakan untuk menjalankan program kerang ajaib

import time

# Fungsi Kerang Ajaib
def kerangajaib():
    answerlist = ['Bisa jadi(?)', 'Kubilang tidak ya tidak', 'Menurut ngana?', "Hidup maneh kumaha maneh", "YNTKTS", 
            "Pertanyaan tersebut diluar kapasitas kemampuan.", "Kerang ajaib menolak untuk menjawab.", 'Kerang ajaib has left the chat.']
    
    # Menghitung panjang list answerlist
    length = 0
    counting = True
    while (counting == True):
        if (answerlist[length] == 'Kerang ajaib has left the chat.'): #List selalu diset bahwa string "Kerang ajaib has left the chat." berada pada posisi terakhir
            counting = False
        if (counting == True):                  # Penambahan length tidak perlu dilakukan bila perhitungan sudah dinonaktifkan
            length = length +1 

    input("Apa pertanyaanmu? ")

    # Mendapatkan program dilaksanakan pada detik ke berapa
    local = time.localtime()
    current = time.strftime("%S", local)
    # Program randomize memanfaatkan detik yang terus bertambah, sehingga nilai yang didapatkan terus berubah
    result = int(current) % length  
    print(answerlist[result])