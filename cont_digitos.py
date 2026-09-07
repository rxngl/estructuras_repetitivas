print("CONTADOR DE DIGITOS")

numero = int(input("Ingresa un numero entero: "))

numero = abs(numero)

if numero == 0:
    cantidad = 1
else:
    cantidad = 0

    while numero > 0:
        numero = numero // 10
        cantidad += 1

print("El numero tiene", cantidad, "digitos.")
