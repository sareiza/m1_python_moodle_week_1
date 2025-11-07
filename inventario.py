while True:
    nombre = input("Ingresa el nombre del producto: ")

    if not nombre.isalpha():
        print("❌ Dato no válido para un nombre. Por favor ingrésalo nuevamente.")
        continue
    else:
        break

# -----------------------------------------------
# Solicitar al usuario el precio del producto
# Convertirlo a tipo float y validar que no sea negativo
# -----------------------------------------------
while True:
    try:
        precio = float(input("Ingresa el precio del producto: "))
        if precio < 0:
            print("❌ El precio no puede ser negativo. Por favor ingrésalo nuevamente.")
            continue
        break
    except ValueError:
        print("❌ Precio inválido. Ingresa un valor numérico correcto.")

# -----------------------------------------------
# Solicitar al usuario la cantidad del producto
# Convertirla a tipo int y validar que no sea negativa
# -----------------------------------------------
while True:
    try:
        cantidad = int(input("Ingresa la cantidad del producto: "))
        if cantidad < 0:
            print("❌ La cantidad no puede ser negativa. Por favor ingrésala nuevamente.")
            continue
        break
    except ValueError:
        print("❌ Cantidad inválida. Ingresa un valor numérico entero correcto.")

# -----------------------------------------------
# Calcular el costo total (precio * cantidad)
# -----------------------------------------------
costo_total = precio * cantidad

# -----------------------------------------------
# Mostrar resumen de la información ingresada
# -----------------------------------------------
print("\n------- Producto agregado correctamente -------")
print(f"Nombre del producto: {nombre}")
print(f"Precio unitario: ${precio:,.0f}")
print(f"Cantidad: {cantidad}")
print(f"Costo total: ${costo_total:,.0f}")