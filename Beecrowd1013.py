values = input()
numbers = []

for num in values.split(' '):
  numbers.append(int(num))

print(str(max(numbers)) + ' eh o maior')