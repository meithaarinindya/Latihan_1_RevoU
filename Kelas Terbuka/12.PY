#pertemuan 12 = latihan logika dan komparasi
''''membuat gabungan area rentang dari angka'''

'''
    contoh rentang daerah antara 3 dan 10
    +++++ 3 ----- 10 +++++
    area di luar rentang (gabungan)
    rumus OR
'''
print("\n=====CONTOH SOAL 1=====")
a = float(input("\n masukan angka yang memiliki nilai\n kurang dari 3 atau lebih dari 10 = "))
# daerah kurang dari 3 bernilai True
a_kurang_dari = (a < 3)
print("jika kurang dari 3, maka ", a_kurang_dari)
#daerah lebih dari 10 bernilai True
a_lebih_dari = (a > 10)
print("jika lebih dari 10, maka ",a_lebih_dari)
#daerah rentang antara 3 dan 10
area_rentang = a_kurang_dari or a_lebih_dari
print("sehingga pada rentang 3 sampai 10 adalah",area_rentang)

'''
    contoh rentang antara 3 sampai 10
    ----- 3 +++++ 10 -----
    area di dalam rentang (irisan)
    rumus AND 
'''
print('\n=====CONTOH SOAL 2=====')
b = float(input("\ncontoh soal 2\n masukan angka yang memiliki nilai\n lebih dari 3 dan kurang dari 10 = "))
#daerah lebih dari 3
b_lebih_dari = b > 3
print("jika lebih dari 3, maka", b_lebih_dari)
#daerah kurang dari
b_kurang_dari = b < 10
print("jika kurang dari 10, maka", b_kurang_dari)
#daerah diantara rentang
area_rentang = b_lebih_dari and b_kurang_dari
print("sehingga pada rentang 3 dampai 10 adalah", area_rentang)

#soal nomor 1
print("\n===SOAL NOMOR 1===")
# ----- 0 +++++ 5 ----- 8 +++++ 11 -----
a = float(input("bilangan dengan ketentuan\n nilai pada rentang 0 sampai 5\n atau\n nilai pada rentang 8 sampai 11\n jika bilangan tersebut = "))
b = (0<a and a<5) or (8<a and a<11)
print("maka hasilnya ", b)

# soal nomor 2
print("\n===SOAL NOMOR 2===")
# +++++ 0 ----- 5 +++++ 8 ----- 11 +++++
p = float(input("bilangan dengan ketentuan\n kurang dari nol\n diantara 5 dan 8\n lebih dari 11\n jika bilagan tersebut = "))
q = (p<0 or 5<p and p<8 or p>11)
print("maka hasilnya ", q)