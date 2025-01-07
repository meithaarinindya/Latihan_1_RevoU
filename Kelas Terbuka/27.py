#control flow
#break

print(31*'-','1')

#contoh 1
a = 0
while a < 5 :
    a += 1
    print(f"angka sekarang = {a}")
    if a == 3 :
        print('buttercups')
        break #akan berhenti jika bertemu a = 3
    print('sunflower')
print('selesai')

print(31*'-','2')

#contoh 2
i = int(input('menghitung angka sampai = '))
a = 0

while True :
    a += 1
    print(f"count = {a}")
    if a == i :
        print("tulip")
        break
    print("daisy")
print('selesai')

print(31*'-')

#contoh 3

