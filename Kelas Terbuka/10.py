#pertemuan 10 = operasi komparasi
'''
    merupakan operasi perbandingan
    setia hasilnya adahal tipe boolean
    >, <. >=, <=, ==, !=, is, is not
    is/is not digunakan untuk mebandingkan objek
'''

a = 1
b = 3
c = 5
d = 5
print("a = ",a,"b = ",b,"c = ",c)

#lebih dari (>)
print("===LEBIH DARI===")
hasil = a>3
print(a,">",3,"=",hasil)
hasil = b>3
print(b,">",3,"=",hasil)
hasil = c>3
print(c,">",3,"=",hasil)

#kurang dari (<)
print("===KURANG DARI===")
hasil = a<3
print(a,"<",3,"=",hasil)
hasil = b<3
print(b,"<",3,"=",hasil)
hasil = c<3
print(c,"<",3,"=",hasil)

#lebih dari sama dengan(>=)
print("===LEBIH DARI SAMA DENGAN===")
hasil = a >= 3
print(a,">=",3,"=",hasil)
hasil = b >= 3
print(b,">=",3,"=",hasil)
hasil = c >= 3
print(c,">=",3,"=",hasil)

#kurang dari sama dengan (<=)
print("===KURANG DARI SAMA DENGAN===")
hasil = a <= 3
print(a,"<=",3,"=",hasil)
hasil = b <= 3
print(b,"<=",3,"=",hasil)
hasil = c <= 3
print(c,"<=",3,"=",hasil)

#sama dengan ==
print("===SAMA DENGAN===")
hasil = a == 3
print(a,"==",3,"=",hasil)
hasil = b == 3
print(b,"==",3,"=",hasil)
hasil = c == 3
print(c,"==",3,"=",hasil)

#tidak sama dengan !=
print("===TIDAK SAMA DENGAN===")
hasil = a != 3
print(a,"!=",3,"=",hasil)
hasil = b != 3
print(b,"!=",3,"=",hasil)
hasil = c != 3
print(c,"!=",3,"=",hasil)

#is sebagai komparasi objek yang sama
print("===IS===")
hasil = a is b
print(a,"is",b,"=",hasil)
hasil = c is d
print(c,"is",d,"=",hasil)
print("nilai c = ",c,", id = ",hex(id(c)))
print("nilai d = ",d,", id = ",hex(id(d)))
#id sama karena nilainya sama

#is not sebagai komparasi objek yang tidak sama
print("===IS NOT===")
hasil = b is not c
print(b,"is not",c,"=",hasil)
hasil = c is not d
print(c,"is not",d,"=",hasil)
