# Loop (pengulangan)
'''
Pada pengulangan jika kondisi tidak sesuai
maka akan mengulang aksi yang ada di awal
contoh Un = a + 3 + 3 + ... + 3
'''
#contoh manual
print('\n','CONTOH MANUAL'.center(30,'-'))
a = 5
print('untuk a = ',a)
a = a + 3
print(a)
a = a + 3
print (a)

#Rumus Loop
'''
a = description      --> start
for i in a :         --> condition
    print ()         --> action (true)
print()              --> end
'''

#Looping dengan himpunan
print('\n','LOOPING MANUAL'.center(30,'-'))
A = [0, 1, 2, 3, 4]
print('A =',A)
for i in A :
    print(f"i sekarang -> {i}")
print('selesai')

#looping dengan range
print('\n','LOOPING RANGE'.center(30,'-'))
for i in range(5) :
    print(f"i sekarang -> {i}")
print('selesai')

#looping dengan range batas
print('\n','LOOPING RANGE BATAS'.center(30,'-'))
for i in range(5,9) :
    print(f"i sekarang -> {i}")
print('selesai')

#looping dengan string
print('\n','LOOPING DENGAN STRING'.center(30,'-'))
B = "a glimpse of the everyday"
for i in B :
    print(i)
print('selesai')
