#Escribe un programa que solicite al usuario su año de nacimiento y muestre en qué
#año cumplirá 18, 21 y 100 años.

entrada = input("Introduce tu año de nacimiento: ")

nacimiento = int(entrada)

print("Cumplirás 18 años en el:", nacimiento + 18)
print("Cumplirás 21 años en el:", nacimiento + 21)
print("Cumplirás 100 años en el:", nacimiento + 100)