#Latihan Dictionary

#template dict mahasiswa

import datetime
import os
import string
import random

#p = mahasiswa_template
p = {
    'nama':'nama',
    'nim':'00000000',
    'sks':0,
    'lahir':datetime.datetime(1111,11,11)
}

#q = data_mahasiswa
q = {}

print(p)
print(q)

#r = mahasiswa

while True : #membuat berulang
    os.system('cls') #menghilangkan info

    #judul
    print(f"{'SELAMAT DATANG':^50}")
    print(f"{'DATA MAHASISWA':^50}")
    print('='*50)

    #input user
    r = dict.fromkeys(p.keys())

    r['nama']=input('Nama Mahasiswa: ')
    r['nim']=input('NIM Mahasiswa : ')
    r['sks']=int(input('SKS Lulus : '))
    YEAR = int(input("Tahun lahir (YYYY) : "))
    MONTH = int(input('Bulan Lahir (MM) : '))
    DAY = int(input('Tanggal Lahir (DD) : '))

    r['lahir']=datetime.datetime(YEAR, MONTH, DAY)

    print('\n')
    
    print(f"{'KEY':<6} {'NAMA':<17} {'NIM':<8} {'SKS':^10} {'LAHIR':^10}")
    print('-'*50)

    #menambahkan data

    KEY = ''.join(random.choice(string.ascii_uppercase) for i in range(6))
    q.update({'KEY':r})
    
    for r in q :
        KEY = r

        NAMA = q[KEY]['nama']
        NIM = q[KEY]['nim']
        SKS = q[KEY]['sks']
        LAHIR = q[KEY]['lahir'].strftime('%x')


    print(f"{KEY:<6} {NAMA:<17} {NIM:<8} {SKS:^10} {LAHIR:^10}")

    print('\n')
    s = input('Apakah sudah selesai (y/n)? ')
    if s == 'n' :
        break

print('\nAkhir dari program, Terima kasih')