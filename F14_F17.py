# Subprogram F14 hingga F17
# File ini berisikan fungsi-fungsi yang digunakan untuk menjalankan program mulai dari Fungsi ke 14 hingga Fungsi ke 17

# Algoritma Sub Program
import os
import time
from password import *
from csvlistfunction import *


# F14 - Help
# Subprogram Meminta Bantuan
# procedure help (string role)
'''
Deskripsi :
Prosedur tersebut memiliki sebuah input, 'role', yang bertipe string. 'Role' merupakan variabel yang menyatakan peran dari
pengguna tersebut (user, admin, atau guest). Prosedur ini memiliki tujuan untuk memperlihatkan segala perintah yang dapat
dilakukan oleh pengguna.

'''
# Algoritma 
def help(role):
    if (role == 'guest'):
        print("======================= HELP ======================= ")
        print("login                - Melakukan login ke dalam sistem.")                                            #F3
        print("help                 - Menampilkan perintah yang dapat dilakukan.")                                  #F14
        print("kerangajaib          - Menanyakan suatu pertanyaan pada kerang ajaib.")
        print("tictactoe            - Memulai permainan tictactoe.")

    elif (role == 'admin'):
        print("======================= HELP ======================= ")
        print("register             - Melakukan registrasi user baru.")                                             #F2
        print("login                - Melakukan login ke dalam sistem.")                                            #F3
        print("tambah_game          - Menambahkan game baru pada toko.")                                            #F4
        print("ubah_game            - Mengubah spesifikasi pada game tertentu.")                                    #F5
        print("ubah_stok            - Mengubah stock game yang ada pada toko.")                                     #F6
        print("list_game_toko       - Mengurutkan game yang ada pada toko berdasarkan parameter tertentu.")         #F7
        print("search_game_at_store - Mencari game berdasarkan parameter yang diinputkan.")                         #F11
        print("topup                - Menambahkan saldo pada suatu user tertentu.")                                 #F12
        print("help                 - Menampilkan perintah yang dapat dilakukan")                                   #F14
        print("print                - Menampilkan data csv pada terminal.")
        print("kerangajaib          - Menanyakan suatu pertanyaan pada kerang ajaib.")
        print("tictactoe            - Memulai permainan tictactoe.")
    else :                                                              # role == 'user'
        print("======================= HELP ======================= ")
        print("login                - Melakukan login ke dalam sistem.")                                            #F3
        print("list_game_toko       - Mengurutkan game yang ada pada toko berdasarkan data tertentu.")              #F7
        print("buy_game             - Membeli game tertentu dari toko.")                                            #F8
        print("list_game            - Mengurutkan seluruh game yang dimiliki berdasarkan parameter tertentu.")      #F9
        print("search_my_game       - Mencari game tertentu berdasarkan parameter tertentu.")                       #F10
        print("search_game_at_store - Mencari game berdasarkan parameter yang diinputkan.")                         #F11
        print("help                 - Menampilkan perintah yang dapat dilakukan")                                   #F14
        print("kerangajaib          - Menanyakan suatu pertanyaan pada kerang ajaib.")
        print("tictactoe            - Memulai permainan tictactoe.")

# F15 - Load
# Subprogram Mengambil Data Penyimpanan
# function load(string folder)
'''
Deskripsi :
Fungsi tersebut memiliki sebuah input, 'folder', yang bertipe string. 'folder' adalah variabel yang digunakan sebagai penunjuk jalan bagi program
untuk mengetahui tempat data yang disimpan. Fungsi akan mengembalikan kembali variabel 'folder' ke program utama bila folder tersebut
memang benar ada pada data penyimpanan. Di sisi lain, fungsi tidak mengembalikan apapun apabila tidak ditemukan folder sesuai dengan
yang diinputkan oleh pengguna.

Kamus :
    check : bool
'''
# Algoritma 
def load(folder):
    if(folder != "."):                                           # menghindari penggunaan input "."
        check = os.path.isdir("./csv files/"+folder)
        if (check == False):
            print('Folder "'+folder+'" tidak ditemukan.')
            return None
        else:
            print("Loading...")
            time.sleep(1)
            print('Selamat datang di antarmuka "Binomo"')
            return folder
    else:                                                           
        print('Folder "'+folder+'" tidak ditemukan.')
        return None

