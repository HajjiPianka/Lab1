##cw1
def cw1():
    a = []
    while True:
        b = input('Podaj liczbę całkowitą: ')
        if b == 'q' or b == 'Q':
            break
        try:
            b = int(b)
            if b not in a:
                a.append(b)
        except:
            print('Podana wartość nie jest liczbą całkowitą')
        print(f'Unikalne liczby: {len(a)}')

cw1()