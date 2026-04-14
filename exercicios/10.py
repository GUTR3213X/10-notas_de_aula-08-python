N = int(input(">>> "))
i = 0
a = 0
b = 1
if i <= N:
    temp = a + b
    a = b
    b = temp
    i += 1
print(b)