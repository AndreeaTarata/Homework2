# 1. Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else
# if else - este o ramura in cod care va curge de sus in jos in functie de conditiile puse (true sau false)
# daca nu se gasesste true in if codul curge direct in else si nimic din if nu va mai fi luat in considerare
# 2. Verifica si afiseaza daca x este numar natural sau nu (un numar se considera natural
#

x = int(input('introduceti un numar: '))
if x > 0:
    print(f'{x} este numar natural')
else:
    x < 0
    print(f'{x} nu este un numar natural')

# 3 Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru

if x > 0:
    print(f'{x} este numar pozitiv')
elif x == 0:
    print('numar neutru')
else:
    x < 0
    print(f'{x} este un numar negativ')

# 4 Verifica si afiseaza daca x este intre -2 si 13 (incluzand captele de interval).

if x >= -2 and x <= 13:
    print(f'{x} este in intervalul -2 si 13')
else:
    print(f'{x} nu este in intervalul -2 si 13')

# 5 Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5 (diferenta inseamna
# cate numere sunt intre x si y, nu rezultatul diferentei intre x si y). Hint: Se va folosi functia
# abs

y = 20
dif = abs(x - y) - 1
if dif < 5:
    print(f'Diferenta {dif} este mai mica decat 5')
else:
    print(f'Diferenta {dif} NU este mai mica decat 5')

#  Verifica daca x NU este intre 5 si 27, incluzand capetele de interval. (a se folosi ‘not’)

lista = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
if x != lista:
    print(x not in lista)
    print(f'{x} nu este in lista')
else:
    print(f'{x} este in lista')

# 7 Declara o noua variabila y de tip int si apoi verifica si afiseaza daca x si y sunt egale,
# daca nu, afiseaza care din ele este mai mare

if x == y:
    print(f'{x} este egal cu {y}')
else:
    if x > y:
        print(x)
    else:
        print(y)

# 8 Presupunand ca x, y, z (toate de tip int) - reprezinta laturile unui triunghi, afiseaza daca
# triunghiul este isoscel (doua laturi sunt egale), echilateral (toate laturile sunt egale) sau
# oarecare (nicio latura nu e egala).

z = int(input('Latura z = '))
if (x == y or x == z or y == z) and (x != z or y != z or x != y):
    print('triunghiul este isoscel')
elif x == y == z:
    print('toate laturile sunt egale')
else:
    print('nicio latura nu e egala')

# 9 Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu. Atentie!
# Trebuie sa evaluati si cazurile uppercase si cazurile lowercase.

litera = input('Litera este: ')
a ,e ,i ,o ,u ,A ,E ,I ,O ,U = 'a','e' ,'i' ,'o','u' ,'A' ,'E' ,'I' ,'O' ,'U'
if litera in (a ,e ,i ,o ,u ,A ,E ,I ,O ,U):
    print('litera introdusa este o vocala')
else:
    print('Litera introdusa nu este o vocala')

# 10 Transforma si printeaza notele din sistem românesc in sistem american dupa cum
# urmeaza:
# a. Peste 9 => A
# b. Peste 8 => B
# c. Peste 7 => C
# d. Peste 6 => D
# e. Peste 4 => E
# f. 4 sau sub => F

nota = float(input('Introduceti Nota: '))
if nota >= 9 and nota <= 10:
    print('Peste 9 => A')
elif nota < 9 and nota >= 8:
    print('Peste 8 => B')
elif  nota < 8 and nota >= 7:
    print('Peste 7 => C')
elif  nota < 7 and nota >= 6:
    print('Peste 6 => D')
elif  nota < 6 and nota > 4:
    print('Peste 4 => E')
else:
    if nota > 1 and nota <= 4:
        print('4 sau sub => F')
    else:
        print('Aceasta cifra nu este o nota!')
