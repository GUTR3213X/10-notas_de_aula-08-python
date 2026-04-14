N = int(input(">>> "))
i = 0
pares = 0
impares = 0
while i <= N:
    entrada = int(input(">>> "))
    if entrada % 2 == 0:
        pares += 1
    else:
        impares += 1
    i += 1
print(f'pares: {pares}')
print(f'impares: {impares}')