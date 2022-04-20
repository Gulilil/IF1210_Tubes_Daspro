# File ini berisikan fungsi-fungsi yang digunakan untuk menjalankan program tic-tac-toe

# Subprogram Melakukan Output Papan Permainan TicTacToe
# procedure printboard (matrix board)
'''
Deskripsi :
Prosedur tersebut sebuah input yaitu 'board' yang bertipe matrix. Prosedur akan melakukan print untuk setiap 
baris pada board sehingga dapat dilihat oleh pemain.

Kamus :
    board : matrix of char
    i, j : int
'''
# Algoritma 
def printboard(board): #Untuk melakukan print papan tictactoe
    for i in range (3):
        for j in range(3):
            print(board[i][j],end='')
        print()


# Subprogram Melakukan Pengecekan Petak
# function checkxy(matrix board)
'''
Deskripsi :
Fungsi tersebut sebuah input yaitu 'board' yang bertipe matrix. Fungsi ini akan melakukan pengecekan
pada variabel 'board' yang berfungsi sebagai papan mengenai apakah suatu petak bersifat valid untuk diisi. 
Petak yang bersifat valid adalah petak kosong, dalam hal ini, maka petak tersebut diisi dengan "#".

Kamus :
    board : matrix of char
    iy, ix : int
'''
# Algoritma
def checkxy(x,y,board):
    iy = y-1            #iy adalah index y pada papan
    ix = x-1            #ix adalah index x pada papan
    if ( x < 0 or x > 3 or y < 0 or y > 3):
        print("Koordinat berada diluar papan.")
        return False
    if (board[2-iy][ix] != "#"):
        print("Petak tersebut telah diisi.")
        return False
    return True


# Subprogram Melakukan Pengecekan Pemenang
# function checkwin(matrix board)
'''
Deskripsi :
Fungsi tersebut sebuah input yaitu 'board' yang bertipe matrix. Fungsi ini akan melakukan pengecekan
pada variabel 'board' yang berfungsi sebagai papan untuk mengeluarkan output apakah sudah ada pemenang 
dalam permainan tersebut. Pengecekan pemenang akan dilakukan sesuai dengan aturan tic-tac-toe.

Kamus :
    board : matrix of char
    i, j : int
'''
# Algoritma
def checkwin(board):
    # Fungsi mengeluarkan return True jika permainan selesai (sudah ada pemenang)
    # Check horizontal:
    for i in range(3):
        if ( board[i][0] == "X" and board[i][1] == "X" and board[i][2] == "X"):
            print('Pemain "X" menang secara horizontal.')
            return True     
        if ( board[i][0] == "O" and board[i][1] == "O" and board[i][2] == "O"):
            print('Pemain "O" menang secara horizontal.')
            return True
    # Check vertical:
    for j in range(3):
        if ( board[0][j] == "X" and board[1][j] == "X" and board[2][j] == "X"):
            print('Pemain "X" menang secara vertikal.')
            return True     
        if ( board[0][j] == "O" and board[1][j] == "O" and board[2][j] == "O"):
            print('Pemain "O" menang secara vertikal.')
            return True
    #Check Diagonal:
    # Check Diagonal garis y = x
    if ( board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X"):
        print('Pemain "X" menang secara diagonal.')
        return True     
    elif (board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O"):
        print('Pemain "O" menang secara diagonal.')
        return True
    # Check Diagonal garis y = -x
    if ( board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X"):
        print('Pemain "X" menang secara diagonal.')
        return True     
    elif ( board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O"):
        print('Pemain "O" menang secara diagonal.')
        return True
    return False


# Subprogram Melakukan Pengecekan Berakhir Seri
# function checkdraw(matrix board)
'''
Deskripsi :
Fungsi tersebut sebuah input yaitu 'board' yang bertipe matrix. Fungsi ini akan melakukan pengecekan
pada variabel 'board' yang berfungsi sebagai papan mengenai apakah permainan telah berakhir dengan seri. 
Fungsi ini dilakukan setelah pengecekan pemenang. Bila belum ditemukan pemenang, maka ada 2 kemungkinan yaitu
permainan masih berlanjut atau permainan berakhir dengan seri.

Kamus :
    board : matrix of char
    hashcount : int
    i, j : int
'''
# Algoritma
def checkdraw(board):
    hashcount = 0                   # Menghitung banyaknya hashtag pada papan
    for i in range(3):
        for j in range(3):
            if (board[i][j] == "#"):
                hashcount +=1
    if (hashcount > 0):             # Bila masih ada papan kosong, permainan belum selesai
        return False
    elif (hashcount == 0):          # Bila sudah tidak ada papan kosong, permainan selesai
        print("Permainan selesai dengan berakhir seri.")
        return True


# Subprogram Melaksanakan Permainan Tic-Tac-Toe
# procedure tictactoe()
'''
Deskripsi :
Prosedur tictactoe memiliki fungsi untuk menjalankan permainan tictactoe. Prosedur ini menjadi komponen utama
dalam mengatur segala fungsi-fungsi lainnya yang menunjang pelaksanaan permainan tictactoe.

Kamus :
    game : bool
    round : int
    x, y : int
    board : matrix of char
'''
# Algoritma 
def tictactoe():
    print("========================================================================================")
    print("Legenda: ")
    print("# Kosong")
    print("X Pemain 1")
    print("O Pemain 2")
    game = True             # Variabel yang menandakan apakah game masih berlanjut
    round = 1               # Menyatakan banyaknya ronde pada permainan

    # Melakukan setup papan tictactoe
    board = [['#','#','#'],
             ['#','#','#'],
             ['#','#','#']]
    

    while (game == True):
        print("Ronde", round)
        print("Status Papan")
        printboard(board)

        # Check apakah permainan sudah mendapatkan pemenang
        if (checkwin(board) == True):
            game = False
        
        # Check apakah permainan berakhir seri
        if (checkdraw(board) == True):
            game = False

        if (game == True):                      # Dilakukan apabila game masih berlanjut
            if (round % 2 == 1):
                print("Giliran Pemain 'X'")
            else:                               # (round % 2 == 0):
                print("Giliran Pemain '0'")
            
            #Meminta input pada pemain
            x = int(input("X: "))
            y = int(input("Y: "))
            while (checkxy(x,y,board) == False):
                x = int(input("X: "))
                y = int(input("Y: "))
            # Memasukan input pada papan
            iy = y-1            #iy adalah index y pada papan
            ix = x-1            #ix adalah index x pada papan
            if (round % 2 == 1):
                board[2-iy][ix] = "X"
            else :
                board[2-iy][ix] = "O"

            round = round +1