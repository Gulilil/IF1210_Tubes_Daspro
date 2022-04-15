# Subprogram F8 hingga F13
# File ini berisikan fungsi-fungsi yang digunakan untuk menjalankan program mulai dari Fungsi ke 8 hingga Fungsi ke 13

# Algoritma Sub Program 
from csvlistfunction import *

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
    try:                                                            # Melakukan handle error selain angka
        saldo = float(input("Masukkan saldo: "))
        
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