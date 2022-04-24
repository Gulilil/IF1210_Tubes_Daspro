# Subprogram F2 hingga F7
# File ini berisikan fungsi-fungsi yang digunakan untuk menjalankan program mulai dari Fungsi ke 2 hingga Fungsi ke 7


# Algoritma Subprogram
from password import *
from csvlistfunction import *


# F2 - Register
# Subprogram Melakukan Pendaftaran Akun
# function register(matrix dfuser)
'''
Deskripsi :
Fungsi tersebut memiliki sebuah input yaitu 'dfuser' yang bertipe matrix. Fungsi ini akan melakukan penginputan 
terhadap akun user baru yang ingin dibuat. Fungsi ini akan mengeluarkan output sebuah matrix yang telah
diinputkan data user baru tersebut. 

Kamus :
    nama, username, password : string
    length : int
    newid : int
    sameuser, uservalid : bool
    newuserlist : array of string
    mergedlist : matrix of string
    function encryptpass(string password) -> string
    function lengthlist (matrix dfuser) -> int
    function mergelist(matrix dfuser, array newuserlist) -> matrix

'''
# Algoritma 
def register(dfuser):
    print("========================================================================================")
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
        # Tetap dilakukan pengecekan apakah ada username yang sama
        for i in range(length):
            if (dfuser[i][1] == username):                              # Kolom index 1 adalah kolom dimana username disimpan
                sameuser = True
            
    
    uservalid = True
    # Melakukan cek validitas username
    for i in username:
        # Alphabet kapital berada pada rentang ord 65 hinga 90, alphabet kecil berada pada rentang 97 hingga 122
        # '-' ada pada ord 45 dan '_' ada pada ord 95, angka berada pada rentang ord 48 hingga 57
        if (ord(i) < 48 or ord(i) > 57) and (ord(i) <65 or ord(i) > 90) and (ord(i)< 97 or ord(i) > 122) and (ord(i) != 45) and (ord(i) != 95):
            uservalid = False
    while (uservalid == False):
        print("Username", username, "tidak valid. Username hanya diperkenankan mengandung alphabet, angka, underscore, dan strip")
        username = input("Masukan username: ")
        uservalid = True
        for i in username:
            if (ord(i) < 48 or ord(i) > 57) and (ord(i) <65 or ord(i) > 90) and (ord(i)< 97 or ord(i) > 122) and (ord(i) != 45) and (ord(i) != 95):
                uservalid = False

    # Mengubah password yang diinputkan menjadi chippered password 
    password = encryptpass(password)

    # Melakukan penggabungan 2 list
    newid = length
    newuserlist = [str(newid), username, nama, password, "user", "0"]
    mergedlist = mergelist(dfuser, newuserlist)
    print("Username", username,' telah berhasil register ke dalam "Binomo".')
    return mergedlist



# F3 - Login (dan Logout)
# Subprogram Melakukan Masuk ke Suatu Akun User
# function login (matrix dfuser)
'''
Deskripsi :
Fungsi tersebut memiliki sebuah input yaitu 'dfuser' yang bertipe matrix. Fungsi ini akan melakukan digunakan untuk
membaca username dan password yang diinputkan oleh pengguna untuk masuk ke suatu akun. Bila username dan password benar
(terdapat pada data), maka user akan berhasil masuk ke dalam akunnya. Fungsi ini akan mengeluarkan suatu index yang menunjukkan
index dimana suatu data user disimpan. Bila login gagal dilakukan, maka fungsi ini tidak mengeluarkan output apapun.

Kamus :
    username, password : string
    initialpass : string
    length : int
    index : int
    available, search : bool
    function decryptpass(string password) -> string
    function lengthlist(matrix dfuser) -> int
'''
# Algoritma 
def login(dfuser):
    print("========================================================================================")
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
        initialpass = decryptpass(dfuser[index][3])           # kolom index ke 3 adalah kolom password disimpan
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

