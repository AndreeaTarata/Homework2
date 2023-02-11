# # 1 Verifica daca x are minim 4 cifre (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)

# x = int(input('Introdu o cifra: '))
# lungime = len(str(x))
# if lungime >= 4:
#     print(f'{x} are minim 4 cifre')
# else:
#     print(f'{x} NU are minim 4 cifre')
#
# # 2 Verifica daca x are exact 6 cifre

# if lungime == 6:
#     print(f'{x} are exact 6 cifre')
# else:
#     print(f'{x} NU are exact 6 cifre')

# # 3 Verifica daca x este numar par sau impar

# if x % 2 == 0:
#     print(f'{x} este nr impar')
# else:
#     print(f'{x} este numar impar')

# # 4 Avand trei variabile x, y, z (toate int) afiseaza in consola care este cel mai mare dintre
# ele

# y = 20
# z = int(input('z = '))
# if x > y > z or x > z > y:
#     print(f'{x} este mai mare decat {z} si {y}')
# elif y > x > z or y > z > x:
#     print(f'{y} este mai mare decat {z} si {x}')
# elif z > x > y or z > y > x:
#     print(f'{z} este mai mare decat {x} si {y}')
# else:
#     if x == y:
#         print(f'{x} este egal cu {y}, introduceti numere diferite')
#     elif z == y:
#         print(f'{z} este egal cu {y}, introduceti numere diferite')
#     elif x == z:
#         print(f'{x} este egal cu {z}, introduceti numere diferite')

# 5 Presupunand ca x, y, z - reprezinta unghiurile unui triunghi, verifica si afiseaza daca
# triunghiul este valid sau nu (un triunghi este valid daca suma tuturor unghiurilor este de
# 180 de grade sau daca suma lungimilor a oricare doua laturi este mai mare decat
# lungimea celei de-a treia laturi)

x = 50
y = int(input('Introdu unghiul y: '))
z = int(input('Introdu unghiul z: '))
if x + y + z == 180:
    print('Triunghiul este valid')
else:
    print('Triunghiul nu este valid')

# 6 Avand stringul: 'Coral is either the stupidest animal or the smartest rock' citește de
# la tastatura un număr x de tip int și afișează stringul fără ultimele x caractere. ex: dacă
# ați ales 7 se va afisa urmatorul string: 'Coral is either the stupidest animal or the
# smarte'

prop = 'Coral is either the stupidest animal or the smartest rock'
x = int(input('Introduceti numarul dorit: '))
print(prop[:-x]) #cut the kast letters

# 7 Folosindu-te de același string de la exercițiul 6, declara un string nou care sa fie format
# din primele 5 caractere + ultimele 5

sub1 = 'Coral'
sub2 = ' rock'
prop_new = sub1 + sub2
print(prop_new)

# 8 Folosindu-te de același string de la exercițiul 6, salvează într-o variabila și afiseaza
# indexul de start al cuvântului rock - adică poziția in string la care începe cuvântul rock
# (hint: este o funcție care te ajuta sa faci asta). Folosind aceasta variabila + slicing,
# afișează tot stringul pana la acest cuvant. Output asteptat: 'Coral is either the stupidest
# animal or the smartest '
# indexul de start al cuvantului rock
# scoatem cuvantul rock din propozitie

rock = prop.index('rock')
print(prop[:rock])

# 9 Citeste de la tastatura un string si verifica daca primul și ultimul caracter sunt la fel. Se
# va folosi un assert. Atentie: se dorește ca programul sa fie case insensitive, adica 'apA'
# e acceptat ca un string in care primul si ultimul caracter este la fel (hint, te poti folosi de o
# functie pentru a face string-ul case insensitive)

nou = input('Introdu un string: ').lower()
assert nou[0] == nou [-1]

#  10 Avand stringul '0123456789' afiseaza doar numerele pare si apoi doar numerele impare
# (hint: foloseste slicing si controleaza afisarea in slicing cu slicing step)

str = '0123456789'
print(str[0::2])
print(str[1::2])