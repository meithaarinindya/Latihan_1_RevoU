#Operasi List

print('\n','OPERASI LIST'.center(30,'='))

print('\n','-'*50,'\n')

#menghitung banyak data
'''.count'''

A = [1,5,1,4,3,2,4,3,2,3,7,8,9,0]
print(A)

a = A.count(4)
print(f'Jumlah angka 4 adalah {a}')
a = A.count(3)
print(f'jumlah angka 3 adalah {a}')

print('\n','-'*50,'\n')

#mengambil posisi data
'''.index'''

B = ['plum','latte','blue','rose']
print(B)

b = B.index('blue')
print(f'index blue adalah {b}')
b = ~(B.index('rose'))
print(f'~index rose adalah {b}')

print('\n','-'*50,'\n')

#mengurutkan data
'''.sort'''

A = [1,5,1,4,3,2,4,3,2,3,7,8,9,0]
print(A)
A.sort()
print(A)

print('\n')

B = ['plum','latte','blue','rose']
print(B)
B.sort()
print(B)

print('\n','-'*50,'\n')

#membalik urutan data
'''.reverse'''

B.reverse()
print(B)

print('\n','-'*50,'\n')