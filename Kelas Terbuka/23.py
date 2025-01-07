#Aplikasi IF, ELSE & ELIF statement

#Kalkulator sederhana
'''
1. ambil data user (angka_pertama, operator, angka_kedua)
2. cabangnya
3. hasil & tampilnya
'''

print('\n','KALKULATOR SEDERHANA'.center(30,'='))
print(31*'-','\n')

angka_1 = float(input('masukan angka pertama = '))
operator = input('operator (+, -, x, :) = ')
angka_2 = float(input('masukan angka kedua = '))

#percabangan

if operator == "+" :
    a = angka_1 + angka_2
    print (f"hasilnya adalah {a}")
elif operator == "-" :
    b = angka_1 - angka_2
    print (f"hasilnya adalah {b}")
elif operator == "x" :
    c = angka_1 * angka_2
    print (f"hasilnya adalah {c}")
elif operator == ":" :
    d = angka_1 / angka_2
    print (f"hasilnya adalah {d}")
else :
    print('operasi yang anda masukan salah')