#looping dictionary

print('\nLOOPING DICTIONARY\n')

dream = {
    'nj':'na jaemin',
    'ml':'mark lee',
    'lj':'lee jeno',
    'hr':'huang renjun',
    'lh':'lee haechan',
    'zc':'zhong chenle',
    'pj':'park jisung'
}

print(f'dream = {dream}')

print('\n','-'*50,'1','\n')

#looping for in -> akan mengeluarkan keyword
for i in dream :
    print(i)

print('\n','-'*50,'2','\n')

#operatation untuk mengambil iterables

'''
.keys -> keyword
.values -> value
.items -> keyword dan value
'''

x = dream.keys()
print(x)
for i in dream.keys() :
    print(dream.get(i))

print('\n','-'*50,'3','\n')

y = dream.values()
print(y)
for i in dream.values() :
    print(i)

print('\n','-'*50,'4','\n')

z = dream.items()
print(z)
for i in dream.items() :
    print(i)

print('\n','-'*50,'5','\n')

for x,y in dream.items() :
    print(f'key = {x}, value = {y}')

print('\n','-'*50,'\n')