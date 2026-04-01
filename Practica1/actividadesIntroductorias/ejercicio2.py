#Escribe un programa que solicite al usuario una cantidad de segundos y muestre
#cuántas horas, minutos y segundos equivalen. Por ejemplo, 3661 segundos son 1
#hora, 1 minuto y 1 segundo

total_segundos = int(input("Introduce la cantidad de segundos: "))

horas = total_segundos // 3600


segundos = total_segundos % 3600


minutos = segundos // 60


segundos_finales = segundos % 60

# Mostramos el resultado
print(f"{total_segundos} segundos equivalen a:")
print(f"{horas} hora(s), {minutos} minuto(s) y {segundos_finales} segundo(s)")