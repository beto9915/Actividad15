import os

def limpiar():
    os.system("cls")

def pausar():
    input("\nPresione Enter para continuar...")

estudiantes = {}
opcion = 0

while opcion != 4:
    limpiar()
    print("="*45)
    print("  SISTEMA DE REGISTRO DE ESTUDIANTES")
    print("="*45)
    print("1. Registrar Estudiante")
    print("2. Mostrar todos los estudiantes por cursos")
    print("3. Buscar estudiante por carnet")
    print("4. Salir")
    print("="*45)

    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        pausar()
        continue

    if opcion == 1:
        limpiar()
        carnet = input("Ingrese el número de carnet: ").strip()
        nombre = input("Ingrese el nombre del estudiante: ").strip()
        edad = int(input("Ingrese la edad: "))
        carrera = input("Ingrese la carrera: ").strip()

        cantCursos = int(input("Ingrese la cantidad de cursos: "))
        cursos = []
        for i in range(cantCursos):
            print(f"\nCurso {i+1}:")
            curso = input("Nombre del curso: ").strip()
            notaTarea = int(input("Nota tarea: "))
            notaParcial = int(input("Nota parcial: "))
            notaProyecto = int(input("Nota proyecto: "))
            cursos.append({
                "curso": curso,
                "notaTarea": notaTarea,
                "notaParcial": notaParcial,
                "notaProyecto": notaProyecto
            })

        estudiantes[carnet] = {
            "nombre": nombre,
            "edad": edad,
            "carrera": carrera,
            "cursos": cursos
        }

        print("\nEstudiante registrado con éxito.")
        pausar()

    elif opcion == 2:
        limpiar()
        if not estudiantes:
            print("No hay estudiantes registrados.")
        else:
            print("=== LISTA DE ESTUDIANTES ===\n")
            for carnet, datos in estudiantes.items():
                print(f"Carnet: {carnet}")
                print(f"Nombre: {datos['nombre']}")
                print(f"Edad: {datos['edad']}")
                print(f"Carrera: {datos['carrera']}")
                print("Cursos:")
                for idx, curso in enumerate(datos["cursos"], start=1):
                    print(f"  {idx}. {curso['curso']} - "
                          f"Tarea: {curso['notaTarea']}, "
                          f"Parcial: {curso['notaParcial']}, "
                          f"Proyecto: {curso['notaProyecto']}")
                print("-"*45)
        pausar()

    elif opcion == 3:
        limpiar()
        buscado = input("Ingrese carnet a buscar: ").strip()
        if buscado in estudiantes:
            datos = estudiantes[buscado]
            print(f"\nNombre: {datos['nombre']}")
            print(f"Edad: {datos['edad']}")
            print(f"Carrera: {datos['carrera']}")
            print("Cursos:")
            for idx, curso in enumerate(datos["cursos"], start=1):
                print(f"  {idx}. {curso['curso']} - "
                      f"Tarea: {curso['notaTarea']}, "
                      f"Parcial: {curso['notaParcial']}, "
                      f"Proyecto: {curso['notaProyecto']}")
        else:
            print("⚠ Estudiante no encontrado.")
        pausar()

    elif opcion == 4:
        print("Saliendo del sistema...")
    else:
        print("Opción inválida.")
        pausar()
