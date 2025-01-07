#Exercise for Looping
#Making a triangle

print('\n','TRIANGLE'.center(30))

print('-'*31,'1')

#rumus for
t = 6 #
a = 1 #dummy variable
for i in range(6) :
    print('*'*a)
    a += 1

print('-'*31,'2')

#rumus while
t = 10
a = 1 #dummy variable
while True :
    print('*'*a)
    a += 1
    if a > t :
        break

print('-'*31,'3')

#hanya ganjil saja
#menggunakan modulus 2
t = 8
a = 1
while True :
    if a % 2 :          #print jika ganjil
        print('*'*a)
        a += 1
    else :              #kembali jika genap
        a += 1
        continue
    if a > t :          #selesai jika melebihi sisi
        break       

print('-'*31,'4')

t = 12
a = 1
spasi = int(t//2)
while True :
    if a % 2 :          #print jika ganjil
        print(' '*spasi+'+'*a)
        spasi -= 1
        a += 1
    else :              #kembali jika genap
        a += 1
        continue
    if a > t :          #selesai jika melebihi sisi
        break      

print('-'*31,'EXERCISE')
#belah ketupat

t = 15
a = 1           #start for +
b = int(t/2)    #start for space
while True :
    if a % 2 :                   # condition : a ganjil
        print(' '*b + '+'*a)
        a += 1                   # true : ke bawah semakin bertambah
        b -= 1                   # true : ke bawah semakin berkurang
    else :
        a += 1                  # false, tambah 1 dulu baru di loop
        continue
    if a > 15 :
        break                    # akhir
a = 13            #start for +
b = 1             #start for space
while True :
    if a % 2 :                  # condition : a ganjil
        print(' '*b + '+'*a)
        a -= 1                  # true : ke bawah semakin berkurang
        b += 1                  # true : ke bawah semakin bertambah
    else :
        a -= 1                  # false, kurang 1 dulu baru di loop
        continue
    if b > 7 :                  # akhir
        break
