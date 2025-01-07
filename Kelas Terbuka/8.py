#pertemuan 8 = operasi aritmetika

a = 10
b = 3

print("=====OPERASI HITUNG ARITMETIKA=====")

#operasi penjumlahan
hasil = a + b
print(a,"+",b,"=",hasil)

#operasi pengurangan
hasil = a - b
print(a,"-",b,"=",hasil)

#operasi perkalian
hasil = a * b
print(a,"x",b,"=",hasil)

#operasi pembagian
hasil = a / b
print(a,":",b,"=",hasil)

#operasi perpangkatan (eksponen)
hasil = a ** b
print(a,"pangkat",b,"=",hasil)

#operasi modulus (sisa pembagian)
hasil = a % b
print(a,"mod",b,"=",hasil)

#operasi floor division (pembulatan ke bawah)
hasil = a // b
print(a,"floor div",b,"=",hasil)

#priority of operation
x = 3
y = 2
z = 4
hasil = x + y * z
print(x,"+",y,"x",z,"=",hasil)
'''
    1. tanda kurung
    2. eksponen/perpangkatan **
    3. perkalian (*), pembagian (/), mod (%), floor div (//)
    4. penjumlahan (+), pengurangan (-)
'''
hasil = x ** y * z + x / y - y % z // x
print(x,"**",y,"*",z,"+",x,"/",y,"-",y,"%",z,"//",x,"=", hasil)