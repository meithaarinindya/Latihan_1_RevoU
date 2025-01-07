#pertemuan 5 = variabel, data

print("=====TIPE DATA=====")
#tipe integer merupakan bilangan bulat
a = 3
print("data :", a, "tipe data :", type(a))
#tipe float merupakan bilangan desimal
b = 0.5
print("data :", b, "tipe data :", type(b))
#tipe string merupakan teks
c = "joshua"
print("data :", c, "tipe data :", type(c))
#tipe boolean merupakan nilai true & false
d = True
print("data :", d, "tipe data :", type(d))


#pertemuan 6 = tipe data
#casting = mengubah tipe data

print("\n=====CASTING DATA=====")
#casting data integer for variabel a
a_float = float(a)
print("data :", a_float, "tipe data :", type(a_float))
a_str = str(a)
print("data :", a_str, "tipe data :", type(a_str))
a_bool = bool(a)
print("data :", a_bool, "tipe data :", type(a_bool))

#casting data float for variabel b
b_integer = int(b)
print("data :", b_integer, "tipe data :", type(b_integer))
b_str = str(b)
print("data :", b_str, "tipe data :", b_str)
b_bool = bool(b)
print("data :", b_bool, "tipe data :", type(b_bool))

#casting data bool for variabel d
d_int = int(d)
print("data :", d_int, "tipe data :", type(d_int))
d_float = float(d)
print("data :", d_float, "tipe data :", d_float)
d_string = str(d)
print("data :", d_string, "tipe data :", type(d_string))

#casting data string for variabel c
c = 13
c_int = int(c) #string harus angka
print("data :", c_int, "tipe data :", c_int)
c_float = float(c) #string harus angka
print("data :", c_float, "tipe data :", type(c_float))
c_bool = bool(c)
c_boolean = bool() #false jika string kosong
print("data :", c_bool, "tipe data :", c_bool)
print("data :", c_bool, "tipe data :", c_boolean)