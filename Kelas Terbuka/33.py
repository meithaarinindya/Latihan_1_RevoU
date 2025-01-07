#nasted list/ list bersarang
#membuat list bagian

print('\n','-'*30,'1\n')

a = [1,2]
print(a)

b = [3,4]
print(b)

s = [1,2,3,4]
print(s)

c = [a,b]
print(c)

print('\n','-'*30,'2\n')

#pengaplikasian

p = ['Oh Si On','Sion','11 Mei 2002']
q = ['Maeda Riku','Riku','28 Juni 2003']
r = ['Tokuno yushi','Yushi','5 April 2004'] 
s = ['Kim Daeyoung','Jaehae','21 Juni 2005']
t = ['Hirose Ryo','Ryo','4 Agustus 2007']
u = ['Fujinaga Sakuya','Sakuya','18 November 2007']

print(f'\n{p}\n{q}\n{r}\n{s}\n{t}\n{u}\n')

w = [p,q,r,s,t,u]
print(w)

print('\n','-'*30,'3\n')

for i in w :
    print(f'Nama Lahir\t: {i[0]}')
    print(f'Nama Panggung\t: {i[1]}')
    print(f'Tanggal Lahir\t: {i[2]}\n')

print('\n','-'*30)
