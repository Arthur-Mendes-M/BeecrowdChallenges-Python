values = input()
a = float(values.split(' ')[0])
b = float(values.split(' ')[1])
c = float(values.split(' ')[2])

message = 'TRIANGULO: %0.3f' % ((a * c) / 2)
message += '\nCIRCULO: %0.3f' % (3.14159 * (c * c))
message += '\nTRAPEZIO: %0.3f' % (((a + b) * c) / 2)
message += '\nQUADRADO: %0.3f' % (b * b)
message += '\nRETANGULO: %0.3f' % (a * b)

print(message)