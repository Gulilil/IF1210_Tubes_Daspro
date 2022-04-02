

def csvtolist (file,component):
    # Component adalah lebar data csv
    # user.csv --> 6, game.csv --> 6, riwayat.csv --> 5, kepemilikan.csv --> 2
    # Membuka file csv 
    if (file == 'user'):
        data = open("user.csv", "r")
    elif (file == 'game'):
        data = open("game.csv", "r")
    elif (file == 'riwayat'):
        data = open("riwayat.csv","r")
    elif (file == 'kepemilikan'):
        data = open("kepemilikan.csv", "r")
    
    # Mengukur panjang list
    length = 0
    for i in data:
        length +=1

    # Membuat datalist kosong
    datalist = [[ 0 for i in range (component)] for i in range(length)]
    data.close()

    # Membuka kembali file csv 
    if (file == 'user'):
        data = open("user.csv", "r")
    elif (file == 'game'):
        data = open("game.csv", "r")
    elif (file == 'riwayat'):
        data = open("riwayat.csv","r")
    elif (file == 'kepemilikan'):
        data = open("kepemilikan.csv", "r")
    
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
    length = 0
    for i in list1:
        length +=1
    return length
