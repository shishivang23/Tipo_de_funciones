#9.Sistema completo integrado:
def validar_nota(nota):
    if nota>=1 and nota <=7:
        return True
    return False

def agregar_nota(notas, alumno, nota):
    if not validar_nota(nota):
        print("Nota invalida, Debe estar entre 1.0 y 7.0")
        return
    notas.append({"alumno":alumno, "nota":nota})
    print(f"Nota de {alumno} registrada")

def mostrar_promedio(notas):
    if not notas:
        print("Sin notas registradas.")
    total = 0
    for registro in notas:
        total += registro ["nota"]
    promedio = total/len(notas)
    print(f"Promedio del curso: {promedio:.1f}")

registro = []
agregar_nota(registro, "Ana", 6.5)
agregar_nota(registro, "Luis", 7.0)
agregar_nota(registro, "Pedro", 5.5)
mostrar_promedio(registro)