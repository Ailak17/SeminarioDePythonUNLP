
#Modifica el ejercicio 4 para que, en lugar de imprimir los números, genere dos listas:
#una con los múltiplos de 5 y otra con el resto de los números. Imprimí ambas listas al
#finalizar.


numero = int(input("Introduce hasta qué número quieres procesar: "))


multiplos_de_5 = []
otros_numeros = []


for i in range(1, numero + 1):
    if i % 5 == 0:

        multiplos_de_5.append(i)
    else:

        otros_numeros.append(i)

print(f"Múltiplos de 5 encontrados: {multiplos_de_5}")
print(f"Resto de los números: {otros_numeros}")