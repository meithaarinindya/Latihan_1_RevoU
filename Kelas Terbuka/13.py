#pertemuan 13 = operator bitwise, operasi biner, binar
# note : pertemuan 12

a = 9
b = 5

#bitwise OR (|)
c = a | b
print("\n=====BITWISE OR=====")
print("nilai a = ",a,"binary = ",format(a,"08b"))
print("nilai b = ",b,"binary = ",format(b,"08b"))
print("----------")
print("nilai c = ",c,"binary = ",format(c,"08b"))

#bitwise AND (&)
c = a & b
print("\n=====BITWISE AND=====")
print("nilai a = ",a,"binary = ",format(a,"08b"))
print("nilai b = ",b,"binary = ",format(b,"08b"))
print("nilai c = ",c,"binary = ",format(c,"08b"))

#bitwise XOR (^)
c = a ^ b
print("\n=====BITWISE XOR=====")
print("nilai a = ",a,"binary = ",format(a,"08b"))
print("nilai b = ",b,"binary = ",format(b,"08b"))
print("nilai c = ",c,"binary = ",format(c,"08b"))

#bitwise NOT (~)
#mirror 0 dengan -1, 1 dengan -2, dst
c = ~a
d = ~b
print("\n=====BITWISE NOT=====")
print("nilai a     = ",a,"binary   = ",format(a,"08b"))
print("nilai NOT a = ",c,"binary = ",format(c,"08b"))
print("nilai b     = ",b,"binary   = ",format(b,"08b"))
print("nilai NOT b = ",d,"binary  = ",format(d,"08b"))
#mirror 0 dengan 1 maka bisa gunakan XOR
#misal ambil e = 11111111
e = 0b11111111
print("nilai flip biner a = ",a^e,"binary = ",format(a^e,"08b"))


#shifting

#shift right (>>)
c = a >> 1
print("\n=====SHIFT RIGHT=====")
print("nilai a       = ",a,"binary = ",format(a,"08b"))
print("shift right 1 = ",c,"binary = ",format(c,"08b"))

#shift left (<<)
d = a << 3
print("\n=====SHIFT LEFT=====")
print("nilai a      = ",a,"binary  = ",format(a,"08b"))
print("shift left 3 = ",d,"binary = ",format(d,"08b"))
