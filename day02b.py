# Írjunk egy függvényt, ami paraméterben kap 2 számot
# Majd az eredménnyel tér vissza a hívás helyére

def addition(num1: int, num2: int) -> int:
    return num1 + num2

num3 = addition(5, 8)
print(num3)

a = int(input("Adjon meg egy számot, de ne zenét: "))
b = int(input("Ezaz csináld még: "))

num4 = addition(a, b)
print()
print(num4)