#operator dictionary

print('\n','-'*50,'1','\n')

a = {
    'ss' : 'strawberry shortcake',
    'rs' : 'raspberry sorbet',
    'tb' : 'tea blossom',
    'bm' : 'blueberry muffin',
    'ac' : 'angle cake',
    'gs' : 'ginger snap'
}

#data dict
print(a)

#panjang dict
print(len(a))

#search item
print(a['ss'])
print(a.get('ss'))
print(a.get('pp','key tidak ditemukan')) #key dengan message

#detect item/ check words
check = 'ss' in a
print(check)

 #mengubah data
a['ac'] = 'apple crispy'
print(a)

#menambah data -> di belakang karena tidak ada index
a['hb'] = 'huckle berry'
print(a)

#mengembalikan ke semula
a.update({'ac':'angle cake'}) #data kembali ke semula
print(a)
a.update({'ft':'frosty'}) #jika data belum ada, maka akan ditambhakan
print(a)

#menghapus data
del a['ft']
print(a)

print('\n','-'*50,'2','\n')

