# declaram o variabila in care sa stocam un float si vrem sa afisam pe ecran 2 valori cu zecimale de dupa punct

x = 50.17
# sa afisam 17

print(str(x)[3:])
y = int(x*100)
print(y)

l = y % 10
print(l)

m = y % 100
print(m)

