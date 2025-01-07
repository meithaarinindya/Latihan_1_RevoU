#operasi pada list
#manipulasi data list

print('\n','='*30)

#index  0      1     2   (depan)
#index -3     -2    -1   (belakang)
S = ['eden','sky','sage']
print(S)

print('-'*30)

#mengambil data dari list
A = S[0]
print(f"data pertama adalah = {A}")
B = S[-1]
print(f"data terakhir adalah = {B}")

print('-'*30)

#jumlah data pada list
C = len(A)
print('panjang data adalah =',C)

print('='*30)
print('MANIPULASI DATA LIST'.center(29))
print('-'*30)

#menambahkan item pada list
'''data.insert(index,item)'''

print(f'data sebelumnya = \n{S}')

S.insert(1,'pepper')
print(f'\ndata setelahnya adalah = \n{S}')

#menambah item pada akhir list
'''data.append('data baru')'''

S.append('ruby')
print(f'\ndata sesudah ditambahkan di akhir adalah = \n{S}')

#menggabungkan dua buah list
'''data.extend(lilstbaru)'''
S = ['eden','sky','sage']
R = ['mars','orion','puto']
S.extend(R)
print(f'\ndata gabungan adalah = \n{S}')

#mengubah item
'''data[index] = itembaru'''
S[2] = 'romeo'
print(f'\ndata yang diubah = \n{S}')

#menghapus item pada list
'''data.remove(itemremove)'''
S = ['eden','sky','sage']
S.remove('sage')
print(f'\ndata yang sudah di hapus adalah \n{S}')

#menghapus item di akhir
'''data.pop'''
S = S.pop()
print(f'data akhir adalah \n{S}')