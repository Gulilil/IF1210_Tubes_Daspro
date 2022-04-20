# Subprogram F8 hingga F13
# File ini berisikan fungsi-fungsi yang digunakan untuk menjalankan program mulai dari Fungsi ke 8 hingga Fungsi ke 13

# Algoritma Sub Program 
from csvlistfunction import *
import time

# F8 - Membeli Game
def buy_game(dfuser, dfgame, dfkepemilikan, dfriwayat, userID, index):
    print("========================================================================================")
    gameID = input("Masukkan ID Game: ")

    # Menghitung panjang data setiap matrix
    userLength = lengthlist(dfuser)
    gameLength = lengthlist(dfgame)
    kepemilikanLength = lengthlist(dfkepemilikan)

    # Cek apakah selama ID Game yang diinputkan benar ada pada data
    def gameAvailable(dfgame, gameID, gameLength):
        for i in range(gameLength):
            if (dfgame[i][0] == gameID):                # Pengecekan pada kolom index 0 karena kolom tersebut menyimpan data ID Game
                return [True, i]
        return [False, -999]                             # Mengembalikan False bila sampai akhir pengecekan tidak ditemukan ID tersebut
    
    def gameOwned(dfkepemilikan, gameID, kepemilikanLength, userID):
        for i in range(kepemilikanLength):
            if (dfkepemilikan[i][0] == gameID and dfkepemilikan [i][1] == userID):  #Melakukan pengecekan pada data kepemilikan game
                return True
        return False                                # Mengembalikan False apabila sampai akhir pengecekan, user tersebut tidak memiliki game yang ingin dibeli

    def cekSaldo(dfuser, userLength, userID, dfgame, gameLength, gameID):
        for i in range(gameLength):
            if (dfgame[i][0] == gameID):                # Dilakukan pencarian harga untuk game dengan ID yang diinputkan
                price = float(dfgame[i][4])
        for i in range(userLength):
            if (dfuser[i][0] == userID):                # Dilakukan pencarian saldo untuk user ID 
                saldo = float(dfuser[i][5])
        if (saldo >= price):                                    # Saldo tidak cukup
            return [True, saldo-price]
        else:
            return [False, saldo]
    
    def cekStok(dfgame, gameLength, gameID):
        for i in range(gameLength):
            if (dfgame[i][0] == gameID):                # Dilakukan pencarian harga untuk game dengan ID yang diinputkan
                stok = int(dfgame[i][5])                # kolom index 5 menyimpan data stok
        if (stok <= 0):                                         # Stok habis
            return [False, stok]
        else:
            return [True, stok-1]
    
    # Melakukan setiap pengecekan
    resultGame = gameAvailable(dfgame, gameID, gameLength)
    available = resultGame[0]
    gameIndex = resultGame[1]
    if (available == False):                # Input ID yang dimasukkan salah
        print('Game dengan ID "'+gameID+'" tidak ada pada data kami.')
        return dfuser, dfkepemilikan, dfriwayat
    if (gameOwned(dfkepemilikan, gameID, kepemilikanLength, userID) == True):   # user sudah memiliki game tersebut
        print('Anda sudah memiliki game tersebut!')
        return dfuser, dfkepemilikan, dfriwayat

    resultSaldo = cekSaldo(dfuser, userLength, userID, dfgame, gameLength, gameID)
    resultStok = cekStok(dfgame, gameLength, gameID)
    if (resultSaldo[0] == False):                                           # Saldo user tidak mencukupi
        print("Saldo anda tidak cukup untuk membeli Game tersebut!")
        return dfuser, dfkepemilikan, dfriwayat
    if (resultStok[0] == False):                                            # Stok game tidak ada
        print("Stok game tersebut sudah habis!")
        return dfuser, dfkepemilikan, dfriwayat
    
    # Jika lolos dari serangkaian pengecekan, maka game akan dibeli
    dfuser[index][5] = str(resultSaldo[1])                    # Mengubah data saldo pengguna
    gameName = dfgame[gameIndex][1]                     # kolom index adalah kolom dimana nama game disimpan

    # Penambahan list untuk dfkepemilikan
    kepemilikanArray = [0 for i in range(2)]
    kepemilikanArray[0] = gameID
    kepemilikanArray[1] = userID
    dfkepemilikan = mergelist(dfkepemilikan, kepemilikanArray)      # Menggabungkan matrix dengan baris baru
    dfkepemilikan = sortmatrix(dfkepemilikan, 0)                    # Mengurutkan data pada matrix
    # Penambahan list untuk dfriwayat
    riwayatArray = [0 for i in range(5)]
    riwayatArray[0] = gameID
    riwayatArray[1] = dfgame[gameIndex][1]
    riwayatArray[2] = dfgame[gameIndex][4]
    riwayatArray[3] = userID
    local = time.localtime()                                # local adalah variabel untuk menyatakan localtime
    year = time.strftime("%Y", local)
    riwayatArray[4] = year
    dfriwayat = mergelist(dfriwayat, riwayatArray)                  # Menggabungkan matrix dengan baris baru
    dfriwayat = sortmatrix(dfriwayat, 0)                            # Mengurutkan data pada matrix
    print('Game "'+gameName+'" berhasil dibeli!')
    
    return dfuser, dfkepemilikan, dfriwayat

