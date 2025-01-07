#MULTI KEYS & NESTING DICTIONARY

print('\nMULTI KEYS & NESTING DICTIONARY\n')

import datetime

mahasiswa1 = {
    'nama':'Zhong Chenle', #string
    'nim':'24250001', #string
    'sks':130, #numbers
    'beasiswa':False, #boolean
    'lahir':datetime.datetime(2001,11,22) #date
}

mahasiswa2 = {
    'nama':'Park Jisung',
    'nim':'24250002',
    'sks':100, 
    'beasiswa':True, 
    'lahir':datetime.datetime(2002,2,5)
}

mahasiswa3 = {
    'nama':'Na Jaemin',
    'nim':'24250003',
    'sks':130,
    'beasiswa':False,
    'lahir':datetime.datetime(2000,7,13)
}

dream = {
    'p':mahasiswa1,
    'q':mahasiswa2,
    'r':mahasiswa3
}

print(f'{mahasiswa1}\n{mahasiswa2}\n{mahasiswa3}\n\ndream = {dream}\n\n')
print('-'*50)


print(f'{'KEY':<6} {'Nama':<17} {'SKS':<5} {'Beasiswa': <9} {'Lahir':<10}')
print('-'*50)
for i in dream :
    KEY = i

    NAMA = dream[KEY]['nama'] 
    NIM = dream[KEY]['nim']
    SKS = dream[KEY]['sks']
    BEASISWA = dream[KEY]['beasiswa']
    LAHIR = dream[KEY]['lahir'].strftime("%x")
    print(f'{KEY:<6} {NAMA:<17} {SKS:<5} {BEASISWA:^9} {LAHIR:<10}')