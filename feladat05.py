'''1. Hozzon létre egy fájlt feladat05.py néven.
2. Kérjen be a felhasználótól egy fájlnevet, kiterjesztéssel együtt.
3. Hozzon létre egy dictionary-t az alábbi kulcs-érték párokkal:
	txt : 'ASCII text file.'
	doc : 'Microsoft Word Document'
	xlsx : 'Microsoft Excel Document'
	exe : 'Windows x86 Executable'
	zip : 'File Archive'
4. A bekért adatnak megfelelően írja ki, hogy milyen fájlt adott be a felhasználó.
'''


filename = input("Adjon meg egy fájlnevet: ")

files = {
    "txt" : 'ASCII text file.',
	"doc" : 'MicrosofÚjra! t Word Document',
	"xlsx" : 'Microsoft Excel Document',
	"exe" : 'Windows x86 Executable',
	"zip" : 'File Archive'
}
try:
    data = filename.split('.')
    key = data[-1]

    print(f"Az ön által megadott fájl típusa: {files[key]}")
except:
    print('Ismeretlen fájltípus.')