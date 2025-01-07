#copy untuk nesting list

print('\n','-'*30,'1\n')

#mengambil data dari nested list
a = [1,2]
b = [3,4]
p = [a,b]
print(f'p = {p}')

c = p[0]
print(c)
d = p[0][0]
print(d)

print('\n','-'*30,'2\n')

#shallow copy
print('SHALLOW COPY\n')

a = [1,2]
b = [3,4]
p = [a,b]
print(f'a = {a}\nb = {b}\np = {p}')

q = p.copy()
print(f'q = {q}')

print('\n')

#pembuktian
p[0][0]='joshua'
print(f'p = {p}')
print(f'q = {q}') #shallow copy

print('\n')

#address semuanya
print(f'address p = {hex(id(p))}')
print(f'address q = {hex(id(q))}') #address list copy berbeda

print(f'address item 1 = {hex(id(p[0][0]))}')
print(f'address item 1 = {hex(id(q[0][0]))}') # address item copy masih sama

print('\n')

#deep copy
print('DEEP COPY\n')

a = [1,2]
b = [3,4]
p = [a,b]
print(f'a = {a}\nb = {b}\np = {p}')

from copy import deepcopy

q = deepcopy(p)
print(p)

print('\n')

#pembuktian
p[0][0]= 'joshua'
print(f'p = {p}')
print(f'q = {q}') #shallow copy

print('\n')

#address semuanya
print(f'address p = {hex(id(p))}')
print(f'address q = {hex(id(q))}') #address list copy berbeda

print(f'address item joshua = {hex(id(p[0][0]))}')
print(f'address item 1 = {hex(id(q[0][0]))}') # address item copy masih sama

print('\n')

