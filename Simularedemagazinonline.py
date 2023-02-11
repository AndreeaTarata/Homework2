"""
user introduce din consola nume, an nastere, luna, ziua, CNPul
verificam daca userul e major - daca da se logheaza, daca nu il trimitem acasa
daca e major - incercam sa extragem din cnp anul nasterii si sa verificam daca corespunde cu anul nasterii pe care l-a introdus el
daca nu e ok - userul nu este lasat sa intre pe site
daca da extragem pe baza primei cifre din CNP daca user e barbat sau femeie
daca e femeie se afiseaza un strig - parfum
daca e barbat un string - cu pantofi
daca nu e nici barbat nici femeie - afiseaza esti un robot
"""

nume = input('Introdu numele: ')
an_nastere = int(input('Introdu anul nasterii: '))
luna = int(input('Introdu luna nasterii: '))
ziua = int(input('Introdu ziua nasterii: '))
cnp = int(input('Introdu CNP: '))

#varsta unei persoane!
import datetime

azi = datetime.date.today()
print(azi)
varsta = float(azi.year - an_nastere - ((azi.month, azi.day) < (luna, ziua)))
print(varsta)
if varsta > 18:
    print('Bine ati venit pe site-ul nostru')
else:
    print('Ai nevoie de un parinte pentru a intra pe acest site - ACCES DIENIED')

cnp = str(cnp)
if len(cnp) != 13:
    print('CNP-ul trebuie sa aiba 13 cifre')
an_cnp = cnp[1] + cnp[2]
print(an_cnp)
an_nastere = str(an_nastere)
an_nastere = an_nastere[2:]
print(an_nastere)
gen = cnp[0]
print(gen)
gen = int(gen)
if an_nastere == an_cnp:
    print('Anul nasterii din CNP corespundel anului de nastere introdus')
    if gen == 1:
        print('PANTOF de barbat')
    elif gen == 2:
        print('PARFUM de femeie')
    else:
        print('esti ROOOBBOOOTTT')
else:
    print('Introdu din nou anul nasterii, altfel nu poti intra pe site: ')



