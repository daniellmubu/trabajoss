asignaturas = []
calificaciones = []
materias = int(input("cuantas materias vas a agregar"))

for i in range (materias):
    agregar = input("que materia piensa agregar")
    asignaturas.append (agregar)

for i in range (materias):
    calificacion = float(input("ingrese sus calificaciones en orden"))
    calificaciones.append(calificacion)
    boletin =dict(zip(asignaturas, calificaciones))

eliminar = [materia for materia, nota in boletin.items() if nota >= 6]

for clave in eliminar:
    boletin.pop(clave)
print("estas son todas las materias que debe recuperar", boletin)