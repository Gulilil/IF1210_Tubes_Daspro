# Subprogram F2 hingga F7
# File ini berisikan fungsi-fungsi yang digunakan untuk menjalankan program mulai dari Fungsi ke 2 hingga Fungsi ke 7

# Kamus Global :
'''
    alphabet : string = "abcdefghijklmnopqrstuvwxyz"
    numbersymbol : string = "0123456789-_"
'''

# Algoritma Subprogram
from password import *
from csvlistfunction import *

alphabet = "abcdefghijklmnopqrstuvwxyz"
numbersymbol  = "0123456789-_"


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
'''
MASIH DALAM TAHAP PENGERJAAN
def tambah_game(game):
   id_game = input("Masukkan ID Game: ")
   isAda = False  

   length = lengthlist (game)

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

    if (isAda == True):
        found = True
        cekEmpty = True
        cekoutpu1 = False
        cekoutput2 = False
        while found == True or cekEmpty == True:
            if cekoutput2 == False:
                if cekoutput1 == True:
                    print("Gagal menambahkan game karena game sudah ada.")
            else:
                print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
        
            namaGame = input("Masukkan nama game: ")
            kategori = input("Masukkan kategori: ")
            tahun = input("Masukkan tahun rilis: ")
            harga = input("Masukkan harga: ")
            stok = input("Masukkan stok awal: ")

            cekEmpty = cekInputKosong(namaGame,kategori,tahun,harga,stok)
            cekoutput1 = found
            cekoutput2 = cekEmpty

    print("Selamat! Berhasil menambahkan game ", namaGame)
    print()
    newgame = ['G' + id_game(),namaGame,kategori,tahun,harga,stok]
    index += [newgame]
    return index
'''
# F5 - Mengubah Game pada Toko
# F6 - Mengubah Stok Game di Toko
def ubah_stok(game):
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
            game[index][5] = stok
            print(jumlah_baru, "stok dari", game[index][1],"berhasil ditambahkan. Stok sekarang:", (stok))
    else:                                                                     # Dilakukan apabila tidak ada game dengan id tersebut
        print("Tidak ada item dengan ID tersebut!")
# F7 - Listing Game di Toko 
