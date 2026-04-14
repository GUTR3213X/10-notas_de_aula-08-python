N = int(input(">>> "))
i = 0
entradas = []
while i <= N:
    entradas.append(int(input(">>> ")))
    i += 1
print(f'menor valor: {min(entradas)}')
print(f'maior valor: {max(entradas)}')