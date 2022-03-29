# Identitas


# Kamus



# Algoritma
import pandas as pd

# Inisasi Data
dfuser = pd.read_csv("./user.csv", sep = ';')
dfgame = pd.read_csv("./game.csv", sep = ';')
dfriwayat = pd.read_csv("./riwayat.csv", sep = ';')
dfkepemilikan = pd.read_csv("./kepemilikan.csv", sep =';')

# F2 - Register
# F3 - Login
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
    else :                                                              # role == 'user'
        print("================ HELP ================ ")
        print("login                - Melakukan login ke dalam sistem.")                                            #F3
        print("list_game_toko       - Mengurutkan game yang ada pada toko berdasarkan data tertentu.")              #F7
        print("buy_game             - Membeli game tertentu dari toko.")                                            #F8
        print("list_game            - Mengurutkan seluruh game yang dimiliki berdasarkan parameter tertentu.")      #F9
        print("search_my_game       - Mencari game tertentu berdasarkan parameter tertentu.")                       #10
        print("search_game_at_store - Mencari game berdasarkan parameter yang diinputkan.")                         #F11

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
    answer = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)").lower()
    while (answer != "y" and answer != "n"):
        answer = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)").lower()
    return answer
    # return dalam char 'y' atau 'n'

# Program Utama
program = True                  # variabel program adalah syarat untuk menjalankan program

while (program == True):
    action = input("Tindakan apa yang akan dilakukan: ").lower()
