#date and time

import datetime as dt

#contoh
print('\n','CONTOH'.center(30,'-'))

hari_ini = dt.date.today()
print(hari_ini)

print(f"hari ini adalah hari = {hari_ini:%A}")
tanggal = dt.date(1999,5,24)
print(tanggal,f"adalah hari hari {tanggal:%A}")

#program 1
print('\n','PROGRAM DATE AND TIME'.center(30,'-'))

print('Silahkan masukkan tanggal, bulan dan tahun anda') #input user
q1 = int(input('Tanggal\t: '))
q2 = int(input('Bulan\t: '))
q3 = int(input('Tahun\t: '))
c = dt.date(q3,q2,q1)
print(f"Tanggal lahir anda adalah :{c}") #tanggal lahir
d = dt.date.today()
e = d - c
print(f"Umur hari anda adalah {e}")
f = e.days // 365
print(f"Umur tahun anda adalah {f} tahun")
g = (e.days % 365) // 30
print(f"Umur tahun dan bulan anda adalah {f} tahun {g} bulan")