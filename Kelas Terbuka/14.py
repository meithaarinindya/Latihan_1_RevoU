#operator assignment
''''
operasi yang dapat dilakukan dengan penyingkatam
operasi ditambah dengan assignment
'''
print("=====OPERATOR ASSIGNMENT=====\n")

print("-----KONSEP ASSIGNMENT-----")
#operasi penjumlahan
a = 5
b = a + 1
print("jika a =",a, "maka a + 1 =",b)
a += 1
print("atau dapat menggunakan rumus a += 1 =",a)

#operasi pengurangan
a = 7
b = a - 4
print("jika a =",a,"maka a - 4 =",b)
a -= 4
print("atau dapat menggunakan rumus a -= 4 =",a)

print("\n-----OPERASI DASAR ASSIGNMENT-----")

a = 5 #assignment
print("jika a =",a,", maka : ")

a += 7 #penjumlahan
print("a += 7 adalah",a)

a -= 7 #pengurangan
print("a -= 7 adalah",a)

a *= 7 #perkalian
print("a *= 7 adalah",a)

a /= 7 #pembagian
print("a /= 7 adalah",a)

a = 40 #assignment
print("jika a =",a,", maka :")
a %= 6 #modulus
print("a %= 6 adalah",a)

a = 40
print("jika a =",a,", maka :")
a //= 9 #floor division (pert 8)
print("a //= 9 adalah",a)

a = 5
print("jika a = ",a,", maka :")
a **= 3 #perpangkatan
print("a **= 3 adalah",a)

print("\n-----OPERASI BITWISE ASSIGNMENT-----")

p = True
p |= True
print("true OR true adalah",p)
p = True
p |= False
print("true OR false adalah",p)
p = False
p |= True
print("false OR true adalah",p)
p = False
p |= False
print("false OR false adalah",p)
p = True
p &= True
print("true AND true adalah",p)
p = True
p &= False
print("true AND false adalah",p)
p = False
p &= True
print("false AND true adalah",p)
p = False
p &= False
print("false AND false adalah",p)
p = True
p ^= True
print("true XOR true adalah",p)
p = True
p ^= False
print("true XOR false adalah",p)
p = False
p ^= True
print("false XOR true adalah",p)
p = False
p ^= False
print("false XOR false adalah",p)

q = 0b0100
print("\njika q =",q,"binary =",format(q,"04b"))
q >>= 2
print("maka swift right 2 adalah",format(q,"04b"))
q <<= 3
print("maka swift left 3 adalah",format(q,"04b"))