# Identitas


# Kamus



# Algoritma
import pandas as pd
from kerangajaib import kerangajaib
from tictactoe import tictactoe
from password import *

# Inisasi Data
dfuser = pd.read_csv("./user.csv", sep = ';')
dfgame = pd.read_csv("./game.csv", sep = ';')
dfriwayat = pd.read_csv("./riwayat.csv", sep = ';')
dfkepemilikan = pd.read_csv("./kepemilikan.csv", sep =';')

# F2 - Register
alphabet = "abcdefghijklmnopqrstuvwxyz"
numbersymbol = "0123456789-_"

def register(dfuser):
    nama = input("Masukan nama: ")
    username = input("Masukan username: ")
    password = input("Masukan password: ")
    # Melakukan cek apakah terdapat username yang sama
    sameuser = False
    for i in dfuser["username"]:
        if (i == username):
            sameuser = True
    while (sameuser == True):
        sameuser = False
        print("Username", username," sudah terpakai, silakan menggunakan username lain.")
        username = input("Masukan username: ")
        for i in dfuser["username"]:
            if (i == username):
                sameuser = True
            
    
    uservalid = True
    # Melakukan cek validitas username
    for i in username:
        if (i not in (alphabet) and i not in (alphabet.upper()) and i not in (numbersymbol)):
            uservalid = False
    while (uservalid == False):
        print("Username", username, "tidak valid. Username hanya diperkenankan mengandung alphabet, angka, underscore, dan strip")
        username = input("Masukan username: ")
        uservalid = True
        for i in username:
            if (i not in (alphabet) and i not in (alphabet.upper()) and i not in (numbersymbol)):
                uservalid = False

    # Mengubah password yang diinputkan menjadi chippered password 
    password = encryptpass(password, alphabet)

    # Memasukan data ke dalam dataframe
    total = dfuser.shape[0]
    totalindex = total - 1
    last_id = dfuser["id"].iloc[totalindex]
    userdata = {    "id"            : [last_id + 1],
                "username"      : [username],
                "nama"          : [nama],
                "password"      : [password],
                "role"          : ["user"],
                "saldo"         : [0] }
    df = pd.DataFrame(data=userdata)
    dfjoin = pd.concat([dfuser,df], ignore_index = True)
    print("Username", username,' telah berhasil register ke dalam "Binomo".')
    return dfjoin

# F3 - Login
def login(dfuser):
    username = input("Masukan username: ")
    password = input("Masukan password: ")

    # Melakukan verifikasi terhadap username dan password
    index = 0
    lastindex = dfuser.shape[0] - 1
    available = False       # Variabel untuk menjelaskan apakah username ada pada dataframe
    search = True           # Variabel untuk melakukan pencarian terhadap data user
    while (search == True):
        if (dfuser["username"].iloc[index] == username):
            available = True            # Data username terdapat pada dataframe
            search = False              # Pencarian tidak perlu dilakukan lagi
        if (index == lastindex and dfuser["username"].iloc[index] != username ):    # Sampai suku terakhir, tidak ditemukan data pengguna
            available = False
            search = False
        if (search == True):            # Jika search = False, tidak perlu lagi dilakukan penambahan index
            index = index + 1
    if (available == True):
        # Mengeluarkan pernyataan login 
        # Bila benar, mengembalikan data pengguna berada pada index ke berapa
        # Bila salah, tidak mengembalikan apapun

        # Mengembalikan chippered password ke initial password
        initialpass = decryptpass(dfuser['password'].iloc[index], alphabet)
        # Melakukan cek apakah password yang dimasukan sama dengan initial password
        if (initialpass == password):
            print("Halo "+ dfuser["nama"].iloc[index]+'! Selamat datang di "Binomo".')
            return index
        else:
            print("Password atau username salah atau tidak ditemukan.")
            return None
    else:
        print("Password atau username salah atau tidak ditemukan.")
        return None

# F4 - Menambah Game ke Toko
# F5 - Mengubah Game pada Toko
# F6 - Mengubah Stok Game di Toko
# F7 - Listing Game di Toko 
# F8 - Membeli Game
# F9 - Melihat Game yang dimiliki
# F10 - Mencari Game yang dimiliki
# F11 - Mencari Game di Toko 
# F12 - Top Up Saldo
# F13 - Melihat Riwayat Pembayaran
# F14 - Help
def help(role):
    if (role == 'admin'):
        print("================ HELP ================ ")
        print("register             - Melakukan registrasi user baru.")                                             #F2
        print("login                - Melakukan login ke dalam sistem.")                                            #F3
        print("tambah_game          - Menambahkan game baru pada toko.")                                            #F4
        print("ubah_game            - Mengubah spesifikasi pada game tertentu.")                                    #F5
        print("ubah_stok            - Mengubah stock game yang ada pada toko.")                                     #F6
        print("list_game_toko       - Mengurutkan game yang ada pada toko berdasarkan parameter tertentu.")         #F7
        print("search_game_at_store - Mencari game berdasarkan parameter yang diinputkan.")                         #F11
        print("topup                - Menambahkan saldo pada suatu user tertentu.")                                 #F12
        print("print                - Menampilkan data csv pada terminal.")
        print("kerangajaib          - Menanyakan suatu pertanyaan pada kerang ajaib.")
        print("tictactoe            - Memulai permainan tictactoe.")
    else :                                                              # role == 'user'
        print("================ HELP ================ ")
        print("login                - Melakukan login ke dalam sistem.")                                            #F3
        print("list_game_toko       - Mengurutkan game yang ada pada toko berdasarkan data tertentu.")              #F7
        print("buy_game             - Membeli game tertentu dari toko.")                                            #F8
        print("list_game            - Mengurutkan seluruh game yang dimiliki berdasarkan parameter tertentu.")      #F9
        print("search_my_game       - Mencari game tertentu berdasarkan parameter tertentu.")                       #F10
        print("search_game_at_store - Mencari game berdasarkan parameter yang diinputkan.")                         #F11
        print("kerangajaib          - Menanyakan suatu pertanyaan pada kerang ajaib.")
        print("tictactoe            - Memulai permainan tictactoe.")

