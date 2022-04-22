
# Subprogram Pengubahan Data File CSV menjadi List Matrix
# function csvtolist (string file, int component, string folder)
'''
Deskripsi :
Fungsi tersebut memiliki 3 buah input, 'file' bertipe string merupakan penentu sebagai indikasi file csv apa yang ingin diubah. 
Lalu 'component' bertipe integer yang merupakan lebar data list yang ingin dibentuk dari data csv. Terakhir, 'folder' bertipe 
string sebagai penunjuk jalan akan folder mana yang ingin dibuka.

Kamus :
    file, folder : string
    line : string
    word : string
    data : file of string
    datalist : matrix of string
    row, col, sum, index : int
    component, length : int
'''
# Algoritma 
def csvtolist (file,component, folder):
    # Component adalah lebar data csv
    # user.csv --> 6, game.csv --> 6, riwayat.csv --> 5, kepemilikan.csv --> 2
    # Membuka file csv 
    if (file == 'user'):
        data = open("./csv files/"+folder+"/user.csv", "r")
    elif (file == 'game'):
        data = open("./csv files/"+folder+"/game.csv", "r")
    elif (file == 'riwayat'):
        data = open("./csv files/"+folder+"/riwayat.csv","r")
    elif (file == 'kepemilikan'):
        data = open("./csv files/"+folder+"/kepemilikan.csv", "r")
    
    # Mengukur panjang list
    length = 0
    for i in data:
        length +=1

    # Membuat datalist kosong
    datalist = [[ 0 for i in range (component)] for i in range(length)]
    data.close()

    # Membuka kembali file csv 
    if (file == 'user'):
        data = open("./csv files/"+folder+"/user.csv", "r")
    elif (file == 'game'):
        data = open("./csv files/"+folder+"/game.csv", "r")
    elif (file == 'riwayat'):
        data = open("./csv files/"+folder+"/riwayat.csv","r")
    elif (file == 'kepemilikan'):
        data = open("./csv files/"+folder+"/kepemilikan.csv", "r")
    
    row = 0                                         # variabel untuk menghitung baris tertentu pada loop
    for line in data:
        col = 0                                     # variabel untuk menghitung kolom tertentu pada loop
        word = ""                                       # variabel word digunakan untuk menampung kata per kata
        # Mengukur panjang satu baris
        sum = 0
        for i in line:
            sum +=1

        for index in range(sum):                    # Pengulangan setiap huruf dalam suatu line
            if (line[index] == ";"):                    # jika suku tertentu tersebut adalah ";", maka digunakan sebagai pemisah
                datalist[row][col] = word           # maka kumpulan huruf word dimasukan kedalam list
                word =""                                # variabel word di-reset ulang menjadi kosong
                col +=1                             # nilai kolom bertambah 1 untuk memasukan variabel word ke kolom berikutnya
            else:
                word = word + line[index]           # selama suku tertentu bukan ";", maka variabel char akan terus digabung dengan word
            if (index == sum - 2):                      # jika index sudah mencapai suku terakhir pada baris
                datalist[row][col] = word           # otomatis variabel word yang telah terbentuk akan dimasukkan ke dalam list
            

        row +=1                                     # nilai baris bertambah 1 seiring bergantinya variabel line

    data.close
    return datalist


# Subprogram Melakukan Output Sebuah List atau Matriks 
# procedure printlist(array datalist)
'''
Deskripsi :
Prosedur tersebut memiliki sebuah input, 'datalist', yang bertipe array. Fungsi ini akan melakukan print atau mengeluarkan 
output untuk setiap data yang terletak pada array tersebut secara berurutan.

Kamus :
    datalist : array 
'''
# Algoritma 
def printlist(datalist):
    for i in datalist:
        print(i)


# Subprogram menggabungkan dua buah list
# function mergelist(array list1, array list2)
'''
Deskripsi :
Fungsi tersebut memiliki 2 buah input, 'list1' dan 'list2', yang keduanya bertipe array. Fungsi ini digunakan untuk menggabungkan
kedua fungsi tersebut sehingga menjadi suatu fungsi yang baru. Fungsi baru yang dihasilkan akan memiliki data dari 'list1' terlebih 
dahulu kemudian ditambah dengan data dari 'list2'

Kamus :
    listinlist : array 
    mergedlist : array
'''
# Algoritma 
def mergelist(list1,list2):
    # Asumsikan list1 adalah list yang panjang dan list 2 merupakan list 1 baris
    # Asumsikan lebar list1 dan list2 sama
    listinlist = [list2]
    mergedlist = list1 + listinlist
    return mergedlist


# Subprogram Mengukur panjang sebuah List 
# function lengthlist(array datalist)
'''
Deskripsi :
Fungsi tersebut memiliki sebuah input, 'list1', yang bertipe array. Fungsi ini akan melakukan perhitungan
untuk setiap data yang ada pada array tersebut. Untuk setiap data yang ada pada array, nilai variabel penghitung
akan bertambah sebanyak 1.

Kamus :
    list1 : array or string 
    length : int
'''
# Algoritma 
def lengthlist(list1):
    # Fungsi mengembalikan suatu variabel integer "length" yang merupakan panjang dari suatu list
    length = 0
    for i in list1:
        length +=1
    return length