# F9 - Melihat Game yang dimiliki
# F10 - Mencari Game yang dimiliki
# Subprogram mencari game yang dimiliki
# procedure search_my_game(input dfgame matrix, input dfkepemilikan matrix, input id string)
'''
Deskripsi :
Prosedur ini memiliki beberapa parameter, yaitu 'dfgame' dan 'dfkepemilikan' yang bertipe matrix serta
'id' yang bertipe string. Prosedur ini akan mencetak game yang dimiliki user sesuai pada data dfkepemilikan.csv.
Jika filter tidak diisi, maka prosedur ini akan mencetak seluruh game yang dimiliki user, tetapi jika salah satu input
tidak tepat, maka prosedur tidak akan mencetak pesan bahwa game tidak tersedia.

Kamus :
    filter_id, filter_tahun : string
    mygame : array of string
    jarak, nomor : int
    check : bool
    function maxlength(int indeks, matrix list) -> int
    procedure printing(input nomor int, input indeks string)
    
'''
def search_my_game(dfgame,dfkepemilikan, id):
    print("========================================================================================")
    filter_id = input("Masukkan ID Game: ")
    filter_tahun = input("Masukkan Tahun Rilis Game: ")

    # Mengisi array mygame dengan data game yang dimiliki user
    mygame = []
    for i in range(1, lengthlist(dfkepemilikan)):
            if dfkepemilikan[i][1] == id :                  # Jika sesuai dengan indeks user, maka
                mygame += [dfkepemilikan[i][0]]             # game akan disimpan ke list mygame
    sortlist(mygame)                                        # Sorting untuk mengurutkan indeks game dari urutan terkecil

    # Fungsi untuk mencari nilai dari elemen yang terpanjang
    def maxlength(indeks,list):
        jarak = 0                                           # Inisialisasi variabel jarak
        for i in list:                                      # i adalah elemen dari list pada parameter
            if lengthlist(i[indeks]) >= jarak:              # panjang elemen lebih panjang dari jarak
                jarak = lengthlist(i[indeks])               # jarak diganti dengan nilai dari elemen terpanjang pada list
        return jarak                                        # nilai jarak dikembalikan

    # Prosedur mencetak game sesuai filter
    def printing(nomor,indeks):
        print(nomor,end='. ')                                   # mencetak nomor dari daftar
        for k in range(5):                                      # atribut id game hingga harga game
            jarak = maxlength(k, dfgame)                        # variabel jarak merupakan nilai elemen terpanjang
            print(f"{dfgame[indeks][k]:<{jarak}}", end=' | ')   
        print()                                                 # print kosong untuk jarak antar baris
    
    # Proses mencari data dari game user
    print("Daftar game pada inventory yang memenuhi kriteria: ")
    nomor = 0                                               # Inisialisasi nomor game yang akan dicetak
    check = False                                           # Inisialisasi variabel check
    for i in range(lengthlist(mygame)):
        for j in range(1, lengthlist(dfgame)):
            if mygame[i] == dfgame[j][0]:                   # Indeks game sesuai dengan indeks pada game.csv
                if not filter_id and not filter_tahun :     # Tidak ada kriteria sehingga output adalah semua game     
                    nomor += 1
                    check = True                            # user memiliki game di dalam library
                    printing(nomor,j)
                    
                elif not filter_id and filter_tahun :       # Hanya ada filter tahun, output game dengan tahun sesuai
                    if filter_tahun == dfgame[j][3]:        # Filter_tahun sesuai dengan tahun rilis game
                        nomor += 1
                        check = True                        # user memiliki game di dalam library
                        printing(nomor,j)

                elif filter_id  and not filter_tahun :      # Hanya ada filter ID game, output game dengan ID sesuai
                    if filter_id == dfgame[j][0]:           # Indeks game user sama dengan indeks game pada game.csv
                        nomor += 1                      
                        check = True                        # user memiliki game di dalam library
                        printing(nomor,j)

                else:                                                              # filter_tahun dan filter_id terisi      
                    if filter_id == dfgame[j][0] and filter_tahun == dfgame[j][3]: # Filter tahun dan ID game yang sesuai
                        nomor += 1
                        check = True
                        printing(nomor,j)
    if not check:                                                                  # Jika check = False, maka tidak ada data game yang dimiliki user
        print("Tidak ada game pada inventory-mu yang memenuhi kriteria")

