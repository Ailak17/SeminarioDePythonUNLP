#Escribe un programa que simule una caja registradora: el usuario ingresa precios de
#productos de a uno. Cuando ingresa 0, el programa se detiene y muestra el total
#acumulado. Nota: utilizá la sentencia break cuando haga falta.



total = 0

while True:
    precio = float(input("Ingresa el precio del producto: "))
    
    if precio == 0:
        break  # sale del while
    
    total += precio

print(f"El total de la compra es: ${total:.2f}")