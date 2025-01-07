'''FUNGSI DENGAN KEMBALIAN (RETURN VALUE)'''

#fungsi kuadrat

def f(x) :
    y = x**2
    return y

y = f(4)
print(y)

z = 10 + f(7)
print(z)

print('-'*50,'1\n')

#fungsi tambah

def f(x,y) :
    return(x + y)

a = f(10,8)
print(a)

print('-'*50,'2\n')

#fungsi dengan return banyak

def f(x,y) :
    a = x + y
    b = x - y
    c = x * y
    d = x / y
    return a,b,c,d

p,q,r,s = f(4,5)

print(p)
print(q)
print(r)
print(s)

