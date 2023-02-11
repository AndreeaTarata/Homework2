varsta = int(input('Varsta dv. este : '))
print(varsta)
varsta_ok = varsta >=18
varsta_no = varsta < 18
pasaport = input('Detineti un pasaport?  : ')
print(pasaport)
pasaport_da = 'da'
pasaport_nu = 'nu'





if varsta >=18  and pasaport == pasaport_da:
    print('Aveti dreputl sa calatoriti')
elif varsta >= 18 and pasaport == pasaport_nu:
    print('major fara pasaport, nu puteti calatori')
else:
    print('Suntei minor, trebuie sa calatoriti cu unul dintre parinti cel putin')

insotit_mama =input('Sunteti insotit de mama: ')
print(insotit_mama)
insotit_mama_da = 'da'
insotit_mama_nu = 'nu'
insotit_tata =input('Sunteti insotit de tata: ')
print(insotit_tata)
insotit_tata_da = 'da'
insotit_tata_nu = 'nu'





if insotit_mama == insotit_mama_da and insotit_tata == insotit_tata_da:
    print('Indepliniti conditiile, calatoriti impreuna cu ambii parinti')
elif insotit_mama == insotit_mama_da and insotit_tata == insotit_tata_nu:
    print('Calatoriti doar cu mama, dar aveti nevoie de act de permisiune a tatalui')
elif insotit_tata == insotit_tata_da and insotit_mama == insotit_mama_nu:
    print('Calatoriti impreuna cu tata, dar aveti nevoie de act de permsiune a mamei')
else:
    print('Sunteti minor nu puteti calatori singur')
act_permisiune_tata = input('atasati actul de permisiune al  tatalui: ')
print(act_permisiune_tata)
act_permisiune_tata_da = 'da'
act_permisiune_tata_nu = 'nu'



act_permisiune_mama = input('atasati actul de permisiune al  mamei: ')
print(act_permisiune_mama)
act_permisiune_mama_da = 'da'
act_permisiune_mama_nu = 'nu'

if insotit_tata == insotit_tata_da and insotit_mama == insotit_mama_nu and act_permisiune_mama == act_permisiune_mama_da:
    print('calatoriti cu tata, cu act de permisiune din partea mamei')
elif insotit_tata == insotit_tata_da and insotit_mama == insotit_mama_nu and act_permisiune_mama == act_permisiune_mama_nu:
    print('nu puteti calatoriti cu tata, cu act de permisiune din partea mamei')
elif insotit_mama == insotit_mama_da and insotit_tata== insotit_tata_nu and act_permisiune_tata == act_permisiune_tata_da :
    print('calatoriti cu mama, cu un act de permisiune din partea tatalui')
elif insotit_mama == insotit_mama_da and insotit_tata== insotit_tata_nu and act_permisiune_tata == act_permisiune_tata_nu :
    print('Nu puteti calatori fara act de permisiune din partea tatalui')
else:
    print('Nu puteti calatori fara nicio permisiune ')