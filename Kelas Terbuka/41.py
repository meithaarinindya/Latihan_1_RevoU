#copy & pop dictionary

print('\nCOPY & POP DICTIONARY\n')

#copy biasa

dream = {
    'nj':'na jaemin',
    'ml':'mark lee',
    'lj':'lee jeno',
    'hr':'huang renjun',
    'lh':'lee haechan',
    'zc':'zhong chenle',
    'pj':'park jisung'
}

print(f'dream: {dream}\n')

nct = dream
print(f'nct : {nct}\n')

dream['ml']='kim doyoung'
print(f'dream: {dream}\n')
print(f'nct : {nct}\n')

print('\n','-'*50,'1','\n')

#copy dict

dream = {
    'nj':'na jaemin',
    'ml':'mark lee',
    'lj':'lee jeno',
    'hr':'huang renjun',
    'lh':'lee haechan',
    'zc':'zhong chenle',
    'pj':'park jisung'
}
print(f'dream: {dream}\n')

nct = dream.copy()
print(f'nct : {nct}\n')

dream['ml']='kim doyoung'
print(f'dream: {dream}\n')
print(f'nct : {nct}\n')

print('\n','-'*50,'2','\n')

#pop dict -> transfer item

dream = {
    'nj':'na jaemin',
    'ml':'mark lee',
    'lj':'lee jeno',
    'hr':'huang renjun',
    'lh':'lee haechan',
    'zc':'zhong chenle',
    'pj':'park jisung'
}
print(f'dream: {dream}\n')

nct127 = dream.pop('ml')
print(f'nct127 = {nct127}\n')
print(f'dream = {dream}\n')

#pop item dict -> transfer item terakhir

dream = {
    'nj':'na jaemin',
    'ml':'mark lee',
    'lj':'lee jeno',
    'hr':'huang renjun',
    'lh':'lee haechan',
    'zc':'zhong chenle',
    'pj':'park jisung'
}
print(f'dream: {dream}\n')

lastdream = dream.popitem()
print(f'nct127 = {lastdream}\n')
print(f'dream = {dream}\n')