'''1. Hozzon létre egy feladat02.py fájlt.
2. Kérje be a felhasználótól a téglalap 2 oldalának a hosszát.
3. Számolja ki a téglalap kerületét (2*(a+b)) és területét (a*b).
4. Írja ki a felhasználónak az eredményeket, szépen megformázva.
5. Hozzon létre egy feladat02_b.py fájlt, majd csinálja meg úgy a feladatot, hogy létrehoz 2 db üres listát:
	- Az első listához adja hozzá a bekért adatokat.
	- A második listához adja hozzá az eredményeket.
6. A kiiratást úgy csinálja meg, hogy a kiiratás során a lista megfelelő indexével hívja elő az eredményt, és azt írja bele a formázott kiirató szövegbe.
6+1. Az eredményt tartalmazó listát konvertálja át és mentse el egy tuple-be.
'''
bekert=[]
bekert.append(int(input("Kerem a teglalap A oldalát: ")))
bekert.append(int(input("Kérem a téglalap B oldalát: ")))

eredmeny=[]
eredmeny.append( 2*bekert[0]+2*bekert[1] )
eredmeny.append( bekert[0]*bekert[1] )

print("A téglalap kerülete: ", eredmeny[0])
print("A téglalap területe: ", eredmeny[1])