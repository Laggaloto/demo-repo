'''Készítsünk olyan programot, amely induláskor megkérdezi hogy kör, 
téglalap, négyzet adatait kívánjuk-e kezelni. Majd bekéri a megfelelő síkidom jellemző adatait (sugár, oldalak hosszúsága), 
és kiírja a képernyőre a választott síkidom kerületét és területét.'''

from konstans import *

def circlek(r: float):
    result = 2 * r * PI
    return result

def circklet(t: float):
    result = t*t * PI
    return result

def kerulet(a, b: float):
    result = 2 * (a + b)
    return result

def terulet(a, b: float):
    result = a * b
    return result

v = int(input("Válassza ki, hogy mit szeretne vizsgálni\n 1 = Kör\n 2 = Téglalap\n Az ön választása: "))
while v != 1 and v != 2:
      v = int(input("Nincs ilyen opció, válasszon újra! : "))

if v == 1:
    a = float(input("Adja meg a kör sugarát: "))
    b = float(input("Adja meg a kör területét: "))
    kerulet = circlek(a)
    terulet = circklet(b)


    print(f"A kör kerülete: {kerulet}, területe: {terulet}")

elif v == 2:
    a = float(input("Adja meg a téglalap A oldalának hosszát: "))
    b = float(input("Adja meg a téglalap B oldalának hosszát: "))
    tkerulet = kerulet(a, b)
    tterulet = terulet(a, b)

    print(f"\nA téglalap kerülete: {tkerulet} \nA területe pedig: {tterulet}")
