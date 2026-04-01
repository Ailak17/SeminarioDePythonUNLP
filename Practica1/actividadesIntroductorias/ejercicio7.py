#Escribe un programa que solicite al usuario una lista de palabras. Luego, construí una
#oración uniendo únicamente las palabras que tengan más de 3 letras, separadas por
# espacios. Las palabras cortas deben ser excluidas del resultado final.

entrada = input("Ingresa una lista de palabras separadas por espacios: ")

palabras = entrada.split()


palabras_filtradas = []


for p in palabras:
    if len(p) > 3:
        palabras_filtradas.append(p)


oracion_final = " ".join(palabras_filtradas)


print("Resultado")
print(f"Oración final: {oracion_final}")
