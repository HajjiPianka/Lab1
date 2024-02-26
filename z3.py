#zad 3
def zad3():
    a = set(input('Podaj pierwszy zbiór w postaci: x,y,...,z: ').split(','))
    b = set(input('Podaj drugi zbiór w postaci: x,y,...,z: ').split(','))
    
    #suma
    suma = ['Suma:',*set(a.union(b))]
    roznica = ['Różnica:', *a.difference(b)]
    wspol = ['Część wpólna:', *a.intersection(b)]
    sym = ['Różnica symetryczna:',*a.symmetric_difference(b)]
    print(*suma)
    print(*roznica)
    print(*wspol)
    print(*sym)
zad3()