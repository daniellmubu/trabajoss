def staircase(n):
    for i in range(1,n+1):
        espacios = ' ' * (n-i)
        relleno = '#' * i
        total = espacios + relleno
        print(total)
print(staircase(4))
