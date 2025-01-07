#operasi dan manipulasi string part 2
#operator dalam bentuk method

# 1. mengubah case dari string
print('\n=====MENGUBAH CASE=====')

data = 'F\'iGhT fOr YoUr FaIrYtAlE'
print("data =",data)
print('uppercase =' + data.upper()) #ubah ke huruf besar
print('lowercase = ' + data.lower()) #ubah ke huruf kecil

# 2. mengecek isX method
print('\n=====METHOD isX======')

data = 'Silent laughter. Loud peace.'
print(data + " is lower = " + str(data.islower()))
data = data.lower()
print(data + " is lower = " + str(data.islower()))

'''
rumus isX
.islower() = semua karakter huruf kecil
.isupper() = semua karakter huruf besar
.isalpha() = semua karakter huruf
.isalnum() = semua karakter huruf & angka
.isdecimal() = semua karakter angka
.isspace() = string kosong dengan komposisi spasim tab, newline \n
.istitle() = semua karakter di awali huruf kapital
'''

print('\n=====EXAMPLE=====')
judul = "'It Is Okay Not To Be Okay'"
cek_judul = judul.istitle() #hasil bool
print(judul + " is title = " + str(cek_judul))

# 3. mengecek komponen startswith() dan endswith()
print('\n=====MENGECEK KOMPONEN=====')

#kata awal .startswish()
data = "'Rainy Days And Cozy Cliche'"
print(data)
cek_start = data.startswith('\'Rainy')
print("start 'Rainy = " + str(cek_start))
cek_start = data.startswith('rainy')
print("start rainy = " + str(cek_start))

#kata akhir .endswith ()
cek_end = data.endswith('Cliche\'')
print("end Cliche' = " + str(cek_end))
cek_end = data.endswith('clichE')
print('end clichE  = ' + str(cek_end))

print('\n')

# 4. menggabungkan komponen join() dan split()
data = ['daisy', 'iris','sakura','tulip']
print(data)

#menggabungkan .join()
print(','.join(data))

#memisahkan .split()
data = 'daisyppirisppsakurapptulip'
print(data.split('pp'))

# 5. alokasi karakter rjust(), ljust(), center()

data = 'moonlight magic moments'
print('\n'+data)
kanan = data.rjust(30)
print("'"+kanan+"'") #rata kanan spasi
tengah = data.center(30)
print("'"+tengah+"'") #rata tengah spasi
kiri = data.ljust(30)
print("'"+kiri+"'") #rata kiri spasi

data = 'whispers of wind'
print('\n'+data)
kanan = data.rjust(30,'-')
print(kanan) #rata kanan karakter
tengah = data.center(30,'=')
print(tengah) #rata tengah karakter
kiri = data.ljust(30,'*')
print(kiri) #rata kiri karakter

#menghilangkan karakter .strip
data = 'petals in storm'
print('\n',data)
tengah = data.center(30,'^')
print(tengah)
split = tengah.strip('^')
print(split)

