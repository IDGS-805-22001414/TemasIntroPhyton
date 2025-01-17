'''
Crear un programa para pedir una cantidad n de numeros y almacenerlos en un arreglo 
la salida debera ser la siguiente:
Lista completa : xxxxxxxx
Numeros pares de la lista  : aaaaaaa
Numeros Impares de la lista : rrrrr
'''

n = int(input("Ingrese la cantidad de números: "))
numeros = []

    
for i in range(n):
        numero = int(input(f"Ingrese el número {i+1}: "))
        numeros.append(numero)

    
print("Lista completa:", numeros)

    
pares = []
impares = []

    
for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

   
print("Números pares:", pares)
print("Números impares:", impares)


