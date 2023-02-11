fructe = ['mar', 'banana', 'portocala', 3, True, 3]
print(fructe)

# adaugam en el
fructe.append('rosie')

# suprascriem

fructe[0] = 'para'
print(fructe)
print(len(fructe))

# scoate si ne da ultimul element

last = fructe.pop()
print('ultimul element', last)
print('lista', fructe)

# de cate ori apare un element
print(fructe.count(3))

# extind lista
fructe_exotice = ['ananas', 'kiwi']
fructe.extend(fructe_exotice)
print(fructe)