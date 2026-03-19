
total = 0

while True:
    precio = float(input("Ingresa el precio del producto: "))
    
    if precio == 0:
        break  # sale del while
    
    total += precio

print(f"El total de la compra es: ${total:.2f}")