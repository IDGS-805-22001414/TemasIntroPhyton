#listas

lista1=[10,5,3]
lista2=[1,5,2,66,1.70,89.2]
lista3=["Lunes" , "Martes" , "Miercoles" ]
lista4=["JUan" , 45 , 1 , 92]

print(type(lista1))
print(len(lista1))

print(lista1[0])

x=0
suma=0
while x<len(lista1):
    suma=suma+lista1[x]
    x=x+1

print("La suma es : {}".format(suma)) # ????


print(lista1)
print(lista1[0])
lista1.append(100)
print(lista1)
print(lista1[3])

listas=[]

for x in range(5):
    valor=int(input("Ingresa valor:"))
    listas.append(valor)

    print(listas)

#Eliminar elementos de la lista
print(lista1)
lista1.pop()
print(lista1)


'''
Crear un programa para pedir una cantidad n de numeros y almacenerlos en un arreglo 
la salida debera ser la siguiente:
Lista completa : xxxxxxxx
Numeros pares de la lista  : aaaaaaa
Numeros Impares de la lista : rrrrr
'''

lista1.sort()#ordenar lista
print(lista1)
lista1.reverse()
print(lista1)

lista1.remove(10)
print(lista1) #?

lista1.clear()
print(lista1) #? 


