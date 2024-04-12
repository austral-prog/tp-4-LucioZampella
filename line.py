def line():
import math
coef_a = float(input("Ingrese el coeficiente A: "))
coef_b = float(input("Ingrese el coeficiente B: "))
coef_X1 = float(input("Ingrese el coeficiente X1: "))
coef_X2 = float(input("Ingrese el coeficiente X2 "))

print(f"El coeficiente A de su ecuacion es: {coef_a}")
print(f"El coeficiente B de su ecuacion es: {coef_b}")
print(f"El coeficiente X1 de su ecuacion es: {coef_X1}")
print(f"El coeficiente X2 de su ecuacion es: {coef_X2}")

print(f"Para la siguiente ecuacion:\n{coef_a} + {coef_b}")

print(f"Dado los siguientes puntos:\nP1 {coef_X1, coef_a*coef_X1 + coef_b} ")
print(f"P1 {coef_X2, coef_a*coef_X2 + coef_b} ")

print(f"La distancia entre ellos es:" , math.dist([coef_X1, coef_a*coef_X1 + coef_b] , [coef_X2, coef_a*coef_X2 + coef_b]))