# F16 - Save
# Subprogram Penyimpanan Data
# procedure save (matrix d1, matrix d2, matrix d3, matrix d4)
'''
Deskripsi :
Prosedur tersebut memiliki 4 buah input yang bertipe matriks untuk ke 4 variabel tersebut. Untuk masing-masing variabel secara berturut-turut
diinputkan data pengguna, data game, data riwayat, dan data kepemilikan. Fungsi ini akan melakukan penyimpanan data-data tersebut
ke sebuah folder yang dikehendaki oleh pengguna.

Kamus :
    folder : string
    timedata : string
    local : time.struct_time
    check : bool
    procedure listtocsv(string file, string folder, matrix dataframe)
'''
# Algoritma 
def save(df1, df2, df3, df4):
    # Secara berturut-turut df1 = dfuser, df2 = dfgame, df3 = dfriwayat, df4 = dfkepemilikan.
    print("Ketikkan '#time' bila ingin membuat folder sesuai waktu pelaksanaan save.")
    folder = input("Masukkan nama folder penyimpanan: ")

    # Jika pengguna menginput nama folder dengan "#time", maka nama yang diinputkan adalah waktu sebenarnya
    local = time.localtime()                                # local adalah variabel untuk menyatakan localtime
    timedata = time.strftime("%Y-%m-%d_%H%M%S", local)
    if (folder == "#time"):
        folder = timedata

    # Melakukan check apakah terdapat nama folder sesuai dengan yang diinputkan
    check = os.path.isdir("./csv files/"+folder)
    if (check == True):                             # Dilakukan jika file tersebut benar ada
        listtocsv('user', folder, df1)
        listtocsv('game', folder, df2)
        listtocsv('riwayat', folder, df3)
        listtocsv('kepemilikan', folder, df4)
    else :                                          # Dilakukan jika tidak ada file dengan nama tersebut
        parent_dir = "./csv files"
        path = os.path.join(parent_dir, folder)         # Fungsi untuk menggabung
        os.mkdir(path)                                  # Command untuk membuat directory baru
        listtocsv('user', folder, df1)
        listtocsv('game', folder, df2)
        listtocsv('riwayat', folder, df3)
        listtocsv('kepemilikan', folder, df4)
    
    print("Data telah disimpan pada folder "+folder+"!")

# F17 - Exit
# Subprogram Penyelesaian Penggunaan Program
# fungsi exit()
'''
Deskripsi :
Fungsi exit digunakan bagi pengguna untuk keluar dari program. Saat ingin keluar program, pengguna akan ditanyakan apakah benar
ingin menyudahi penggunaan program. Fungsi akan mengembalikan output jawaban dari pengguna.

Kamus :
    answer : string
'''
# Algoritma 
def exit():
    answer = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ").lower()
    while (answer != "y" and answer != "n"):
        answer = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ").lower()
    return answer
    # return dalam char 'y' atau 'n'

# ======================= Fungsi lain-lain =======================

# Subprogram Penampilan Data
# proscedure printdataframe(matrix dfuser, matrix dfgame, matrix dfriwayat, matrix dfkepemilikan)
'''
Deskripsi :
Prosedur tersebut memiliki 4 jenis output yang berjenis matrix. Untuk masing-masing variabel, data tersebut secara berturut-turut adalah
data user, data game, data riwayat, dan data kepemilikan. Prosedur akan menanyakan pengguna mengenai data apa yang ingin ditampilkan.
Prosedur akan menampilkan data sesuai dengan data yang dikehendaki oleh pengguna.

Kamus :
    choice : string
'''
# Algoritma 
def printdataframe(dfuser, dfgame, dfriwayat, dfkepemilikan):       # Untuk melihat dataframe, hanya bisa diakses oleh admin
    print("Ketik data yang ingin dilihat (1-4).")
    choice = input("1. User, 2. Game, 3.Riwayat, 4. Kepemilikan : ")
    
    if (choice == '1' or choice == 'user'):
        printlist(dfuser)
    elif (choice == '2' or choice == 'game'):
        printlist(dfgame)
    elif (choice == '3' or choice == 'riwayat'):
        printlist(dfriwayat)
    elif (choice == '4' or choice == 'kepemilikan'):
        printlist(dfkepemilikan)
    else :
        printlist("Pilihan data invalid.")