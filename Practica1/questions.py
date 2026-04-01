import random
'''words = [
    "python",
    "programa",
    "variable",
    "funcion",
    "bucle",
    "cadena",
    "entero",
    "lista",
]'''
categorias = {
    'Programacion': ['python' , 'variable' , 'cadena' , 'entero'],
    'Sofware': ['teclado', 'mouese' , 'monitor'],
    'Videojuegos': ['counter', 'lol', 'valorant', 'minecraft']
}


print("¡Bienvenido al Ahorcado!")
print()


print("Categorías disponibles:")
for nombre in categorias.keys():
    print(f"- {nombre}")

seleccion = input("Elegí una categoría: ").capitalize()

word = random.choice(categorias[seleccion])
guessed = []
attempts = 6
puntos = 0

while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)
    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        print("¡Ganaste!")
        puntos += 6
        break

    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    letter = input("Ingresá una letra: ").lower() #paso a minusculas por que no tomaba mayus sino
    #inciso A: Modificar para que los intentos sean letras
    if len(letter) != 1 or not letter.isalpha(): 
        print("Entrada no valida")
        print()
        continue
    
    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        puntos-=1
        attempts -= 1
        print("Esa letra no está en la palabra.")
    print()
else:
    print(f"¡Perdiste! La palabra era: {word}")
    puntos = 0
print(f"Tu puntaje final es: {puntos}")