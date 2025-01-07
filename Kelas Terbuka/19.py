#string width and allignment

#data
a = "hansol vernon chwe"
b = "amerika serikat"
c = "18 februari 1998"
d = "rapper"

#string
data = f"nama lengkap = {a}; tempat lahir = {b}; tanggal lahir =  {c}; pekerjaan = {d}"
print("Data String".center(30,"-"))
print(data)

#string multiline (\n newline)
data = f"nama lengkap = {a}\ntempat lahir = {b}\ntanggal lahir = {c}\npekerjaan = {d}"
print("\n","Data String Multiline".center(30,"-"))
print(data)

#string multiline (''' kutip triplets)
data = f'''
nama lengkap = {a:>18}
tempat lahir  = {b:>18}
tanggal lahir = {c:>18}
pekerjaan     = {d:>18}
'''
print("\n","Data String Multiline".center(30,"-"))
print(data)
