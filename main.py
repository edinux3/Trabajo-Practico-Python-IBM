class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append({'tarea': tarea, 'completada': False})

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            del self.tareas[indice]
        else:
            print("¡Índice de tarea no válido!")

    def marcar_completada(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice]['completada'] = True
        else:
            print("¡Índice de tarea no válido!")

    def mostrar_tareas(self):
        print("\n--- Tareas Pendientes ---")
        for i, tarea in enumerate(self.tareas):
            if not tarea['completada']:
                print(f"{i + 1}. {tarea['tarea']}")

        print("\n--- Tareas Completadas ---")
        for i, tarea in enumerate(self.tareas):
            if tarea['completada']:
                print(f"{i + 1}. {tarea['tarea']}")


if __name__ == "__main__":
    lista_tareas = ListaTareas()
    
    while True:
        print("\n--- Lista de Tareas ---")
        lista_tareas.mostrar_tareas()
        print("\n1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Marcar tarea como completada")
        print("4. Visualizar tareas")
        print("5. Salir")
        
        opcion = input("\nIngrese el número de la opción que desea realizar: ")
        
        if opcion == '1':
            tarea = input("Ingrese la tarea a agregar: ")
            lista_tareas.agregar_tarea(tarea)
        elif opcion == '2':
            indice = int(input("Ingrese el número de la tarea que desea eliminar: ")) - 1
            lista_tareas.eliminar_tarea(indice)
        elif opcion == '3':
            indice = int(input("Ingrese el número de la tarea que desea marcar como completada: ")) - 1
            lista_tareas.marcar_completada(indice)
        elif opcion == '4':
            pass
        elif opcion == '5':
            print("¡Adiós!")
            break
        else:
            print("¡Opción no válida! Por favor ingrese una opción válida.")
