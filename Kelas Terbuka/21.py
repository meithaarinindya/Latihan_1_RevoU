# IF dan ELSE statement

#if statement untuk jawaban dengan beberapa kondisi
#control flow : kondisi user merupakan alur yang bisa dikendalikan

# 1. IF
'''
program selanjutnya harus boolean (true/false)
a = description                 --> start
if a == condition : print()     --> answer & action (true)
print()                         --> end
'''
print('\n','PROGRAM 1'.center(10,'-'))
print("jawab dengan menggunakan ya/ tidak")
a = input('Apakah kamu ulat? ')
if a=="ya" : print("Kamu akan menjadi kupu-kupu!")
print("Selesai")

# 2. IF INDENTATION
''''
indentasi adalah tab untuk program selanjutnya
a = description         --> start
if a == condition :     --> answer
    print()             --> action (true)
print()                 --> end
'''
print('\n','PROGRAM 2'.center(30,'-'))
print('jawab dengan menggunakan ya/ tidak')
a = input('Apakah kamu ulat? ')
if a =="ya" :
    print("Kamu akan menjadi kupu-kupu!") #lebih sering digunakan
print("selesai")

# 3. ELSE STATEMENT
'''
a = description         --> start
if a == condition       --> answer
    print ()            --> action (true)
else :
    print ()            --> action (false)
print()                 --> end
'''
print('\n','PROGRAM 3'.center(30,'-'))
print('jawab dengan menggunakan ya/ tidak')
a = input('Apakah kamu ulat? ')
if a=="ya":
    print("Kamu akan menjadi kupu-kupu!")
else :
    print("Kamu tidak akan menjadi kupu-kupu.")
print('selesai')  
