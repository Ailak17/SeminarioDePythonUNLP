#Crea un programa que solicite al usuario un número y muestre su tabla de multiplicar
#del 1 al 10 utilizando un bucle for


numero = int(input("Introduce el numero a multiplicar: "))

for i in range(10) :
    print(f" {numero} x {i+1} = {numero * (i+1)}")

print(f"\n--- Tabla del {numero} ---")

# Usamos range(1, 11) para ir del 1 al 10 directamente
for i in range(1, 11):
    resultado = numero * i
    # Añadimos el "x" y el "=" para que sea una tabla bonita
    print(f"{numero} x {i} = {resultado}")