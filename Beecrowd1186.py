operation = input()

matriz = []
size = 12

for index in range(size):
    row = []
    for element in range(size):
        row.append(float(input()))
    matriz.append(row)

newMatriz = []

for line in range(1, size):
    for column in range(size-line, size):
        newMatriz.append(matriz[line][column])

result = 0
if operation == 'S':
    result = sum(newMatriz)
elif operation == 'M':
    result = sum(newMatriz) / len(newMatriz)

print("%0.1f" %result)