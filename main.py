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
from subprograms import *


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

    while (program == True):
        print("========================================================================================")
        print("Tindakan yang bisa dilakukan tanpa login: 'login', 'kerangajaib', 'tictactoe', dan 'exit'")
        action = input("Silahkan ketikkan perintah: ").lower()
        logged = False              # Variabel yang menjelaskan apakah pengguna sudah login atau belum
        if (action == 'login'):
            # Inisasi Data yang akan dipakai
            # Saat pertama kali pembacaan, program akan membaca save data pada folder 'main save'
            dfuser = csvtolist("user",6,folder)
            dfgame = csvtolist("game",6,folder)
            dfriwayat = csvtolist("riwayat",5,folder)
            dfkepemilikan = csvtolist("kepemilikan", 2,folder)

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




