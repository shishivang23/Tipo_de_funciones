#7. Función para menú:
def mostrar_menu():
    print("\n=== MENU PRINCIPAL ===")
    print("1.Ver Producto")
    print("2.Agregar producto")
    print("3.Salir")

def ver_productos():
    print("Lista de productos: [Vacía]")

def agregar_productos():
    nombre = input("Nombre del prodcuto")
    print(f"{nombre} agregado correctamente")

def ejecutar_menu():
    while True:
        mostrar_menu()
        opcion = input("elige una opción ")
        if opcion=="1":
            ver_productos()
        elif opcion=="2":
            agregar_productos
        elif opcion=="3":
            print("Hasta pronto")
            break
        else:
            print("Opción incorrecta")
ejecutar_menu()

