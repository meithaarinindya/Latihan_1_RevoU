#Looping dari list

print('\n')

#for loop
'''
for i in A :
    print(i)
'''

a = [4,3,2,5,6,1]
print(a)

for i in a :
    print(i)

print('\n')

b = ['eden','sky','sage','mars','orion','puto']
print(b)

for i in b :
    print(i)

print('\n','-'*30,'1\n')

#for loop and range
'''
variabel p | p = len(A)
for i in range(p) :
    print((a[i]))
'''

a = [4,3,2,5,6,1]
print(a)

p = len(a)

for i in range(p) :
    print(a[i])

print('\n','-'*30,'2\n')

#while loop
'''
variabel r | r = len(A)
variabel i = 0
while i < r :
    print(i)
    i += 1
'''

a = [10,5,4,2,6,5]
print(a)

r = len(a)
i = 0

while i < r :
    print(i)
    i += 1

print('\n','-'*30,'3\n')

#list comprahension
'''[print(i) for i in A]'''

a = ['eden','sky','sage','mars','orion','puto']
print(a)

[print(i) for i in a]

print('\n','-'*30,'4\n')

#enumerate
'''for index,data in enumerate(A)'''

a = ['eden','sky','sage','mars','orion','puto']
print(a)

for index,data in enumerate(a) :
    print(index,data)

#data kuadrat

a = [10,5,4,3,6,5]
print(f'\n{a}')
b = [i**2 for i in a]
print(b)