# Subprogram Melakukan Keluar dari Suatu Akun User
# function logout (matrix dfuser, int index)
'''
Deskripsi :
Fungsi tersebut memiliki 2 input yaitu 'dfuser' yang bertipe matrix dan 'index' yang bertipe integer. Fungsi ini digunakan oleh user
untuk keluar dari akunnya. Bila user ingin menggunakan akun lain, maka user perlu keluar terlebih dahulu dari akun yang sedang
digunakannya. Maka dari itu, fungsi logout dibutuhkan. Bila pengguna ingin melakukan logout, maka fungsi akan mengembalikan nilai
"True", sedangkan terjadi sebaliknya bila pengguna tidak jadi melakukan logout.

Kamus :
    choice : string
'''
# Algoritma 
def logout(dfuser, index):
    print("========================================================================================")
    choice = input("Apakah anda ingin melakukan logout? (y/n) ").lower()
    if (choice == 'y'):
        print("Anda sudah keluar dari akun anda. Sampai jumpa "+dfuser[index][2]+"!")
        return True
    elif (choice == 'n'):
        print("Anda masih menggunakan akun dengan username '"+dfuser[index][1]+"'. Selamat berbelanja!")
        return False
    else:
        print("Input yang dimasukkan tidak valid.")
        return False


# F4 - Menambah Game ke Toko
# Subprogram untuk penambahan game
# function tambah_game(matrix dfgame)
'''
Deskripsi :
Fungsi tersebut memiliki sebuah input yaitu 'dfgame' yang bertipe matrix.
Fungsi ini akan melakukan digunakan untuk membaca nama game, apakah di toko sudah ada game yang memiliki nama yang sama. 
Jika sudah ada nama game yang sama di toko, maka tidak dapat menambahkan nama game tersebut dan akan meminta input ulang 
dengan nama game yang berbeda.

Kamus :
    namaGame : string
    kategori : string
    tahun : int 
    harga : int 
    stok : int
    length : int
    alreadyInStore : bool
    function checkAlreadyInStore(dfgame, namaGame) -> bool
    function lengthlist(list) -> int
    function mergelist(matrix dfgame, list newGameList) -> matrix
'''
# Algoritma
def tambah_game(dfgame):
    print("========================================================================================")
    # Melakukan check namaGame terlebih dahulu, apakah di toko sudah ada game yang memiliki nama yang sama
    namaGame = input("Masukkan nama game: ")

    # mengukur panjang matrix dfgame
    length = lengthlist(dfgame)
    
    def checkAlreadyInStore(dfgame, namaGame):
        alreadyInStore = False                  # Variabel ini menunjukkan apakah game sudah ada pada toko
        for i in range(length):
            if (dfgame[i][1] == namaGame):              # kolom indeks 1 adalah kolom yang menyimpan nama game
                alreadyInStore = True
        return alreadyInStore                       # Mengembalikan value True atau False
        
    if (checkAlreadyInStore(dfgame, namaGame)):
        print("Game '"+namaGame+"' sudah ada pada toko!")
        return dfgame
    else:                                   # Game belum ada pada toko
        kategori = input("Masukkan kategori: ")
        tahun = input("Masukkan tahun rilis: ")
        harga = input("Masukkan harga: ")
        stok = input("Masukkan stok awal: ")

    while (namaGame == "" or kategori == "" or tahun == "" or harga == "" or stok == ""):
        # Melakukan pengulangan apabila terdapat suatu informasi yang dikosongkan oleh pelaku
        print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
        namaGame = input("Masukkan nama game: ")
        if (checkAlreadyInStore(dfgame, namaGame)):
            print("Game '"+namaGame+"' sudah ada pada toko!")
            return dfgame
        else :
            kategori = input("Masukkan kategori: ")
            tahun = input("Masukkan tahun rilis: ")
            harga = input("Masukkan harga: ")
            stok = input("Masukkan stok awal: ")

    # Jika stok dan harga negatif, program akan meminta input ulang pada pengguna
    while ( int(stok) < 0 or int(harga) < 0):
            print("Nilai harga dan stok tidak mungkin negatif.")
            harga = input("Masukkan harga: ")
            stok = input("Masukkan stok awal: ")
    
    # Memasukkan data game baru pada dfgame
        # Ambil GAME ID paling terakhir
    lastID = dfgame[length-1][0]
    lastNumberID = ""
    
    # Mengukur panjang lastID
    IDlength = lengthlist(lastID)
    # Menentukan ID angka
    for i in range(4, IDlength):                        # Dimulai dari index ke 4 untuk mengambil angkanya saja (e.g. GAME001)
        lastNumberID = lastNumberID + lastID[i]
    lastNumberID = int(lastNumberID)
    newNumberID = lastNumberID + 1                      # Ditambahkan 1 untuk ID baru

    newIDlength = lengthlist(str(newNumberID))
    if (newIDlength < 3):
        zeroAmount = 3 - newIDlength
        newID = "GAME"+"0"*zeroAmount + str(newNumberID)
    else :                                                      # Panjang newID lebih dari 3
        newID = "GAME"+str(newNumberID)

    # Menggabungkan data baru pada dfgame
    newGameList = [newID, namaGame, kategori, tahun, harga, stok]
    dfgame = mergelist(dfgame, newGameList)

    print("Selamat! Berhasil menambahkan game "+namaGame+".")
    return dfgame

