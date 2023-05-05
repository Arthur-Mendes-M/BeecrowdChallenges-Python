firstLine = input() # X1 e Y1
secondLine = input() # X2 e Y2

x1 = float(firstLine.split(' ')[0])
x2 = float(secondLine.split(' ')[0])
y1 = float(firstLine.split(' ')[1])
y2 = float(secondLine.split(' ')[1])

distance = ((x2 - x1)**2 + (y2 - y1)**2)**.5

print('%0.4f' % distance)