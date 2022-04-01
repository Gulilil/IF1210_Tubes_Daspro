# Digunakan untuk mengetest command-command sebelum dimasukan kedalam file utama

import time

'''     # Random Number untuk Kerang Ajaib
n = int(input("Panjang list:"))

local = time.localtime()
current = time.strftime("%S", local)
print(current)

hasil = int(current) % n
print(hasil)
'''

# Padanan Standar ASCII
'''
print(ord('p')) # --> dari char -> ke angka
 
print(chr(112)) # --> dari angka --> char
'''

alphabet = "abcdefghijklmnopqrstuvwxyz"

password = "kendebest"
newpass = ""

for i in (password):
    if (i in alphabet or i in alphabet.upper()):
        code = ord(i)
        penambah = 29
        pengali = 4
        newcode = (code + 29)*4 
        codediv = newcode // 26
        codemod = newcode % 26
        newcodemod = codemod + 97
        newalp = chr(newcodemod)
        #print(newcode, codediv, codemod, newcodemod, newalp)
        newpass = newpass + str(codediv)+ newalp
    else:
        newpass = newpass + i

print(" ======================================= ")
# Fungsi penyimpanan --> y = chipered(x) = (ord(x) + kodepenambah) * kodepengali 
# Fungsi pembalik --> x = semula(y) = chr((y / kodepengali) - kodepenambah)
# String pemisah --> 907

print(newpass)
#newpass = 21s19k22e22e22u21o22a19w

length = 0
for i in (newpass):
        length = length+1 

print(length)

finalcode = ""



i = 0
while (i < length):
    try:
        angka = int(newpass[i]+newpass[i+1])
        require1 = True
    except:
        angka = 0
        require1 = False
    
    if (require1 == True):
        if (i+2 < length and (newpass[i+2] in alphabet)):      #kalo alphabet, pasti huruf kecil
            code = newpass[i+2]
            require2 = True
        else:
            require1 = False
            require2 = False
        
    
    if(require1 == True and require2 == True):
        resultcode = (26*angka + ord(code) - 97 - 116)/4
        resultcode = chr(int(resultcode))
        i = i+3
    
    if(require1 == False):
        resultcode = newpass[i]
        i = i+1
    
    finalcode = finalcode + resultcode

print(finalcode)