#copy list

print('\n','COPY LIST'.center(50,'='))

print('\n','-'*50,'\n')

#menduplikat list --> address akan sama

#membuat list baru dari list lama
A = ['plum','latte','blue','rose']
print(f'A = {A}')
B = A
print(f'B = {B}')

#cek address dari kedua list
print(f'address A = {hex(id(A))}')
print(f'address B = {hex(id(B))}')

#pembuktian
A.sort()
print(f'A = {A}')
B.reverse()
print(f'B = {B}')

print('\n','-'*50,'\n')

#menduplikat list --> address akan samberbeda

#copy
A = ['plum','latte','blue','rose']
print(f'A = {A}')
B = A.copy()
print(f'B = {B}')

#cek address dari kedua list
print(f'address A = {hex(id(A))}')
print(f'address B = {hex(id(B))}')

#pembuktian
A.sort()
print(f'A = {A}')
B.reverse()
print(f'B = {B}')

print('\n','-'*50,'\n')