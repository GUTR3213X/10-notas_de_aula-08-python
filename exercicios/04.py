N = int(input(">>> "))

i = N
if N >= 0:
    resultado = 1
    while i > 0:
        resultado *= i
        i -= 1
    print(f'{N}! = {resultado}')