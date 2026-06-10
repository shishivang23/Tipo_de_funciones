#8. Funcion que recibe y modifica una lista
def agregar_tarea(lisas_tareas, tarea):
    lisas_tareas.append(tarea)
    print(f"Tarea {tarea} agregada")

def mostrar_tareas(listas_tareas):
    if not listas_tareas:
        print("No hay tareas pendientes. ")
        return
    print("\nTareas pendientes: ")
    for i, tarea in enumerate (listas_tareas,1):
        print(f"  {i}.  {tarea}")

mis_tareas =[]
agregar_tarea(mis_tareas, "Estudia python")
agregar_tarea(mis_tareas, "Hacer ejecicio")
mostrar_tareas(mis_tareas)
