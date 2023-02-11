# If
ferrari_price = 5000000
varsta = int(input('ASL PLS'))
sold = int(input('Sold: '))
cash = int(input('Cash: '))
apt_de_munca = True

if sold < cash:
    print('Sold insuficient')
    if varsta < 18:
        print('Ai inca biberon')
    else:
        print('Bravo esti mare')
        if apt_de_munca:
            print('Angajeaza-te!')
elif sold == cash:
    print('Soldul va fi 0 daca se extrag banii')
else:
    sold = sold - cash
    print(sold)
    if sold > ferrari_price:
        print('Cumpara ferrari')
        sold = sold - ferrari_price
        print(sold)
        ferrari_discount = ferrari_price - ferrari_price*0.15
        if sold > ferrari_discount:
            print('Cumpara A 2a masina Ferrari')

    else:
        print ('Ia o Dacie')