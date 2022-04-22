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
        print("sort                 - Mengurutkan data sementara pada kolom spesifik dengan urutan mengurut membesar.")
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
        print("riwayat              - Menampilkan seluruh riwayat pembelian akun tertentu.")                        #F13
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
    print("========================================================================================")
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
def exitprogram():
    print("========================================================================================")
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
    print("========================================================================================")
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
        print("Pilihan data invalid.")

# Subprogram Mengurutkan Data pada Dataframe
# function sortdataframe(dfuser, dfgame, dfriwayat, dfkepemilikan):
'''
Deskripsi :
Prosedur tersebut memiliki 4 jenis parameter yaitu dfuser, dfgame, dfriwayat dan dfkepemilikan. 4 parameter tersebut bertipe matrix.
Prosedur akan mengurutkan suatu jenis dataframe pada kolom yang diinginkan pengguna. Urutan yang dilakukan akan menjadi urutan membesar.

Kamus :
    choice : string
    column : int
    function sortmatrix (matrix, int column) -> matrix
'''
def sortdataframe(dfuser, dfgame, dfriwayat, dfkepemilikan):
    print("========================================================================================")
    print("Ketik data yang ingin diurutkan (1-4). ")
    choice = input("1. User, 2. Game, 3.Riwayat, 4. Kepemilikan : ")
    if (choice == '1' or choice == 'user'):
        print("Ketikan kolom yang ingin diurutkan (1-6).")
        try:
            column = int(input("1. User ID, 2. Username, 3. Nama Pengguna, 4. Password, 5. Role, 6. Saldo : "))
            if (column < 1 or column > 6):
                print("Pilihan data invalid.")
            elif ( column == 6):                                # Saldo adalah satu satunya kolom int
                dfuser = sortmatrixint(dfuser, column-1)
                print("Data dfuser sudah diurutkan!")
            else :                                               # Pilihan 1 -5 adalah data string
                dfuser = sortmatrix(dfuser, column-1)
                print("Data dfuser sudah diurutkan!")
        except :
            print("Invalid Input")
        
        
    elif (choice == '2' or choice == 'game'):
        print("Ketikan kolom yang ingin diurutkan (1-6).")
        try:
            column = int(input("1. Game ID, 2. Nama Game, 3. Kategori, 4. Tahun Rilis, 5. Harga, 6. Stok : "))
            if (column < 1 or column > 6):
                print("Pilihan data invalid.")
            elif(column >=4):                                   # Kolom 4,5,6 adalah data int
                dfgame = sortmatrixint(dfgame, column-1)
                print("Data dfgame sudah diurutkan!")
            else:                                               # Kolom 1,2,3 berisi data string
                dfgame = sortmatrix(dfgame, column-1)
                print("Data dfgame sudah diurutkan!")
        except :
            print("Invalid Input")
        

    elif (choice == '3' or choice == 'riwayat'):
        print("Ketikan kolom yang ingin diurutkan (1-5).")
        try:
            column = int(input("1. Game ID, 2. Nama Game , 3. Harga, 4. User ID, 5. tahun Beli : "))
            if (column < 1 or column > 5):
                print("Pilihan data invalid.")
            elif (column >=3):                                      # Kolom 3,4,5 berisi data int
                dfriwayat = sortmatrixint(dfriwayat, column-1)
                print("Data dfriwayat sudah diurutkan!")
            else:                                                       # Kolom 1, 2 berisi data string
                dfriwayat = sortmatrix(dfriwayat, column-1)
                print("Data dfriwayat sudah diurutkan!")
        except :
            print("Invalid Input")

    elif (choice == '4' or choice == 'kepemilikan'):
        print("Ketikan kolom yang ingin diurutkan (1-2).")
        try:
            column = int(input("1. Game ID, 2. User ID : "))
            if (column < 1 or column > 2):
                print("Pilihan data invalid.")
            elif (column == 2):                                                 # Kolom 2 berisi data int
                dfkepemilikan = sortmatrixint(dfkepemilikan, column-1)
                print("Data dfkepemilikan sudah diurutkan!")
            else:
                dfkepemilikan = sortmatrix(dfkepemilikan, column-1)
                print("Data dfkepemilikan sudah diurutkan!")
        except :
            print("Invalid Input")

    else :
        print("Pilihan data invalid.")
    return dfuser, dfgame, dfriwayat, dfkepemilikan