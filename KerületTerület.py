'''1. Hozzon létre egy feladat02.py fájlt.
2. Kérje be a felhasználótól a téglalap 2 oldalának a hosszát.
3. Számolja ki a téglalap kerületét (2*(a+b)) és területét (a*b).
4. Írja ki a felhasználónak az eredményeket, szépen megformázva.

'''
#import konstans
from konstans import *
#import konstans as k

def circlek(r: float):
    result = 2 * r * PI
    return result
def circklet(t: float):
    result = t*t * PI
    return result

a = float(input("Adja meg a kör sugarát: "))
b = float(input("Adja meg a kör területét: "))
kerulet = circlek(a)
terulet = circklet(b)


print(f"A kör kerülete: {kerulet}, területe: {terulet}")