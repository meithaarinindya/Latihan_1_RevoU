# While Loop

#while loop adalah looping bersyarat
'''
a = description        --> start
while condition :      --> condition
    kondisi bersyarat
    print()            --> action (true)
print()                --> end
'''

#contoh 1
print('\n','LOOP CONTOH 1'.center(30,'='))
a = 0
while a < 5 :
    a += 1
    print("benar")
print('selesai')

#contoh 2
print('\n','LOOP CONTOH 2'.center(30,'='))
a = 0
while a < 5 :
    a += 1
    print(f"angka sekarang -> {a}")
    print("main character energy")
print('selesai')