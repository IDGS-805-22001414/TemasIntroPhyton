import os

def function1():
    os.system("cis")
    print("Dame dos numeros : ")
    num1=int(input("Primer numero: "))
    num2=int(input("Segundo numero: "))
    res=num1-num2
    print("La sume de {} + {} es {}".format(num1,num2,res))
    

def function2():
    print("Hola soy la funcion 2")

def run():
 os.system("cis")
print("Menu de opciones")
print("1. Suma de dos numeros")
print("2. Otra opcion")
print("3. Salir")
opcion = int(input("Ingrese una opcion"))
if opcion == 1:
    function1()

if opcion == 2 :
    function2()

if __name___ == "__main__":
 run()

op=int(input("Numero: "))
if op==1:
    function1()
else:
    function2()