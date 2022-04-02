# Identitas


# Kamus



# Algoritma
from kerangajaib import kerangajaib
from tictactoe import tictactoe
from password import *
from csvlistfunction import *

# Inisasi Data
dfuser = csvtolist("user",6)
dfgame = csvtolist("game",6)
dfriwayat = csvtolist("riwayat",5)
dfkepemilikan = csvtolist("kepemilikan", 2)

# F2 - Register
alphabet = "abcdefghijklmnopqrstuvwxyz"
numbersymbol = "0123456789-_"

def register(dfuser):
    nama = input("Masukan nama: ")
    username = input("Masukan username: ")
    password = input("Masukan password: ")

    # Menghitung panjang dfuser
    length = lengthlist(dfuser)

    # Melakukan cek apakah terdapat username yang sama
    sameuser = False
    for i in range(length):
        if (dfuser[i][1] == username):                              # Kolom index 1 adalah kolom dimana username disimpan
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

    # Melakukan penggabungan 2 list
    newid = length
    newuserlist = [str(newid), username, nama, password, "user", "0"]
    mergedlist = mergelist(dfuser, newuserlist)
    print("Username", username,' telah berhasil register ke dalam "Binomo".')
    return mergedlist

# F3 - Login
def login(dfuser):
    username = input("Masukan username: ")
    password = input("Masukan password: ")

    # Menghitung panjang dfuser
    length = lengthlist(dfuser)
        
    # Melakukan verifikasi terhadap username dan password
    index = 0
    available = False       # Variabel untuk menjelaskan apakah username ada pada dataframe
    search = True           # Variabel untuk melakukan pencarian terhadap data user
    while (search == True):
        if (dfuser[index][1] == username):              # kolom index 1 merupakan kolom username pada df user
            available = True            # Data username terdapat pada dataframe
            search = False              # Pencarian tidak perlu dilakukan lagi
        if (index == length -1  and dfuser[index][1] != username ):    # Sampai suku terakhir, tidak ditemukan data pengguna
            available = False
            search = False
        if (search == True):            # Jika search = False, tidak perlu lagi dilakukan penambahan index
            index = index + 1
    if (available == True):
        # Mengeluarkan pernyataan login 
        # Bila benar, mengembalikan data pengguna berada pada index ke berapa
        # Bila salah, tidak mengembalikan apapun

        # Mengembalikan chippered password ke initial password
        initialpass = decryptpass(dfuser[index][3], alphabet)           # kolom index ke 3 adalah kolom password disimpan
        # Melakukan cek apakah password yang dimasukan sama dengan initial password
        if (initialpass == password):
            print("Halo "+ dfuser[index][2] +'! Selamat datang di "Binomo".')           # kolom index ke 2 adalah kolom nama disimpan
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
def riwayat(id, dfriwayat):
    # Format GameID | Nama game | Harga | Tahun Beli
    
    # Menghitung panjang dfriwayat
    length = lengthlist(dfriwayat)

    # Melakukan pencarian id pada dfriwayat
    gameamount = 0                                  # Variabel digunakan untuk menghitung banyak game yang dimiliki
    print("Daftar Game: ")
    for i in range(length):                                 # i adalah variabel penghitung untuk pertambahan baris pada list dfriwayat
        if (dfriwayat[i][3]== id):                  # Kolom index 3 adalah kolom dimana user_id disimpan
            gameamount +=1
            gameid = dfriwayat[i][0]                                # Kolom index 0 adalah kolom dimana game_id disimpan
            gamename = dfriwayat[i][1]                              # Kolom index 1 adalah kolom dimana game name disimpan
            price = dfriwayat[i][2]
            year  = dfriwayat[i][4]

            # Sebelum melakukan print, akan dimanfaatkan whitespace sehingga output terlihat lebih rapih
            gamenamemaxspace = 60                    # Menandakan panjang string maksimal dari sebuah nama game
            pricemaxspace = 15                       # Menandakan panjang string maksimal dari sebuah harga game
            price = str(price)
            gamename = str(gamename)
            pricelength = 0 ; namelength = 0

            # Menghitung panjang string price dan gamename
            for i in price:
                pricelength +=1
            for i in gamename:
                namelength +=1

            # Jika length lebih panjang dari maxspace, maka banyak whitespace adalah 0
            if (namelength > gamenamemaxspace):
                namewhitespace = 0
            else:
                namewhitespace = gamenamemaxspace - namelength
            if (pricelength > pricemaxspace):
                pricewhitespace = 0
            else:
                pricewhitespace = pricemaxspace - pricelength
            
            print(str(gameamount)+". "+ str(gameid)+" | "+str(gamename)+namewhitespace*" "+" | "+str(price)+pricewhitespace*" "+" | "+str(year)+" | ")

    if (gameamount == 0):
        print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah 'buy_game' untuk membeli.")


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
    # Belum ditambahin os.walk
    # Secara berturut-turut df1 = dfuser, df2 = dfgame, df3 = dfriwayat, df4 = dfkepemilikan.

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
            id = dfuser[index][0]                                               # Kolom index 0 adalah kolom dimana id disimpan
            role = dfuser[index][4]                                             # Kolom index 4 adalah kolom dimana role disimpan
            print("User ID  :", id)
            print("Nama     :", dfuser[index][2])                               # Kolom index 2 adalah kolom dimana nama disimpan
            print("Role     :", role)
            

            # Menanyakan kembali pengguna, tindakan yang akan dilakukan
            action = input("Tindakan apa yang akan dilakukan: ").lower()

            # Jika input adalah register
            if (action == 'register'):
                if (role == 'admin'):   
                    dfuser = register(dfuser)                       # List dfuser diubah dengan dfuser gabungan yang baru
                else:
                    print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")

            # Jika action adalah login
            elif (action == 'login'):
                newindex = login(dfuser)
                if (newindex != None):                  # Index berubah hanya jika login berhasil ke akun baru berhasil dilakukan
                    index = newindex

            # Jika action adalah riwayat
            elif (action == 'riwayat'):
                if (role == 'admin'):
                    print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
                else:
                    riwayat(id, dfriwayat)
            
            # Jika action adalah help
            elif (action == 'help'):
                help(role)

            # Jika action adalah exit
            elif (action == 'exit'):
                if (exit() == 'y'):
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
            program = False
        else :
            program = False
    else :                              # pengguna tidak menginputkan 'login'
        print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login".')




