# # nota_de_trecere = 4.5
# # nota = float(input('alege nota'))
# # if nota > nota_de_trecere:
# #     print(f'ai luat {nota}')
# #     print('felicitari ai trecut examenul')
# # else:
# #     print('nu ai treceut')
# #
# #
# # # robotel telefonic
# # optiunea = int(input('alege o optiune'))
# # if optiunea == 0:
# #     print('meniu anterior')
# # elif optiunea == 1:
# #     print("ati ales ro")
# # elif optiunea == 2:
# #     print('ati ales eng')
# # else:
# #     print('nu am indentif opt')
#
# x = 50.17
# # sa afisam 17
# print(str(x)[3::])
#
# y = int(x*100)
# print(y)
#
# l = y % 100
# print(l)
#
# x = 9
# y = 7
#
# x, y = y, x
# print(x)
# print(y)
#
# a = x
# x = y
# y = a
# print(x, y)
#
# x = x * y
# y = x % y
# x = x % y
#
# print(x, y)

sold = int(input('Sold: '))
cash = int(input('Cash: '))
sold = sold - cash
print(sold)
if sold < 0:
    print('xxx')

