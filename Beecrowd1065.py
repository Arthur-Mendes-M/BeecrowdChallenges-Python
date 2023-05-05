arr = [
    int(input()),
    int(input()),
    int(input()),
    int(input()),
    int(input())
]

pairs = []

for num in arr:
    if num % 2 == 0:
        pairs.append(num)

print(str(len(pairs)) + ' valores pares')