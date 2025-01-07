'''EXERCISE : FUNCTION'''

import os

#program untuk menghitung luas dan keliling persegi panjang

'''
#header program
os.system('cls')
print(f"{'PROGRAM MENGHITUNG LUAS':^50}")
print(f"{'DAN KELILING PEREGI PANJANG':^50}")
print(f"{'-'*50}{'\n'}")

#input user
PANJANG = int(input('Masukan nilai panjang : '))
LEBAR = int(input('Masukan nilai lebar : '))

#program menghitung luas
LUAS = PANJANG*LEBAR
KELILING = 2*(PANJANG+LEBAR)

#tampilan hasil
print(f"Hasil perhitungan luas = {LUAS}")
print(f"Hasil perhitungan keliling = {KELILING}")
'''


def header () :
    os.system('cls')
    print(f"{'PROGRAM MENGHITUNG LUAS':^50}")
    print(f"{'DAN KELILING PEREGI PANJANG':^50}")
    print(f"{'-'*50}{'\n'}")

def input_user() :
    p = int(input('Masukan nilai panjang : '))
    l = int(input('Masukan nilai lebar : '))
    return p,l

def luas(p,l) :
    return p*l

def keliling(p,l) :
    return 2*(p + l)

def display(message,value) :
    print(f'Hasil perhitungan {massage} = {value}')

while True :
    header()
    PANJANG,LEBAR = input_user()
    LUAS = luas(PANJANG,LEBAR)
    KELILING = keliling(PANJANG,LEBAR)

   display('luas',LUAS)
   display('keliling',KELILING)

    isContinue = input('Apakah lanjut (y/n)? ')
    if isContinue == 'n' :
        break

print('Program selesai, terima kasih')