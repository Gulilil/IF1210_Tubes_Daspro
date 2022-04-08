

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

def printlist(datalist):
    for i in datalist:
        print(i)

def mergelist(list1,list2):
    # Asumsikan list1 adalah list yang panjang dan list 2 merupakan list 1 baris
    # Asumsikan lebar list1 dan list2 sama
    listinlist = [list2]
    mergedlist = list1 + listinlist
    return mergedlist

def lengthlist(list1):
    # Fungsi mengembalikan suatu variabel integer "length" yang merupakan panjang dari suatu list
    length = 0
    for i in list1:
        length +=1
    return length

def sortlist(list1):
    # Prosedur untuk mengurutkan suatu list
    for i in range(lengthlist(list1) -1):
        for j in range(lengthlist(list1) -i -1):
            if list1[j] > list1[j+1] :          
                temp = list1[j]                         # temp adalah variabel temporary untuk menyimpan data sementara
                list1[j] = list1[j+1]
                list1[j+1] = temp

def listtocsv(file, component, folder, dataframe):
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
    
