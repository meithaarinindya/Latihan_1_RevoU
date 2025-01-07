#pertemuan 11 = operasi logika atau boolean
'''
    operasi logika = NOT, OR, AND, XOR
    tabel kebenaran
'''
print("===TABEL KEBENARAN OPERASI LOGIKA===")

#operasi not
#operasi kebalikan
print("\n-----NOT-----")
a = True
b = not a
print("jika a =",a)
print("maka not a =",b)

#operasi OR
'''jika salah satu true, maka hasilnya true
asumsikan penjumlahan 0 dan 1'''
print("\n-----OR-----")
c = True
d = True
e = c or d
print(c," OR",d," =",e)
c = True
d = False
e = c or d
print(c," OR",d,"=",e)
c = False
d = True
e = c or d
print(c,"OR",d," =",e)
c = False
d = False
e = c or d
print(c,"OR",d,"=",e)

#operasi AND
'''jika salah satunya false, maka hasilnya false
asumsikan dengan perkalian 0 dan 1'''
print("\n-----AND-----")
f = True
g = True
h = f and g
print(f," AND",g," =",h)
f = True
g = False
h = f and g
print(f," AND",g,"=",h)
f = False
g = True
h = f and g
print(f,"AND",g," =",h)
f = False
g = False
h = f and g
print(f,"AND",g,"=",h)

#operasi XOR
print("\n-----XOR-----")
''''menggunakan lambang ^
jika salah satu true/false, maka hasilnya true
jika keduanya true/false, maka hasilnya false'''
i = True
j = True
k = i ^ j
print(i," XOR",j," =",k)
i = True
j = False
k = i ^ j
print(i," XOR",j,"=",k)
i = False
j = True
k = i ^ j
print(i,"XOR",j," =",k)
i = False
j = False
k = i ^ j
print(i,"XOR",j,"=",k)

