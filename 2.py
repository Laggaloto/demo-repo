a=float(input('Kedves felhasználÓ!\nKérem adja meg a a téglalap 1. oldalának a hosszát: '))
b=float(input('2. oldalának a hossza: '))

def tkerulet(a,b:float):
    result = 2*(a+b)
    return result

def tterulet(a,b:float):
    result = a*b
    return result

ter = tterulet(a,b)
ker = tkerulet(a,b)

print(f'A téglalapocska területecskéje: {ter}\n kerületecskéje pedig: {ker}')