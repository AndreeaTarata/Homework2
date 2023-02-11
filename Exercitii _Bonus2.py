# 1
'''
1. 1. Vrem sa cream o aplicatie pentru achizitionare bilete de avion care sa primeasca drept
inputuri urmatoarele informatii:
a. Varsta
b. Insotit de mama
c. Insotit de tata
d. Pasaport
e. Act permisiune mama
f. Act permisiune tata
Conditii de imbarcare:
1. Daca pers are varsta peste 18 ani si are pasaport
2. Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti
3. Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte
si are permisiune in scris de la celalat parinte

Scrie codul care implementeaza conditiile de imbarcare de mai sus si testeaza-l cu toate
variantele care crezi ca ar trebui testate. Genereaza scenarii de testare cu expected results si
apoi ruleaza codul pentru a verifica daca expected results sunt egale cu actual results.
Exemple:
1. Varsta 19 ani, nu am pasaport => Nu ma pot imbarca
2. Varsta 17 ani, am pasaport, ambii parinti => Ma pot imbarca
Scenarii de testare:
1. Varsta 19 ani, nu am pasaport => Nu ma pot imbarca - Passed
2. Varsta 17 ani, am pasaport, ambii parinti => Ma pot imbarca - Passed
3. Varsta 35 ani, am pasaport => Ma pot imbarca
4. Varsta 5 ani, am pasaport sunt cu tata si am permisiune de la mama => Ma pot imbarca
5. Varsta 5 ani, am pasaport sunt cu mama si am permisiune de la tata => Ma pot imbarca
6. Varsta 19 ani, nu am pasaport, am permisiune de la mama => Nu ma pot imbarca
7. Varsta 5 ani, am pasaport, fara parinti, fara permisiuni => Nu ma pot imbarca

'''
varsta = int(input('Introdu varsta: '))
pasaport = (input('Are pasaport?: '))
print(pasaport)


if varsta >= 18 and pasaport == 'True':
    print('Felicitari! Va puteti imbarca')

else:
    if varsta < 18:
        insotit_mama = input('Insotit de mama?: ')
        insotit_tata = input('Insotit de tata?: ')
        if pasaport == 'True' and insotit_tata == 'True' and insotit_mama == 'True':
            print('Felicitari! Va puteti imbarca cu mama si cu tata')
        else:
            act_permisiune_mama = input('Are act de permisiune de la mama?:')
            act_permisiune_tata = input('Are act de permisiune de la tata?:')
            if pasaport == 'True' and insotit_tata == 'True' and act_permisiune_mama == 'True':
                print('Felicitari! Va puteti imbarca cu tata')
                act_permisiune_mama = input('Are act de permisiune de la mama?:')
                act_permisiune_tata = input('Are act de permisiune de la tata?:')
            elif pasaport == 'True' and insotit_mama == 'True' and act_permisiune_tata == 'True':
                print('Felicitari! Va puteti imbarca cu mama')
    else:
        print('Nu va puteti imbarca')



# # 2 Joc de noroc
# - Cauta pe net si vezi cum se genereaza un numar random
# - Imagineaza-ti ca dai cu zarul si salvezi acest numar intr-o variabila numita dice_roll.
# Numarul salvat va fi generat random cu metoda gasita in online
# - Introdu un numar de la tastatura care sa reprezinte numarul ales de la utilizator
# - Verifica si afiseaza daca utilizatorul a ghicit numarul
# - Vor exista 3 optiuni care vor trebui tratate:
# ● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
# ● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
# ● Ai ghicit. Felicitari? Ai ales x si zarul a fost y

# numar = int(input('Introduceti un numar la noroc: '))
# import random
# zar = [1, 2, 3, 4, 5, 6]
# print('posibiliti zar: ', zar)
# random.shuffle(zar)
# dice_roll = zar[1]
# print(dice_roll)
# if numar < dice_roll:
#     print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {numar} dar a fost {dice_roll}')
# elif numar > dice_roll:
#     print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {numar} dar a fost {dice_roll}')
# else:
#     print(f'Ai ghicit!!! Felicitari. Ai ales {numar} si zarul a fost {dice_roll}')
#
#
#
