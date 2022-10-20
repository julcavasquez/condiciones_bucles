import random
contador = 0
# Quiero que un entero
number = random.randint(1, 1000)
print("trampa", number)

while True:
    num = int(input("Ingrese un numero: "))

    if num == number:
        print("Adivinaste el numero", num)
        print("Número de intentos", contador)
        break
    elif num < number:
        print("Debes ingresar un numero mayor")
        contador += 1
    else:
        print("Debes ingresar un numero menor")
        contador += 1
