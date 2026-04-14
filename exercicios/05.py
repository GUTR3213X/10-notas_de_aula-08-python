N = int(input("[0] >>> "))

if 0 <= N <= 10:
    i = N
    soma = 0
    while i > 0:
        soma += float(input("[0.0] >>> "))
        i -= 1
    print(soma / N)