# F5 - Mengubah Game pada Toko
# Subprogram Pengubahan Game Pada Toko
# function ubah_game(matrix game) 
'''
Deskripsi :
Fungsi ubah_game memiliki parameter yaitu sebuah matrix yang bernama 'game'. Program akan meminta
pengguna untuk memasukan suatu IDGame yang ingin diubah. Lalu program akan mengecek apakah ID Game yang diinputkan
sudah sesuai atau belum. Bila sudah sesuai, program akan mengganti data pada matriks 'game' dengan data yang diinputkan 
oleh pengguna.

Kamus :
    gameId, newName, newKategori, newTahun, newHarga : string
    length : int
    searchResult : array
    available : bool
    gameIndex : int
    game : matrix of string
    function checkAlreadyInStore(dfgame, ID) -> array
    function lengthlist(matrix) -> int


'''
def ubah_game(game):
    # Pembuatan Fungsi Pengecekan
    def checkAlreadyInStore(dfgame, ID):
        alreadyInStore = False                  # Variabel ini menunjukkan apakah game sudah ada pada toko
        index = -999                        # indeks == -999 bila tidak ada pata toko
        for i in range(length):
            if (dfgame[i][0] == ID):              # kolom indeks 0 adalah kolom yang menyimpan ID game
                alreadyInStore = True
                index = i
        return [alreadyInStore, index]              # Mengembalikan value True atau False

    print("========================================================================================")
    gameID = input("Masukkan ID Game: ")
    newName = input("Masukkan nama game baru: ")
    newKategori = input("Masukkan kategori baru: ")
    newTahun = input("Masukkan tahun rilis baru: ")
    newHarga = input("Masukkan harga baru: ")

    # Mengukur panjang data game
    length = lengthlist (game)

    searchResult = checkAlreadyInStore(game, gameID)    
    available = searchResult[0]
    gameIndex = searchResult[1]

    while (gameID == "" or available == False):
        print("ID Game tidak dapat ditemukan. Tolong masukan ID Game dengan benar.")
        gameID = input("Masukkan ID Game: ")
        newName = input("Masukkan nama game baru: ")
        newKategori = input("Masukkan kategori baru: ")
        newTahun = input("Masukkan tahun rilis baru: ")
        newHarga = input("Masukkan harga baru: ")

        searchResult = checkAlreadyInStore(game, gameID)    
        available = searchResult[0]
        gameIndex = searchResult[1]
    
    # Memasukan data baru ke matriks data
    # Secara berturut-turut kolom yang menyimpang nama, kategori, tahun, dan harga adalah
    # Kolom index 1, 2, 3, 4
    if (newName != ""):
        game[gameIndex][1] = newName
    if (newKategori != ""):
        game[gameIndex][2] = newKategori
    if (newTahun != ""):
        game[gameIndex][3] = newTahun
    if (newHarga != ""):
        game[gameIndex][4] = newHarga
    print("Game dengan ID '"+gameID+"' telah berhasil diubah.")
    return game

