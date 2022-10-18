
a = float(input("Adja meg a téglalap A oldalának hosszát: "))
b = float(input("Adja meg a téglalap B oldalának hosszát: "))

def kerulet(a, b: float):
    result = 2 * (a + b)
    return result

def terulet(a, b: float):
    result = a * b
    return result


tkerulet = kerulet(a, b)
tterulet = terulet(a, b)

print(f"\nA téglalap kerülete: {tkerulet} \nA területe pedig: {tterulet}")
