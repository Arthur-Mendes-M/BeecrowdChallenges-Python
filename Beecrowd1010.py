values1 = input()
values2 = input()

calc = int(values1.split(' ')[1]) * float(values1.split(' ')[2]) + int(values2.split(' ')[1]) * float(values2.split(' ')[2])

print('VALOR A PAGAR: R$ %0.2f' % calc)