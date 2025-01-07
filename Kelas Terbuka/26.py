#control flow
#pass, continue

#PASS
'''
berfungsi sebagai dummy
tidak akan dieksekusi
'''
print('\n','CONTROL FLOW : PASS'.center(30,'='))
print('-'*31)

a = 0
while a < 5 :
    a += 1
    if a == 3 :
        print("merkurius")
    print(a)


#continue
print('\n','CONTROL FLOW : CONTINUE'.center(30,'='))
print('-'*31,'1')
'''
dua buah cabang
tetapi akan kembali ke awal yang sama
membuat loop meloncat ke step selanjutnya
'''
#contoh 1
x = 0
print(f"angka awal = {x}")
while x < 5 :
    x += 1
    print(f"{x} =")
    print('peony')
print('selesai')

print(31*'-','2')

#contoh 2
x = 0
print(f"angka awal = {x}")
while x < 5 :
    x += 1
    print(f"{x} =")
    if x == 3 :
        print('*orchid')
    print('peony')
print('selesai')

print(31*'-','3')

#contoh 3
x = 0
print(f"angka awal = {x}")
while x < 5 :
    x += 1
    print(f"{x} =")             #--> action 1
    if x == 3 :
        print('*orchid')
        continue                #skip yang di bawah
    print('peony')              #--> action 2
print('selesai')