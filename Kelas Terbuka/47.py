'''DEFAULT ARGUMENT'''

'''
def fungsi(argument = nilai defaultnya) :
'''
#contoh 1
def f(x = "Seungcheol") :
    print(f'hallo {x}')

f('Joshua')
f()

print('-'*50,'1\n')

#contoh 2
def f(x,y = 'Apa kabar?') :
    print(f'Halo {x}, {y}')

f('Joshua','You\'re so gentlemen')
f('Seungcheol')

print('-'*50,'2\n')

#contoh 3
def f(x, pangkat) :
    y = x**pangkat
    return y

y = f(3,2)
print(y)

y = f(pangkat = 3,x = 5)
print(y)

#contoh 4
def f(p = 1,q = 2,r = 3,s = 4,t = 5) :
    y = p + q + r + s + t
    return y

print(f())
print(f(q = 10)) #hanya variabel q yang diubah
