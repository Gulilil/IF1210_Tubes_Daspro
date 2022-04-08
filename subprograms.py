import os
import time
from kerangajaib import kerangajaib
from tictactoe import tictactoe
from password import *
from csvlistfunction import *

# Kamus :

# SUB PROGRAM
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
def search_my_game(dfgame,dfkepemilikan, id):
    filter_id = input("Masukkan ID Game: ")
    filter_tahun = input("Masukkan Tahun Rilis Game: ")

    # Mengisi array mygame dengan data game yang dimiliki user
    mygame = []
    for i in range(1, lengthlist(dfkepemilikan)):
            if dfkepemilikan[i][1] == id :            # Jika sesuai dengan indeks user, maka
                mygame += [dfkepemilikan[i][0]]     # game akan disimpan ke list mygame
    sortlist(mygame)                                # Sorting untuk mengurutkan indeks game dari urutan terkecil

    # Prosedur mencetak game sesuai filter
    def selection(nomor,j):
        print(nomor,end='. ')
        for k in range(5):               
            print(dfgame[j][k],end=' | ')
        print()
    
    # Proses mencari data dari game user
    print("Daftar game pada inventory yang memenuhi kriteria: ")
    nomor = 0                                          # Inisialisasi nomor game yang akan dicetak
    check = False
    for i in range(lengthlist(mygame)):
        for j in range(1, lengthlist(dfgame)):
            if mygame[i] == dfgame[j][0]:                   # Indeks game sesuai dengan indeks pada game.csv
                if not filter_id and not filter_tahun :     # Tidak ada kriteria sehingga output adalah semua game     
                    nomor += 1
                    check = True                        # user memiliki game di dalam library
                    selection(nomor,j)
                    
                elif not filter_id and filter_tahun :   # Hanya ada filter tahun, output game dengan tahun sesuai
                    if filter_tahun == dfgame[j][3]:    # Filter_tahun sesuai dengan tahun rilis game
                        nomor += 1
                        check = True                    # user memiliki game di dalam library
                        selection(nomor,j)

                elif filter_id  and not filter_tahun :  # Hanya ada filter ID game, output game dengan ID sesuai
                    if filter_id == dfgame[j][0]:       # Indeks game user sama dengan indeks game pada game.csv
                        nomor += 1                      
                        check = True                    # user memiliki game di dalam library
                        selection(nomor,j)

                else:                                                              # filter_tahun dan filter_id terisi      
                    if filter_id == dfgame[j][0] and filter_tahun == dfgame[j][3]: # Filter tahun dan ID game yang sesuai
                        nomor += 1
                        check = True
                        selection(nomor,j)
    if not check:                                          # Jika check = False, maka tidak ada data game yang dimiliki user
        print("Tidak ada game pada inventory-mu yang memenuhi kriteria")

# F11 - Mencari Game di Toko 
def search_game_at_store(dfgame):
    temp = []                                               # Inisialisasi dari list yang akan diisi game yang sesuai filter
    idgame = input("Masukkan ID Game: ")                    # Input ID Game
    ngame = input("Masukkan Nama Game: ")                   # Input nama game
    hgame = input("Masukkan Harga Game: ")                  # Input harga game
    catgame = input("Masukkan Kategori Game: ")             # Input kategori game
    trgame = input("Masukkan Tahun Rilis Game: ")           # Input tahun rilis game

    # Fungsi jika filter merupakan yang pertama
    def filterawal(filter,c,temp):                      # fungsi dijalankan jika filter yang diisi adalah yang pertama kali
        for i in range(lengthlist(dfgame)):                 
            if filter == dfgame[i][c]:                  # filter sesuai dengan isi game
                temp += [dfgame[i]]                     # temp akan diisi oleh data game yang sesuai
        return temp                                     # nilai temp dikembalikan

    # Fungsi jika filter bukan yang pertama
    def filternext(filter, b,temp):                     # fungsi yang dijalankan apabila filter yang diisi bukan yang pertama kali
        temp2=[]                                        # Inisialisasi dari list sementara dari list temp
        for i in range(lengthlist(temp)):               
            if filter == temp[i][b]:                    # filter selanjutnya sesuai dengan isi game pada list temp
                temp2 = [temp[i]]                       # list temp2 akan diisi data yang sesuai
        temp = temp2                                    # temp akan diganti dengan temp2 yang sudah difilter
        return temp                                     # nilai temp akan dikembalikan
    
    # Fungsi mencetak
    def printing(n, list):                              # fungsi untuk mencetak hasil filter
        nomor = 1                                       # inisialisasi nomor data di awal cetak
        for i in range(n, lengthlist(list)):        
            print(nomor,end='. ')                       # nomor dicetak
            for j in range(6):
                print(list[i][j], end=' | ')            # mencetak semua detail dari game, mulai dari id sampai stok
            print()
            nomor += 1                                  # nomor akan selalu ditambah 1

    # Loop filter dari game
    check = True                                        # inisialisasi dari variabel check
    first = True                                        # inisialisasi variabel first yang berarti pertama kali dijalankan
    while check:
        if idgame:                                      # idgame terisi
            filterawal(idgame ,0, temp)                 # filter awal              
            first = False                               # filter merupakan yang pertama diisi, sehingga filter selanjutnya bukan first (first = False)
            if not temp:                                # filter terisi, namun hasil filter kosong
                break                                   # loop berhenti
    
        if ngame:                                       # nama game terisi
            if first:                                   # merupakan yang pertama diisi
                filterawal(ngame ,1, temp)              # filter awal
                first = False                           # filter merupakan yang pertama diisi, sehingga filter selanjutnya bukan first (first = False)
                if not temp:                            # filter terisi, namun hasil filter kosong 
                    break                               # loop berhenti
            else:
                if temp:                         # temp terisi, bukan filter pertama
                    filternext(ngame, 1, temp)   # filter tahap selanjutnya
                    if not temp:
                        break                           

        if hgame:       # harga game terisi
            if first:   # merupakan yang pertama diisi
                filterawal(hgame ,4, temp)  # filter awal                      
                first = False               # filter merupakan yang pertama diisi, sehingga filter selanjutnya bukan first (first = False)
                if not temp:                # filter terisi, namun hasil filter kosong
                    break                   # loop berhenti
            else:
                if temp:                        # temp terisi, bukan filter pertama
                    filternext(hgame, 4, temp)  # filter selanjutnya
                    if not temp:                # hasil filter list kosong atau tidak ada yang sesuai
                        break                   # loop berhenti
                    
        if catgame:     # kategori game terisi
            if first:   # merupakan yang pertama diisi
                filterawal(catgame ,2, temp)    # filter awal            
                first = False                   # filter merupakan yang pertama diisi, sehingga filter selanjutnya bukan first (first = False)
                if not temp:                    # filter terisi, namun hasil filter kosong
                    break
            else:
                if temp:                            # temp terisi, bukan filter pertama
                    filternext(catgame, 2, temp)    # filter selanjutnya
                    if not temp:                    # hasil filter list kosong atau tidak ada yang sesuai
                        break                       # loop berhenti

        if trgame:      # tahun rilis game terisi
            if first:   # merupakan yang pertama diisi
                filterawal(trgame ,3, temp) # filter awal            
                first = False               # filter merupakan yang pertama diisi, sehingga filter selanjutnya bukan first (first = False)
                if not temp:                # filter terisi, namun hasil filter kosong
                    break
            else:
                if temp:                        # temp terisi, bukan filter pertama
                    filternext(trgame, 3, temp) # filter selanjutnya
                    if not temp:                # hasil filter list kosong atau tidak ada yang sesuai
                        break                   # loop berhenti
        check = False

    print("Daftar game pada toko yang memenuhi kriteria: ")
    if not idgame and not ngame and not hgame and not catgame and not trgame:   # filter kosong
        printing(1, dfgame) # output adalah semua game di toko
    else:                   # filter ada yang terisi
        if not temp:        # hasil filter kosong
            print("Tidak ada game yang memenuhi kriteria")
        elif temp:          # filter terisi
            printing(0, temp)   # output adalah game hasil filter yang terdapat pada list temp
    
