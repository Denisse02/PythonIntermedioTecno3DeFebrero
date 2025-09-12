#Ejercicio 1
dividir_Por_()
#Ejercicio 2
#sumarNumeroYCadena()
#Ejercicio 3
#accederConClaveInexistente()
#Ejercicio 4
#abrirArchivo()
#Ejercicio 5
#dividir_Por_VerficandoValidez()
"""
Escribe un programa que intente dividir dos números.
Si el segundo número es cero,captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.
"""
def dividir_Por_():
    print("Inserta el primer valor a dividir")
    a = input()
    print("Inserta el primer valor a dividir")
    b = input()
    
    try:
        resultado = a / b
        print("El resultado es:", resultado)
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
"""
Escribe un programa que intente sumar un número y una cadena. Si se produce un error
de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.
"""
def sumarNumeroYCadena():
    try:
        numero = input("Ingresa un número: ")
        texto = input("Ingresa un texto: ")
        resultado = numero + texto
        print("El resultado es:", resultado)
    except TypeError:
        print("Eror: No se puede sumar un número con una cadena.")
"""
Escribe un programa que intente acceder a una clave que no existe en un
diccionario. Si se produce una excepción KeyError, captura la excepción y muestra
"""
def accederConClaveInexistente():
    diccionario = {"nombre": "Denisse", "edad": 23}

    try:
        clave = input("Ingresa la clave: ")
        valor = diccionario[clave]
        print("El valor de la clave es:", valor)
    except KeyError:
        print("Eror: La clave '{clave}' no existe en el diccionario.")
"""
Escribe un programa que intente abrir un archivo que no existe.
Si se produce una excepción FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario.
Sin embargo, también intenta crear el archivo si no existe
"""
def abrirArchivo():
    archivo_prueba = "archivo_inexistente.txt"
    
    try:
        with open(archivo_prueba, "r") as f:
            contenido = f.read()
            print("Contenido del archivo:")
            print(contenido)
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_prueba}' no existe.")
        print("Creando el archivo...")

        with open(archivo_prueba, "w") as f:
            f.write("Este es un archivo nuevo creado automáticamente.\n")
        print(f"El archivo '{archivo_prueba}' fue creado.")
"""
Escribe un programa que intente dividir dos números. Si el segundo número es cero,
captura la excepción ZeroDivisionError. Si el primer número es un número no válido,
captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario
"""
def dividir_Por_VerficandoValidez():
    try:
        a = int(input("Inserta el primer valor a dividir: "))
        b = int(input("Inserta el segundo valor a dividir: "))
        
        resultado = a / b
        print("El resultado es:", resultado)

    except ValueError:
        print("Error: Debes ingresar un número válido.")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")