# F6 - Mengubah Stok Game di Toko
'''
Deskripsi :
Fungsi tersebut memiliki sebuah input yaitu 'game' yang bertipe matrix.
Fungsi ini akan melakukan digunakan untuk membaca ID game dan membaca besar perubahan stok yang ingin dilakukan.
Bila stok suatu game bernilai nol setelah pengubahan, tidak perlu dihapus dari sistem.

Kamus :
    id_game : string
    isAda : bool
    search : bool
    index : int
    stok : int
    jumlah_baru : int
    length : int
    function lengthlist(matrix game) -> int
'''
# Algoritma
def ubah_stok(game):
    print("========================================================================================")
    id_game = input("Masukkan ID Game: ")
    isAda = False                                   # isAda adalah variabel yang menunjukkan apakah ID game yang diinputkan benar ada

    # Mengukur panjang data game
    length = lengthlist (game)

    # Mencari apakah ada game id sesuai yang diinputkan dengan user
    search = True                       # variabel yang menunjukkan apakah pencarian perlu dilakukan
    index = 0
    while (search == True):
        if (game[index][0] == id_game):
            isAda = True
            search = False              # jika idgame sudah ditemukan, pencarian sudah tidak perlu lagi dilakukan
        elif (index >= length-1):           # dilakukan jika sudah dilakukan pengecekan hingga suku terakhir, tetapi tidak ditemukan
            search = False
        if (search == True):            # Penambahan index hanya dilakukan apabila pencarian masih berlanjut
            index +=1
    
    # Melakukan pencarian bila game tersebut ada pada data
    if (isAda == True):
        print("Stock '"+game[index][1]+"' sekarang adalah "+game[index][5]+".")
        jumlah_baru = int(input("Masukkan jumlah yang ingin diubah : "))
        stok = int(game[index][5])
        if (jumlah_baru < 0):
            if(stok + jumlah_baru >= 0):                       # Stok berada pada kolom index no 5
                # Melakukan perubahan pada stok game index ke-n
                stok += jumlah_baru
                game[index][5] = stok
                print(jumlah_baru*(-1),"stok dari", game[index][1], "berhasil dikurangi. Stok sekarang:", stok)
            else :
                print(jumlah_baru*(-1),"stok dari", game[index][1], "gagal dikurangi karena stok kurang. Stok sekarang:", stok,"(<"+str(jumlah_baru*-1)+")")
        else :
            stok += jumlah_baru
            game[index][5] = str(stok)
            print(jumlah_baru, "stok dari", game[index][1],"berhasil ditambahkan. Stok sekarang:", (stok))
    else:                                                                     # Dilakukan apabila tidak ada game dengan id tersebut
        print("Tidak ada item dengan ID tersebut!")

