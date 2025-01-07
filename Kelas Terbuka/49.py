'''TYPE HINTS UNTUK FUNGSI'''

#penggunaan type hints

def f(x:int)->int:
    y = 10**x
    return y

print(f(2))

import string

def g(x:string):
    print(x)

g('Joshua')