# F12 - Top Up Saldo
def topup(dfuser):
    username = input("Masukkan username: ")
    saldo = int(input("Masukkan saldo: "))

    check = False                                           # Inisialisasi validasi user
    for i in range(1, lengthlist(dfuser)):                   
        if username == (dfuser[i][1]):                      # User tervalidasi
            saldoakhir = int(dfuser[i][5])                  # data saldo user diubah menjadi integer
            saldoakhir += saldo                             # operasi penambahan/pengurangan saldo
            if saldoakhir < 0:                              # saldo berupa negatif
                print("Masukan tidak valid")
            else:
                dfuser[i][5] = str(saldoakhir)              # saldoakhir diubah lagi menjadi string
                if (saldo >= 0):
                    print("Top up berhasil. Saldo", dfuser[i][2],"bertambah menjadi "+str(saldoakhir)+".")       # Bila ditambahkan
                else :
                    print("Top up berhasil. Saldo", dfuser[i][2],"berkurang menjadi "+str(saldoakhir)+".")       # Bila dikurangi
            check = True                                    # Nama user tersedia di user.csv
            break                                           # ketika sudah selesai maka loop dihentikan

    if not check:                                           # user tidak tersedia di user.csv
        print("Username '"+username+"' tidak ditemukan.")
    return dfuser

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
            gamenamemaxspace = 45                   # Menandakan panjang string maksimal dari sebuah nama game
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
def load():
    folder = input("Masukkan nama folder yang ingin dibuka: ")
    
    if (folder == None):                                        # Jika pengguna tidak menginputkan apapun
        print("Tidak ada nama folder yang diberikan!")
        return None, None, None, None
    else:
        # Melakukan pengecekan apakah folder dengan nama yang diinputkan memang benar ada
        check = os.path.isdir("./csv files/"+folder)
        if (check == False):                                    # Folder tersebut tidak ada
            print('Folder "'+folder+'" tidak ditemukan.')
            return None, None, None, None
        else:                                                   # Folder tersebut memang ada
            dfuser = csvtolist("user",6,folder)
            dfgame = csvtolist("game",6,folder)
            dfriwayat = csvtolist("riwayat",5,folder)
            dfkepemilikan = csvtolist("kepemilikan", 2,folder)
            print('Selamat datang di antarmuka "Binomo"')
            return dfuser, dfgame, dfriwayat, dfkepemilikan

# F16 - Save
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
        listtocsv('user', 6, folder, df1)
        listtocsv('game', 6, folder, df2)
        listtocsv('riwayat', 5, folder, df3)
        listtocsv('kepemilikan', 2, folder, df4)
    else :                                          # Dilakukan jika tidak ada file dengan nama tersebut
        parent_dir = "./csv files"
        path = os.path.join(parent_dir, folder)         # Fungsi untuk menggabung
        os.mkdir(path)                                  # Command untuk membuat directory baru
        listtocsv('user', 6, folder, df1)
        listtocsv('game', 6, folder, df2)
        listtocsv('riwayat', 5, folder, df3)
        listtocsv('kepemilikan', 2, folder, df4)
    
    print("Data telah disimpan pada folder "+folder+"!")

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