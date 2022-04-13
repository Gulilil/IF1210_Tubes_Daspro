'''
===== Penjelasan Pengubahan Password =====
Pengubahan password hanya dilakukan untuk bagian huruf saja. Untuk angka dan symbol dibiarkan tetap seperti semula.
Fungsi untuk menyimpan password adalah :

y = (4(x+29)) mod 26 + 97, atau bisa juga ditulis

y - 97 = (4x + 116 ) mod 26  --> 4x + 116 = 26*(hasil bagi) + y -97

4*(code asli) + 116 = 26* (hasilbagi) + (code chippered) - 97

dengan x = code ASCII dari huruf asli,
       y = code ASCII dari huruf chippered,
       4  = pengali (multiplier) = merupakan key1,
       29 = penambah (increment) = merupakan key2,
       mod 26 dilakukan agar hasil yang didapat berkisar pada 0 - 25 (melambangkan urutan alphabet dari A - Z dengan A = 0),
       penambahan 97 dilakukan untuk menyesuaikan dengan kode ASCII untuk alphabet non-kapital (range 97 - 122)

Hasil bagi (4(x+29)) div 26 akan disimpan sebagai suatu variabel kunci. Variabel kunci ini akan digunakan untuk 
menentukan angka semula sehingga dapat mengembalikan chippered password menjadi initial password.
'''


# Subprogram Pengubahan Password Semula menjadi Kode Password
# function enctryptpass (string password)
'''
Deksripsi : 
Fungsi ini memiliki 1 input yaitu variable password yang bertipe string. Password merupakan password awal yang diinputkan oleh
pengguna. Fungsi ini digunakan untuk mengubah password tersebut menjadi sebuah kode password untuk disimpan dalam file penyimpanan.

Kamus Lokal
    alphabet : string = "abcdefghijklmnopqrstuvwxyz"
    newpass, password : string
    key1, key2 : int
    chipcode, varkey : int
    newalphabet : char
'''
# Algoritma
         #daftar alphabet

def encryptpass(password):
    newpass = ""                                        # Variabel ini akan digunakan untuk menyimpan password simpanan
    alphabet = "abcdefghijklmnopqrstuvwxyz"    
    for i in password:
        if (i in alphabet or i in alphabet.upper()):    # Pengubahan pass dilakukan hanya pada komponen huruf saja
            key1 = 4
            key2 = 29
            chipcode = (key1*(ord(i)+key2))% 26 +97
            varkey = key1*(ord(i)+key2) // 26                # Varkey adalah variabel kunci yang digunakan nanti saat pengembalian pass (baca penjelasan)
            newalphabet = chr(chipcode)

            newpass = newpass + str(varkey) + newalphabet
        else:                                           # Bila komponen i bukanlah huruf
            newpass = newpass + i

    return newpass
'''
Contoh hasil: 
    Untuk password masukan = "password", newpass yang dikeluarkan adalah = "21s19k22e22e22u21o22a19w"
    Untuk password masukan = "@Orang_ganteng", newpass yang dikeluarkan adalah = "@16q22a19k21k20i_20i19k21k22i20a21k20i"
    Untuk password masukan = "Huhu123Haha", newpass yang dikeluarkan adalah = "15o22m20m22m12315o19k20m19k"
'''



# Subprogram Pengubahan Kode Password menjadi Password Semula
# function decryptpass (string password) 
'''
Deksripsi:
Fungsi ini memiliki suatu input variabel password yang bertipe string. Fungsi ini digunakan untuk mengembalikan
kode password pada file penyimpanan menjadi bentuk password semula yang diinputkan oleh user.

Kamus Lokal
    alphabet : string = "abcdefghijklmnopqrstuvwxyz"
    length : int
    initpass : string
    varkey : int
    require1, require2 : bool
    chipcode : int
    key1, key2 : int
    initcode : int
    initalphabet : char
'''
# Algoritma
def decryptpass(password):
    alphabet = "abcdefghijklmnopqrstuvwxyz"    

    # Pertama-tama perlu ditentukan terlebih dahulu panjang dari string password
    length = 0
    for i in password:
        length +=1

    initpass = ""                       # initpass adalah variabel initial password yang digunakan untuk menyimpan password asli

    i = 0                               # i hanya dilakukan sebagai variabel pembantu perhitungan
    while (i < length):
        # Melakukan pengecekan pertama (requirement1)
        try :
            varkey = int(password[i]+ password[i+1])         # Melakukan pengecekan apakah index ke i dan setelah i bertipe integer
            require1 = True                                 # mengingat bahwa 1 huruf diubah menjadi 2 integer dan 1 huruf ("p" --> "21s")
        except:
            varkey = 0                                       # Bila index ke i dan index setelah i bukan integer
            require1 = False                                 # maka pengecekan pertama salah, suku tersebut tidak perlu dikonversi
        
        # Melakukan pengecekan kedua (requirement2)
        if (require1 == True):
            if( i+2 < length and (password[i+2] in alphabet)):      # Memastikan bahwa suku setelah varkey merupakan huruf
                chipcode = password[i+2]                            # Perlu dilakukan pengecekan juga bahwa index i+2 harus kurang dari length (mencegah error)
                require2 = True
            else :
                require2 = False                                    # Bila suku setelah varkey bukanlah huruf, maka kedua requirement otomatis salah
                require1 = False                                    # Bagaimanapun juga, bila suku i+2 bukan huruf, maka kelompok 3 suku (2 int dan 1 huruf) tersebut bukanlah hasil encryptpass

        # Melakukan pengembalian ke password semula
        if (require1 == True and require2 == True):
            key1 = 4
            key2 = 29
            initcode = (26*varkey + ord(chipcode) - 97 - (key1*key2))/key1         # Menggunakan fungsi yang terdapat pada penjelasan
            initalphabet = chr(int(initcode))
            initpass = initpass + initalphabet                          # Penggabungan hasil konversi password ke variabel initpass
            i = i + 3                                                   # Dilakukan +3 untuk melompati 2 suku yang telah dicek
            '''
            Misalkan suatu kode "21s19k" dan i = 0, bagian "21s" akan dicek dan dikonversi.
            Setelah suku "2" pada "21s" dicek, suku "1" dan "s" tidak perlu dilakukan pengecekan.
            Maka dari itu, pengecekan selanjutnya akan dilakukan pada kelompok "19k". Maka dari itu dilakukan i = i+3.
            '''
        if (require1 == False):                                         # Bila require1 = False, maka require2 pasti False
            initpass = initpass + password[i]                                     # Maka dapat disimpulkan bahwa kelompok tersebut tidak perlu dikonversi
            i = i + 1                                                   # Suku selanjutnya akan tetap dilakukan pengecekan
    
    return initpass

'''
Contoh Hasil :
    Untuk masukan password = "@16q22a19k21k20i_20i19k21k22i20a21k20i", hasil initpass yang dikeluarkan adalah = "@Orang_ganteng"
'''
            