# F7 - Listing Game di Toko 
# Subprogram listing game di toko
# prosedur list_game_toko(input dfgame matrix)
'''
Deskripsi :
Prosedur ini memiliki parameter input berupa 'dfgame' yang bertipe matrix. Prosedur ini
akan mencetak game pada toko yang diurutkan berdasarkan masukan berupa tahun atau harga,
baik secara ascending maupun descending. Jika masukan kosong, maka game akan terurut 
berdasarkan ID game secara ascending.

Kamus :
    skema                   : string
    nomor, jarak            : int
    listorder, listakhir    : array of string
    function maxlength(int indeks, matrix list) -> int
    function search(matrix dfgame, int indeks) -> array of string
    procedure printing(input nomor int, input indeks integer)
    procedure sortmin(input list1 array of string, input indeks integer)
    procedure sortmax(input list1 array of string, input indeks integer)
    
'''
def list_game_toko(dfgame):
    skema = input("Skema sorting: ")                                                    # masukan skema yang dipilih

    # Fungsi untuk menghitung seberapa panjang elemen dari list
    def maxlength(indeks,list):
        jarak = 0                                                                       # Inisialisasi variabel jarak
        for i in list:                                                                  # i adalah elemen dari list pada parameter
            if lengthlist(i[indeks]) >= jarak:                                          # panjang elemen lebih panjang dari jarak
                jarak = lengthlist(i[indeks])                                           # jarak diganti dengan nilai dari elemen terpanjang pada list
        return jarak

    # Prosedur mencetak
    def printing(list, indeks):
        nomor = 1                                                                       # inisialisasi nomor
        for i in range(lengthlist(list)):
            for j in range(lengthlist(dfgame)):
                if list[i] == dfgame[j][indeks]:                                        
                    print("{: >2}".format(nomor),end='. ')                              # mencetak nomor                                                    
                    for k in range(6):                                                             
                        jarak = maxlength(k, dfgame)                                                
                        print(f"{dfgame[j][k]:<{jarak}}", end=' | ')                    # mencetak data game                             
                    print()                                                  
                    nomor += 1

    # Fungsi untuk mencari game
    def search(dfgame, indeks):
        listorder = []                                                                  # inisialisasi list dari game
        for i in range(1, lengthlist(dfgame)):
            if not listorder:                                                           # list awal masih kosong
                listorder += [dfgame[i][indeks]]                                        # listorder diisi oleh data dari dfgame
            else:
                check = 0                                                               # inisialisasi check
                for j in range(lengthlist(listorder)):
                    if dfgame[i][indeks] == listorder[j]:                               # data dari dfgame ada yang sama dengan data pada listorder
                        check += 1                                                      # check ditambah 1
                if check == 0:                                                          # jika check tidak bertambah, maka
                    listorder += [dfgame[i][indeks]]                                    # data ditambahkan ke listorder
        return listorder                                                                # nilai listorder dikembalikan
    
    # Prosedur sort dari terkecil
    def sortmin(list1, indeks):
        if (indeks == 0):
            for i in range(lengthlist(list1) -1):                                           # panjang list hanya sampai n-1
                for j in range(lengthlist(list1) -i -1):                                    # panjang list untuk pembanding akan semakin berkurang sesuai i
                    if (list1[j] > list1[j+1]) :                                              # jika elemen n > elemen n+1, maka
                        # proses swap elemen n dengan n+1                                                                    
                        temp = list1[j]
                        list1[j] = list1[j+1]
                        list1[j+1] = temp
        else :
            for i in range(lengthlist(list1) -1):                                           # panjang list hanya sampai n-1
                for j in range(lengthlist(list1) -i -1):                                    # panjang list untuk pembanding akan semakin berkurang sesuai i
                    if (int(list1[j]) > int(list1[j+1])) :                                              # jika elemen n > elemen n+1, maka
                        # proses swap elemen n dengan n+1                                                                    
                        temp = list1[j]
                        list1[j] = list1[j+1]
                        list1[j+1] = temp
        printing(list1, indeks)                                                         # mencetak list yang telah diurutkan

    # Prosedur sort dari terbesar
    def sortmax(list1, indeks):                                                         
        for i in range(lengthlist(list1) -1):                                           # panjang list hanya sampai n-1
            for j in range(lengthlist(list1) -i -1):                                    # panjang list untuk pembanding akan semakin berkurang sesuai i
                if (int(list1[j]) < int(list1[j+1])) :                                              # jika elemen n > elemen n+1, maka
                    # proses swap elemen n dengan n+1
                    temp = list1[j]
                    list1[j] = list1[j+1]
                    list1[j+1] = temp    
        printing(list1, indeks)                                                         # mencetak list yang telah diurutkan

    # Proses Utama
    listakhir = []                                                                      # inisialisasi listakhir
    if skema == "tahun+":
        listakhir = search(dfgame, 3)                                                   # listakhir sama dengan list dari fungsi search dengan indeks tahun
        sortmin(listakhir, 3)                                                           # listakhir diurutkan dan dicetak dari tahun terkecil
    elif skema == "tahun-":                                                             
        listakhir = search(dfgame, 3)                                                   # listakhir sama dengan list dari fungsi search dengan indeks tahun
        sortmax(listakhir, 3)                                                           # listakhir diurutkan dan dicetak dari tahun terbesar
    elif skema == "harga+":
        listakhir = search(dfgame, 4)                                                   # listakhir sama dengan list dari fungsi search dengan indeks harga
        sortmin(listakhir, 4)                                                           # listakhir diurutkan dan dicetak dari harga terkecil
    elif skema == "harga-":
        listakhir = search(dfgame, 4)                                                   # listakhir sama dengan list dari fungsi search dengan indeks harga
        sortmax(listakhir, 4)                                                           # listakhir diurutkan dan dicetak dari harga terbesar
    elif skema == "":                                                                   # masukan kosong
        listakhir = search(dfgame, 0)                                                   # listakhir sama dengan list dari fungsi search dengan indeks ID game
        sortmin(listakhir, 0)                                                           # ID game diurutkan dari yang paling kecil
    else:                                                                               # masukan selain tahun+, tahun-, harga+, harga-, dan masukan kosong
        print("Skema sorting tidak valid!")                                             # pesan error
