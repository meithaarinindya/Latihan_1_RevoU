#List

print('\n','LIST'.center(30,'='))

print('\n','CONTOH LIST'.center(30))
print('-'*31)

A = [1, 2, 3, 4]    #kumpulan data numbers
print('A =',A)
B = [4, 2, 7, 1]    #kumpulan data numbers
print('B =',B)
C = ['eden', 'sky', 'rue', 'pepper', 'sage']  # kumpulan data string
print('C =',C)
D = [True, False, False, True] #kumpulan data boolean
print('D =',D)
E = [1,'eden',True,2,'sky',False] #data campuran
print('E =',E)

'''
cara membuat list
'''

print('-'*31)

# 1. menggunakan range(start,stop,step)

A = range(0,10)
print(A)

#list
B = list(range(0,10))
print(B)

C = [i for i in range(0,10)]
print(C)
D = [i**2 for i in range(0,10)]
print(D)

print('-'*31)

# 2. cara alternatif menggunakan for loop, list comprehension

A = [i for i in range(0,10)]
print(A)
B = [i**2 for i in range(0,10)]
print(B)

print('-'*31)

# 3. menggunakan for pakai if

A = [i for i in range(0,10) if i != 5]
print(A)
B = [i for i in range(0,10) if i%2 == 0]
print(B)
C = [i**2 for i in range(0,10) if i%2 != 0]
print(C)