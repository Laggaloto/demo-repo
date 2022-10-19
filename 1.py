from konstans import *

r = float(input('Adja meg a kör sugarának hosszát: '))

def kkerulet(r: float):
    result = 2*r*PI
    return result

def kterulet(r: float):
    result = (r*2)*PI
    return result

kkkerulet = kkerulet(r) 
ktterulet = kterulet(r)

print(f'A kör kerülete: {kkkerulet} \nA kör területe: {ktterulet}')