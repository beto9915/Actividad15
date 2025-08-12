class Program:
    estudiantes={}
    opcion=0
    while opcion!=4:
        print("""1. Registrar Estudiante: 
                 2. Mostrar todos los estudiantes por sus cursos:
                 3. Buscar estudiante por carnet:
                 4. Salir""")
        opcion=int(input("Seleccione una opcion: "))
        try:
            if opcion==1:
                carnet=input("Ingrese el numero de carnet")
                nombre= input("Ingrese el nombre del estudiante: ")
                edad=int(input("Ingrese la edad: "))
                carrera=input("Ingrese la carrera: ")
                cantCursos=int(input("Ingrese la cantidad de cursos: "))
                for i in range(cantCursos):
                    codigoCurso=i+1
                    curso=input("Ingrese el nombre del curso: ")
                    notaTarea=int(input("Ingrese nota tarea: "))
                    notaParcial=int(input("Ingrese nota parcial: "))
                    notaProyecto=int(input("Ingrese la note del proyecto: "))
                    estudiantes[carnet]={"nombre" : nombre, "edad": edad, "carrera": carrera, "cursos": {"curso": curso, "notaTarea":notaTarea, "notaParcial": notaParcial, "notaProyecto": notaProyecto}}
                print("\nEstudiante registrado con exito...")
                input()
            elif opcion==2:
                print("============ESTUDIANTES REGISTRADOS===========")
                for carnet, datos in estudiantes.items():
                    print(f"""Carnet: {carnet}
Nombre: {datos["nombre"]}
Edad: {datos["edad"]}
Carrera: {datos["carrera"]}
Cursos: 
""")
                    for codigoCurso, var in datos["cursos"].items():
                        print(f"""Codigo de curso: {codigoCurso}
Nombre del curso: {var["curso"]}
Nota de Tarea: {var["notaTarea"]}
Nota de Parcial: {var["notaParcial"]}
Nota de Proyecto: {var["notaProyecto"]}""")


                input()
            elif opcion==3:
                buscado=input("Ingrese carnet a buscar: ")
                if buscado in estudiantes:
                    datos= estudiantes[buscado]






        except :
            print("Ocurrio un error, intente de nuevo...")