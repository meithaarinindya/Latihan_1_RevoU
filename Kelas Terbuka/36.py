#aplikasi list
#database sederhana : daftar buku, penulis, judul

print('\n',f'PROGRAM DAFTAR BUKU'.center(50,'='),'\n','-'*50)

d = [] #koleksi buku yang sudah di data

while True :  #data akan terus berputar
    print('Masukkan data buku')
    a = input('  Masukan judul buku\t= ')
    b = input('  Masukan nama penulis\t= ')
    
    c = [a,b] 
    d.append(c) #menambahkan koleksi yang baru diinput
    print(d,'\n')

    print('No. Judul, Penulis')
    for index,i in enumerate(d) :
        print(f'{index}.  {i[0]}, {i[1]}')
    print('\n','-'*50,'\n')
    
    e = input("Apakah ingin melanjutkan? (y/n) = ")
    if e == "n" :
        break

print('Program Selesai')

print('\n','-'*50,'\n')