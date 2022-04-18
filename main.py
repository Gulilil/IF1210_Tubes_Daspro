# Identitas
''' 
Kelas Dasar Pemrograman 9 - Kelompok 7
Nama anggota : 
- Juan Christopher Santoso (16521098) 
- Raymond As Mikhael Hutabarat (16521143) 
- Ferindya Aulia Berlianty (16521188) 
- Hanif Al Falih (16521332) 

'''

# Kamus


# Algoritma
import argparse
from kerangajaib import kerangajaib
from tictactoe import *
from F2_F7 import *
from F8_F13 import *
from F14_F17 import *


# Program Utama
program = False                 # variabel program adalah syarat untuk menjalankan program

parser = argparse.ArgumentParser(description="Program Binomo")
parser.add_argument('folder', type=str, help="Nama folder yang ingin dibuka.")
args = parser.parse_args()

# $python main.py main_save

if __name__ == '__main__':
    # Menjalankan fungsi load terlebih dahulu
    # Dilakukan cek apakah terdapat nama folder yang diinputkan atau tidak
    try:
        folder = load(args.folder)
        if (folder != None):
            program = True              # Program akan dimulai bila terdapat folder yang akan digunakan
    except:
        print("Tidak ada nama folder yang diberikan!")

    # Inisasi Data yang akan dipakai
    # Saat pertama kali pembacaan, program akan membaca save data pada folder 'main save'
    dfuser = csvtolist("user",6,folder)
    dfgame = csvtolist("game",6,folder)
    dfriwayat = csvtolist("riwayat",5,folder)
    dfkepemilikan = csvtolist("kepemilikan", 2,folder)

    while (program == True):
        print("========================================================================================")
        print("Ketik 'help' untuk melihat perintah yang dapat dilakukan.")
        action = input("Silahkan ketikkan perintah: ").lower()
        logged = False              # Variabel yang menjelaskan apakah pengguna sudah login atau belum
        role = 'guest'                # Jika belum melakukan login, role yang diberikan adalah 'guest'
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
                print("Saldo    :", dfuser[index][5])
                

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
                    print("Anda sedang menggunakan akun dengan username '"+dfuser[index][1]+"'.")         # username disimpan pada data kolom index 1
                    print("Silakan logout terlebih dahulu untuk melakukan login menggunakan akun lain.")

                # Jika action adalah logout
                elif (action == 'logout'):
                    result = logout(dfuser, index)      
                    if (result == True):            # Jika pengguna ingin keluar dari akunnya, maka variabel logged menjadi False
                        logged = False

                # Jika action adalah ubah stock game
                elif (action == 'ubah_stok'):
                    if (role == 'admin'):
                        ubah_stok(dfgame)
                    else:
                        print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")

                # Jika action adalah buy game
                elif (action == 'buy_game'):
                    if (role == 'admin'):
                        print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
                    else:
                        dfuser, dfkepemilikan, dfriwayat = buy_game(dfuser, dfgame, dfkepemilikan, dfriwayat, id, index)

                # Jika action adalah search_my_game
                elif (action == 'search_my_game'):
                    if (role == 'admin'):
                        print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
                    else:
                        search_my_game(dfgame , dfkepemilikan, id)
                
                # Jika action adalah search_game_at_store search_game_at_store(dfgame)
                elif (action == 'search_game_at_store'):
                    search_game_at_store(dfgame)
                
                # Jika action adalah topup
                elif (action == 'topup'):
                    if (role == 'admin'):
                        topup(dfuser)
                    else:
                        print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
                    
                # Jika action adalah riwayat
                elif (action == 'riwayat'):
                    if (role == 'admin'):
                        print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
                    else:
                        riwayat(id, dfriwayat)
                
                # Jika action adalah help
                elif (action == 'help'):
                    help(role)

                # Jika action adalah save:
                elif (action == 'save'):
                    save(dfuser, dfgame, dfriwayat, dfkepemilikan)

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

        # Jika action adalah help
        elif (action == 'help'):
            help(role)

        # Melakukan permainan kerang ajaib tanpa melakukan login
        elif (action == 'kerangajaib'):
                kerangajaib()
        # Melakukan permainan tictactoe tanpa melakukan login
        elif (action == 'tictactoe'):
                tictactoe()
        # Jika action adalah exit
        elif (action == 'exit'):
                program = False
        else :                              # pengguna tidak menginputkan 'login'
            print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login".')





