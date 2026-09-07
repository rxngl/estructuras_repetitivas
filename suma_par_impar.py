print("SUMA DE PARES E IMPARES")

n = int(input("Ingresa un numero: "))

suma_pares = 0
suma_impares = 0

for numero in range(1, n + 1):
    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero

print("Suma de los numeros pares:", suma_pares)
print("Suma de los numeros impares:", suma_impares)
