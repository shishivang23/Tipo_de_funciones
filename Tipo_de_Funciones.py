#1. Función sin parametro
def saludar():
    print("Hola! Bienvnido.")
          
saludar()

#2. Función con parametros
def saludar_usuario(nombre):
    print(f"¡Hola, {nombre} ! Bienvenido.")

saludar_usuario("Ana")
saludar_usuario("Luis")

#3. Función con Retorno.
def sumar(a,b):
    resultado = a + b
    return resultado
total = sumar(5,3)
print(f"La suma es: {total}")
print(sumar(10,20))

#4. Parametros con valor por defecto:
def crear_usuario(nombre, rol="estudiante"):
    print(f"Usuario: {nombre} | Rol: {rol}")

crear_usuario("Maria")
crear_usuario("Pedro", "administrador")
crear_usuario("Laura", rol="docente")

#5. Funcion de validación:
def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    return False

edad = int(input("Ingresa tu edad: "))
if es_mayor_de_edad(edad):
    print("Acceso permitido.")
else:
    print("Acceso denegado.")

#Funcion de validacion compuesta:
def validar_contrasena(contrasena):
    if len(contrasena) < 8:
        return False, "Mínimo 8 caracteres"
    tiene_numero = False
    for caracter in contrasena:
        if caracter.isdigit():
            tiene_numero = True
    if not tiene_numero:
        return False, "Debe contener al menos un número"
    return True, "Contraseña valida"
clave = input("Crea tu contraseña: ")
valida, mensaje = validar_contrasena(clave)
print (mensaje)