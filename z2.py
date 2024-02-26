#zad2
def zad2(x: str):
    while x.startswith('0'):
        x = x[1:]
    while x.endswith('0'):
        x = x[:-1]
    x = x.split('1')
    holes = 0
    for i in range(len(x)):
        try:
            if x[i] != '':
                int(x[i])
                holes-=-1
        except:
            continue
    return f'Liczba dziur binarnych: {holes}'

print(zad2('0111001000100010'))
