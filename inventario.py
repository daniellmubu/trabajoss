productos = []

cantidad = int(input("¿Cuántos productos deseas ingresar? "))

for i in range(cantidad):
    nombre = input(f"Ingrese el nombre del producto {i+1}: ")
    stock = int(input(f"Ingrese la cantidad disponible de {nombre}: "))
    productos.append([nombre, stock])

print("\nProductos disponibles en inventario:")
for producto in productos:
    if producto[1] > 0:
        print(producto[0], "-", producto[1], "unidades")
