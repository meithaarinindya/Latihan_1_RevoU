'''ARGS PADA FUNGSI'''

#memasukan data/argumen
def f(p,q,r) :
    print(f'{p} memiliki tinggi {q} dan berat {r}')
f('Joshua',177,65)

def f(x):
    data = x.copy()
    p = data[0]
    q = data[1]
    r = data[2]
    print(f'{p} memiliki tinggi {q} dan berat {r}')
f(['Joshua',177,65])


#args
def f(*args):
    p = args[0]
    q = args[1]
    r = args[2]
    print(f'{p} memiliki tinggi {q} dan berat {r}')
f('Joshua',177,65)

print('-'*50,'1\n')

#
def f(*args):
    #data tipenya tuple, dia bisa diiterasi
    y = 0
    for i in *args :
        output += i

y = f(1,2,3,4,5,6,7,8,9)
print(f'hasil = {y}')