# Subprogram Mengurutkan List 
# function sortlist(array list1)
'''
Deskripsi :
Prosedur tersebut memiliki sebuah input, 'list1', yang bertipe array. Fungsi ini akan melakukan pengurutan dengan urutan membesar.

Kamus 
    list1 : array 
    temp : int or string
'''
# Algoritma 
def sortlist(list1):
    # Prosedur untuk mengurutkan suatu list
    for i in range(lengthlist(list1) -1):
        for j in range(lengthlist(list1) -i -1):
            if list1[j] > list1[j+1] :          
                temp = list1[j]                         # temp adalah variabel temporary untuk menyimpan data sementara
                list1[j] = list1[j+1]
                list1[j+1] = temp

# Subprogram Pengubahan List Matrix menjadi Data CSV
# procedure sortlist(string file, string folder, array dataframe)
'''
Deskripsi :
Prosedur tersebut memiliki 3 buah input, 'file' bertipe string yang mengindikasikan jenis file yang ingin dimasukkan menjadi csv.
Lalu, 'folder' bertipe string yang merupakan penunjuk jalan sebagai tempat penyimpanan data. Terakhir, 'dataframe' yang bertipe matrix
of string berupa data yang ingin disimpan dalam suatu csv.

Kamus 
    data : file of string
    length, component : int
    row, col : int
    line : string
'''
# Algoritma 
def listtocsv(file, folder, dataframe):
    # Melakukan seleksi ke file csv mana save akan dilakukan
    # Fungsi ini juga dapat digunakan untuk membuat file baru, sehingga tidak perlu
    # dilakukan pembuatan fungsi sendiri untuk pembuatan file.csv baru
    if (file == 'user'):    
        data = open("./csv files/"+folder+"/user.csv", "w")
    elif (file == 'game'):
        data = open("./csv files/"+folder+"/game.csv", "w")
    elif (file == 'riwayat'):
        data = open("./csv files/"+folder+"/riwayat.csv","w")
    elif (file == 'kepemilikan'):
        data = open("./csv files/"+folder+"/kepemilikan.csv", "w")

    # Mengukur panjang list dari dataframe
    length = lengthlist(dataframe)

    # Mengukur lebar list dari dataframe
    component = lengthlist (dataframe[0])

    # Setiap row dari data frame akan dibuat menjadi suatu line bertipe string yang dipisahkan oleh ";"
    for row in range(length):
        line = ""                                       # Inisiasi variabel line sebagai string kosong
        for col in range(component):
            if (col == component - 1):                        # Pengecualian bila sudah berada pada suku terakhir
                line = line + dataframe[row][col] + "\n"             # line akan ditambah dengan suku terakhir ditambah argumen new line
            else:                                             # Untuk suku yang bukan suku terakhir
                line = line + dataframe[row][col]+";"                # line akan ditambah dengan suku tertentu ditambah char ";"
        
        # Masukkan setiap line kedalam csv
        data.write(line)   
    
    data.close()

# Subprogram Mengurutkan Data pada matrix berdasarkan suatu parameter
# function sortmatrix(matrix matrix, int comparedColumn)
# function sortmatrixint(matrix matrix, int comparedColumn)
'''
Deskripsi :
Fungsi tersebut memiliki dua buah paramater yaitu 'matrix' yang bertipe matrix dan 'comparedColumn' yang bertipe integer.
Fungsi akan dilakukan untuk mengurutkan matrix tersebut berdasarkan data pada kolom 'comparedColumn' secara mengurut membesar.
Perbedaan antara sortmatrix dan sortmatrixint adalah matrix digunakan untuk string dan sortmatrixint digunakan untuk int

Kamus :
    matrix : matrix of string
    row: int
    comparedColumn : int
'''
# Algoritma
def sortmatrix (matrix, comparedColumn):
    # Mengukur panjang dan lebar matrix
    row = lengthlist(matrix)

    for i in range(1,row-1):                  # Pengurutan dimulai dari index 1 karena index 0 adalah judul dari data
        indexMin = i                          # Pengulangan cukup dilakukan hingga row-1, karena index terakhir pasti sudah terurut setelah dilakukannya pengurutan
        for j in range(i, row):
            if (matrix[j][comparedColumn] < matrix[indexMin][comparedColumn]):
                indexMin = j
        temp = matrix[indexMin]
        matrix[indexMin] = matrix[i]
        matrix[i] = temp
    
    return matrix

def sortmatrixint(matrix, comparedColumn):
    # Mengukur panjang dan lebar matrix
    row = lengthlist(matrix)

    for i in range(1,row-1):                  # Pengurutan dimulai dari index 1 karena index 0 adalah judul dari data
        indexMin = i                          # Pengulangan cukup dilakukan hingga row-1, karena index terakhir pasti sudah terurut setelah dilakukannya pengurutan
        for j in range(i, row):
            if (int(matrix[j][comparedColumn]) < int(matrix[indexMin][comparedColumn])):
                indexMin = j
        temp = matrix[indexMin]
        matrix[indexMin] = matrix[i]
        matrix[i] = temp
    
    return matrix
            
            
    