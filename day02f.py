
def add(a, b):
    try:
        return a + b
    except:
        print("Müvelet nem végezhető el.")
        return 0        

#a = int(input('Adj meg egy számot: '))
#b = int(input('Adj meg még egy számot: '))

def get_number(msg: str):
    try:
        return int(input(msg))
    except Exception as e:
        print(e)
        print("Ez nem szám!")
        return get_number("Most már tényleg számot adjál meg gecó!")

a = get_number("Adjon meg egy számot: ")
b = get_number("Adjon meg még egy számot: ")

print(add(a,b))