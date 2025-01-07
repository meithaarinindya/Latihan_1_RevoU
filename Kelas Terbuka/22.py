#ELIF STATEMENT

'''
a = description         --> start
if a == condition 1     --> answer 1
    print()             --> action for c1 (true)
elif a == condition 2   --> answer 2
    print()             --> action for c1 (true)
elif a == condition 3   --> answer 3
    print()             --> action for c1 (true)
else :
    print()             --> action (false)
print()                 --> end
'''

a = input('Who are u? ')

if a == "joshua" :#kondisi 1
    print('halo joshua!') #aksi true 1
elif a == "vernon" : #kondisi 2
    print('halo vernon') #aksi true 2
elif a == "seungcheol" : #kondisi 3
    print('halo seungcheol!') #aksi true 3
else :
    print('sorry, you\'re not human. You\'re a tiger. Hehe.') #aksi false

