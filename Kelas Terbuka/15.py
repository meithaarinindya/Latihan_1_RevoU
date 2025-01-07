#pertemuan 15 = perkenalan string

data = "data ini dalam bentuk string"
print(data)
print(type(data))

#  1. cara membuat string
'''
    1. menggunakan single quotes '...'
    2. menggunakan double quotes "..."
'''
#contoh :
data = 'data ini menggukana single quote'
print(data)
data = "data ini menggunakan double quotes"
print(data)
data = "'single quote pada string double quote'"
print(data)
data = '"double quotes pada string single quote"'
print(data)

# 2. Tanda backlash (\) untuk karakter khusus
data = 'jum\'at, g\'day, g\'nite'
print(data) #single quote pada string single quote
data = 'C:\\user\\joshua'
print(data) #backslash untuk backlash
data = 'joshua\t\t\tvernon'
print(data) #penggunaan tab
data = 'joshua \bvernon'
print(data) #backspace
data = 'seungcheol.\njeonghan.'
print(data) #newline LF = Line Feed
data = 'seungcheol.\rjeonghan.'
print(data) #CR = carriage Return
data = 'seungcheol.\r\njeonghan.'
print(data) #CRLF = Carriage Return Line Feed (Windows)

# 3. string literal atau raw

#tanpa menggunakan backslash
print(r'C:\new folder\n\r')

#multiline literal string
print("""
Nama    : Mingyu
Jabatan : Ketua Kelas Going Seventeen
""")

#multiline literal string dan RAW
print(r'''
Nama    : Joshua
Quotes  : /new journey
Website : www.joshua.com/newID
''')