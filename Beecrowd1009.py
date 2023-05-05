firstName = input()
currentSalary = float(input())
value = float(input())

total = currentSalary + (15 / 100 * value)

print('TOTAL = R$ %0.2f' % total)