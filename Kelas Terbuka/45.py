'''FUNGSI DENGAN ARGUMEN'''

'''
def nama_fungsi(argument) :
    badan fungsi
'''

def a(nama) :
    #fungsi hello world menerima dengan variabel nama
    print(f'Selamat datang {nama}')


a('Joshua')

print('-'*50,'1\n')

#program tambah

def b(x,y) :
    hasil = x + y
    print(f'{x} + {y} = {hasil}')

b(3,5)

print('-'*50,'2\n')

def c(dream) :
    dream = dream.copy()
    for i in member :
        print(f'Yang terhormat {i}')

member = ['jaemin','jeno','jisung','mark','haechan','chenle','renjun']

c(member)