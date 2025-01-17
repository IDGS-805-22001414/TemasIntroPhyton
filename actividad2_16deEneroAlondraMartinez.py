'''
----Actividad de calcular la distancia entre dos puntos ---
----Autor : Alondra Goretti Martinez Saldaña ---
'''
import math

def calcular_distancia(x1, y1, x2, y2):
  dx = x2 - x1
  dy = y2 - y1
  suma_cuadrados = dx**2 + dy**2
  distancia = math.sqrt(suma_cuadrados)
  return distancia

x1 = float(input("Ingresa el valor de x1 = "))
y1 = float(input("Ingresa el valor de y1 = "))
x2 = float(input("Ingresa el valor de x2 = "))
y2 = float(input("Ingresa el valor de y2 = "))

distancia = calcular_distancia(x1, y1, x2, y2)
print("La distancia entre puntos es de " ,distancia)