# F11 - Mencari Game di Toko
# Subprogram mencari game di toko
# procedure search_game_at_store (input dfgame matrix)
'''
Deskripsi :
Prosedur ini memiliki parameter berupa 'dfgame' yang bertipe matrix. Prosedur ini akan mencetak game
yang sudah difilter sesuai keinginan user. Jika filter tidak diisi, maka filter tersebut dianggap tidak ada.
Namun, jika ada input satu filter yang salah, maka prosedur akan mencetak pesan bahwa game tidak ada.

Kamus :
    temp, temp2, hasil : matrix of string
    idgame, ngame, hgame, catgame, trgame : string
    jarak, nomor : int
    function filterawal(string filter, string indeks, matrix temp) -> matrix of string
    function filternext(string filter, string indeks, matrix temp) -> matrix of string
    function maxlength(int indeks, matrix list) -> int
    procedure printing(input n integer, input list matrix)

'''
def search_game_at_store(dfgame):
    print("========================================================================================")
    temp = []                                               # Inisialisasi dari list sementara game yang sesuai filter
    hasil = []                                              # Inisialisasi dari list akhir game yang sesuai filter
    idgame = input("Masukkan ID Game: ")                    # Input ID Game
    ngame = input("Masukkan Nama Game: ")                   # Input nama game
    hgame = input("Masukkan Harga Game: ")                  # Input harga game
    catgame = input("Masukkan Kategori Game: ")             # Input kategori game
    trgame = input("Masukkan Tahun Rilis Game: ")           # Input tahun rilis game

    # Fungsi jika filter merupakan yang pertama
    def filterawal(filter,indeks,temp):                     # fungsi dijalankan jika filter yang diisi adalah yang pertama kali
        for i in range(lengthlist(dfgame)):                 # loop sebanyak game pada game.csv
            if filter == dfgame[i][indeks]:                 # filter sesuai dengan isi game
                temp += [dfgame[i]]                         # temp akan diisi oleh data game yang sesuai
        return temp                                         # nilai temp dikembalikan

    # Fungsi jika filter bukan yang pertama
    def filternext(filter,indeks,temp):                     # fungsi yang dijalankan apabila filter yang diisi bukan yang pertama kali
        temp2=[]                                            # Inisialisasi dari list sementara dari list temp
        for i in range(lengthlist(temp)):                   # loop sebanyak game yang sudah difilter awal
            if filter == temp[i][indeks]:                   # filter sesuai dengan data pada list temporary
                temp2 += [temp[i]]                          # list temp2 akan diisi data yang sesuai             
        temp = temp2                                        # temp akan diganti dengan temp2 yang sudah difilter
        return temp                                         # nilai temp akan dikembalikan
        
    # Fungsi untuk mencari nilai dari elemen yang terpanjang
    def maxlength(indeks,list):
        jarak = 0                                           # Inisialisasi variabel jarak
        for i in list:                                      # i adalah elemen dari list pada parameter
            if lengthlist(i[indeks]) >= jarak:              # panjang elemen lebih panjang dari jarak
                jarak = lengthlist(i[indeks])               # jarak diganti dengan nilai dari elemen terpanjang pada list
        return jarak                                        # nilai jarak dikembalikan

    # Prosedur mencetak
    def printing(n, list):                                  # fungsi untuk mencetak hasil filter
        nomor = 1                                           # inisialisasi nomor data di awal cetak
        for i in range(n, lengthlist(list)):                # loop sebanyak panjang list
            print("{: >2}".format(nomor),end='. ')          # nomor diformat ke kanan dengan jarak 2 lalu dicetak
            for j in range(6):
                jarak = maxlength(j,list)                   # variabel jarak sebagai jarak maksimum elemen pada list
                print(f"{list[i][j]:<{jarak}}", end=' | ')  # mencetak semua detail dari game, mulai dari id sampai stok
            print()                                         # print kosong untuk jarak antar baris
            nomor += 1                                      # nomor akan selalu ditambah 1 hingga selesai

    # Loop filter dari game
    first = True                                            # inisialisasi variabel first yang berarti pertama kali dijalankan
    while True:
        if idgame:                                          # idgame terisi
            hasil = filterawal(idgame,0,temp)               # list hasil adalah hasil filter awal              
            first = False                                   # filter merupakan yang pertama diisi, sehingga filter selanjutnya bukan first (first = False)
            if not hasil:                                   # filter terisi, namun hasil filter kosong
                break                                       # loop berhenti
    
        if ngame:                                       # nama game terisi
            if first:                                   # merupakan yang pertama diisi
                hasil = filterawal(ngame,1,temp)        # list hasil adalah hasil filter awal
                first = False                           # filter merupakan yang pertama diisi, sehingga filter selanjutnya bukan first (first = False)
                if not hasil:                           # filter terisi, namun hasil filter kosong 
                    break                               # loop berhenti
            else:
                if hasil:                               # filter yang diisi sebelumnya valid
                    temp = hasil                        # temp diganti dengan list hasil sebelumnya
                    hasil = filternext(ngame,1,temp)    # filter tahap selanjutnya
                    if not hasil:                       # hasil filter merupakan list kosong
                        break                           # loop berhenti

        if hgame:                                       # harga game terisi
            if first:                                   # merupakan yang pertama diisi
                hasil = filterawal(hgame,4,temp)        # list hasil adalah hasil filter awal                      
                first = False                           # filter merupakan yang pertama diisi, sehingga filter selanjutnya bukan first (first = False)
                if not hasil:                           # filter terisi, namun hasil filter kosong
                    break                               # loop berhenti
            else:
                if hasil:                               # filter yang diisi sebelumnya valid
                    temp = hasil                        # temp terisi, bukan filter pertama
                    hasil = filternext(hgame,4,temp)    # filter selanjutnya
                    if not hasil:                       # hasil filter list kosong atau tidak ada yang sesuai
                        break                           # loop berhenti
                    
        if catgame:                                     # kategori game terisi
            if first:                                   # merupakan yang pertama diisi
                hasil = filterawal(catgame,2,temp)      # list hasil adalah hasil filter awal            
                first = False                           # filter merupakan yang pertama diisi, sehingga filter selanjutnya bukan first (first = False)
                if not hasil:                           # filter terisi, namun hasil filter kosong
                    break                               # loop berhenti
            else:
                if hasil:                               # filter yang diisi sebelumnya valid
                    temp = hasil                        # temp terisi, bukan filter pertama
                    hasil = filternext(catgame,2,temp)  # filter selanjutnya
                    if not hasil:                       # hasil filter list kosong atau tidak ada yang sesuai
                        break                           # loop berhenti

        if trgame:                                      # tahun rilis game terisi
            if first:                                   # merupakan yang pertama diisi
                hasil = filterawal(trgame,3,temp)       # list hasil adalah hasil filter awal            
                first = False                           # filter merupakan yang pertama diisi, sehingga filter selanjutnya bukan first (first = False)
                if not hasil:                           # filter terisi, namun hasil filter kosong
                    break                               # loop berhenti
            else:
                if hasil:                               # filter yang diisi sebelumnya valid
                    temp = hasil                        # temp terisi, bukan filter pertama
                    hasil = filternext(trgame,3,temp)   # filter selanjutnya
                    if not hasil:                       # hasil filter list kosong atau tidak ada yang sesuai
                        break                           # loop berhenti
        break
    
    # Proses mencetak
    print("Daftar game pada toko yang memenuhi kriteria: ")
    if not idgame and not ngame and not hgame and not catgame and not trgame:   # filter kosong semua
        printing(1, dfgame)                                                     # output adalah semua game di toko
    else:                                                                       # filter ada yang terisi
        if not hasil:                                                           # hasil filter kosong
            print("Tidak ada game yang memenuhi kriteria")
        elif hasil:                                                             # hasil filter terisi
            printing(0, hasil)                                                  # output adalah game hasil filter yang terdapat pada list hasil

