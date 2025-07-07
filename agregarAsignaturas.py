asignaturaList = []
pedirCantidad = int(input("cuantas materias quieres agregar: "))
for i in range(pedirCantidad):
    asignaturas =input(f"ingrese la materia {i+1}:")
    asignaturaList.append(asignaturas)
print("\n Las materias que agregaste son:")
for n in asignaturaList:
    print("-",n)