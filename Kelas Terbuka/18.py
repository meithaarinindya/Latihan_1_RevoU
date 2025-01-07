#format string

#contoh str
print('\n','CONTOH'.center(30,'='))
nama = 'vernon'
rumus = "hello " + nama + "!"
print(rumus)

print("\n","FORMAT".center(30,"="))

#format str
format = f"hello {nama}!"
print(format)

#format bool
data = True
format = f"data boolean = {data}"
print(format)

#format int
tahun = 1999
format = f"tahun = {tahun:d}"
print(format)

#format bilangan ordo ribuan
harga = 5000000
format = f"harga = {harga:,}"
print(format)

#format pembulatan bilangan desimal
panjang = 1234.8789
format = f"ukuran {panjang:.2f}" #dibulatkan 2 bilangan
print(format)
panjang = 12.345678
format = f"ukuran {panjang:10.2f}"
print(format) #hasil 10 bil desimal dengan spasi
panjang = 12.345678
format = f"ukuran {panjang:010.2f}"
print(format) #hasil 10 bil desimal dengan anngka 0

#format tanda + dan -
a = 21
b = -25
format_a = f"bilangan positif = {a:+d}"
format_b = f"bilangan negatif = {b:+d}"
print(format_a, format_b)

#format bilangan persen
a = 0.098
format = f"persentase = {a:.2%}"
print(format)

print("\n","OPERASI ARITMETIKA".center(30,'='))

#operasi aritmetika di dalam placeholder
harga = 10000
jumlah = 5
format = f"harga total = Rp{harga*jumlah:,},-"
print(format)

print("\n","FORMAT ANGKA LAIN".center(30,'='))

#binary, octal, hexadecimmal
angka = 1998
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hexal = f"hexal = {hex(angka)}"
print(format_binary)
print(format_octal)
print(format_hexal)