# F12 - Top Up Saldo
# Subprogram untuk top up saldo
# function topup (matrix dfuser)
'''
Deskripsi:
Fungsi ini memiliki parameter berupa 'dfuser' yang bertipe matrix. Admin harus menginput username dan saldo
yang akan ditambahkan ke akun user tersebut. Fungsi ini memiliki output berupa pesan apakah input valid atau tidak
dan apakah penambahan saldo berhasil dilakukan atau tidak. Fungsi ini juga akan mereturn 'dfuser' yang baru.

Kamus :
    username : string
    saldo : float
    saldoakhir : int
    
'''
def topup(dfuser):
    print("========================================================================================")
    username = input("Masukkan username: ")
    try:                                                            # Melakukan handle error selain angka
        saldo = float(input("Masukkan saldo: "))
        
        check = False                                           # Inisialisasi validasi user
        for i in range(1, lengthlist(dfuser)):                   
            if username == (dfuser[i][1]):                      # User tervalidasi
                saldoakhir = float(dfuser[i][5])                  # data saldo user diubah menjadi integer
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
    except :
        print("Input tersebut tidak diterima.")
    return dfuser

# F13 - Melihat Riwayat Pembayaran
# Subprogram Melihat Riwayat Pembayaran
# procedure riwayat (int id, matrix dfriwayat)
'''
Deskripsi :
Prosedur tersebut memiliki 2 input yaitu 'dfriwayat' yang bertipe matrix dan 'id' yang bertipe integer. Prosedur ini digunakan user untuk
melihat semua riwayat pembayaran yang telah dilakukannya selama berbelanja di 'Binomo'. Variabel 'dfriwayat' merupakan
matrix yang menyimpan seluruh data pembelian user dan variabel 'index' adalah id dari pengguna yang menjadi cirikhas 
bagi masing-masing pengguna.

Kamus :
    length, gameamount : int
    gamemaxspace, namelength, namewhitespace : int
    pricemaxspace, pricelength, pricewhitespace : int
    gameid, gamename, price, year : string
'''
# Algoritma 
def riwayat(id, dfriwayat):
    print("========================================================================================")
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
            
            print(str(gameamount)+". "+ gameid+" | "+gamename+namewhitespace*" "+" | "+price+pricewhitespace*" "+" | "+year+" | ")

    if (gameamount == 0):
        print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah 'buy_game' untuk membeli.")
