#operasi dan manipulasi stribg part 1

# 1. menyambung string (concatenate)
nama_pertama = 'kim'
nama_kedua = 'ming'
nama_akhir = 'yu'
nama_lengkap = nama_pertama + ' ' + nama_kedua + nama_akhir
print(nama_lengkap)

# 2. menghitung panjang string (length)
data = len('seungcheol, jeonghan, joshua')
print('jumlah karakter =',data)

# 3. operator untuk string

#mengecek apakah ada komponen char atau string pada string
nama = 'seungcheol, jeonghan, joshua'
j = "j"
status = j in nama
print('huruf ' + j + ' pada string ' + nama + ' = ' + str(status))
print('komponen mingyu pada ' + nama + ' = ' + str('mingyu' in nama))

#mengulang string
print("vernon "*13)
print(13*'dino ')

#indexing (mengambil data dari string)
print("index(karakter) ke-26 adalah " + nama[27]) #(+) dari depan
print('index(karakter) ke-0 adalah ' + nama[0]) #(0) paling depan
print('index(karakter) ke-0 adalah ' + nama[-3]) #(-) dari belakang
print('index ke 12 sampai 20 adalah ' + nama[12:20]) #12 sampai 19
print('index terjeda adalah ' + nama[0:12:2])

#item paling kecil
print("item terkecil adalah " + min(nama))
print("item terbesar adalah " + max(nama))

#ascii code
ascii_code = ord(' ')
print('ascii code untuk spasi adalah ' + str(ascii_code))
ascii_code = ord('.')
print('ascii_code untuk titik adalah ' + str(ascii_code))
print('ascii code untuk huruf j adalah ' + str(ord('j')))

# 4. operator dalam bentuk method

data = 'seungcheol jeonghan joshua'
jumlah = data.count('e')
print("jumlah huruf e pada " + data + " adalah " + str(jumlah))