# F15 - Load
    # Perlu make argparse
# F16 - Save
def save(df1,df2,df3,df4):
    # Belum ditambahin os.walk
    # Secara berturut-turut df1 = dfuser, df2 = dfgame, df3 = dfriwayat, df4 = dfkepemilikan.
    df1.to_csv("./user.csv", sep = ';')
    df2.to_csv("./game.csv", sep = ';')
    df3.to_csv("./riwayat.csv", sep = ';')
    df4.to_csv("./kepemilikan.csv", sep = ';')

# F17 - Exit
def exit():
    answer = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ").lower()
    while (answer != "y" and answer != "n"):
        answer = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ").lower()
    return answer
    # return dalam char 'y' atau 'n'

# Fungsi lain-lain
def printdataframe(dfuser, dfgame, dfriwayat, dfkepemilikan):       # Untuk melihat dataframe, hanya bisa diakses oleh admin
    print("Ketik data yang ingin dilihat (1-4).")
    choice = input("1. User, 2. Game, 3.Riwayat, 4. Kepemilikan : ")
    
    if (choice == '1'):
        print(dfuser)
    elif (choice == '2'):
        print(dfgame)
    elif (choice == '3'):
        print(dfriwayat)
    elif (choice == '4'):
        print(dfkepemilikan)
    else :
        print("Pilihan data invalid.")



# Program Utama
program = True                  # variabel program adalah syarat untuk menjalankan program

while (program == True):
    print("========================================================================================")
    print("Tindakan yang bisa dilakukan tanpa login: 'login', 'kerangajaib', 'tictactoe', dan 'exit'")
    action = input("Silahkan ketikkan perintah: ").lower()
    logged = False              # Variabel yang menjelaskan apakah pengguna sudah login atau belum
    if (action == 'login'):
        index = login(dfuser)
        if (index == None):
            logged = False
        else :
            logged = True

        while(logged == True):      # Pengguna sudah masuk ke suatu akun
            print("==============================================")
            print("User ID  :", dfuser['id'].iloc[index])
            print("Nama     :", dfuser['nama'].iloc[index])
            print("Role     :", dfuser["role"].iloc[index])
            role = dfuser['role'].iloc[index]

            # Menanyakan kembali pengguna, tindakan yang akan dilakukan
            action = input("Tindakan apa yang akan dilakukan: ").lower()

            # Jika input adalah register
            if (action == 'register'):
                if (role == 'admin'):
                    dfuser = register(dfuser)
                else:
                    print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")

            # Jika action adalah login
            elif (action == 'login'):
                if (login(dfuser) != None):         # Index berubah hanya jika login berhasil ke akun baru berhasil dilakukan 
                    index = login(dfuser)          
            
            # Jika action adalah help
            elif (action == 'help'):
                help(role)

            # Jika action adalah exit
            elif (action == 'exit'):
                if (exit() == 'y'):
                    save(dfuser, dfgame, dfriwayat, dfkepemilikan)
                    program = False
                    logged = False
                else :
                    program = False
                    logged = False
            
            # Jika action adalah print
            elif (action == 'print'):
                if (role == 'admin'):
                    printdataframe(dfuser,dfgame,dfriwayat,dfkepemilikan)
                else:
                    print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
            
            # Memainkan permainan kerang ajaib
            elif(action == 'kerangajaib'):
                kerangajaib()

            # Memainkan permainan tictactoe
            elif(action == 'tictactoe'):
                tictactoe()

            # Input pengguna merupakan fungsi yang tidak dapat diproses
            else:
                print("Maaf perintah tersebut tidak dapat diproses.")

    # Melakukan permainan kerang ajaib tanpa melakukan login
    elif (action == 'kerangajaib'):
            kerangajaib()
    # Melakukan permainan tictactoe tanpa melakukan login
    elif (action == 'tictactoe'):
            tictactoe()
    # Jika action adalah exit
    elif (action == 'exit'):
        if (exit() == 'y'):
            save(dfuser, dfgame, dfriwayat, dfkepemilikan)
            program = False
        else :
            program = False
    else :                              # pengguna tidak menginputkan 'login'
        print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login".')




