

#Calcular el mayor de dos números ingresados por teclado usando un operadorternario
def PrimerEjercicio():
    print("Calcula el mayor de dos números ingresados por teclado usando un operadorternario")
    primerValor = input("Ingresa el primer numero: ")
    segundoValor = input("Ingresa el segundo numero: ")
    calcularElMayor(primerValor, segundoValor)
    
def calcularElMayor(primerNumero,segundoNumero):
    print(f"El mayor numero entre {primerNumero} y {segundoNumero} es {primerNumero if primerNumero > segundoNumero else segundoNumero}")

#----------------------------------------------------------------------------------------------------------------------------------------#


#Buscar una palabra en una lista ingresada por teclado usando args y un operadorternario
def SegundoEjercicio():
    print("Busca una palabra en una lista ingresada por teclado usando args y un operadorternario")
    listaDePalabras = input("Ingresa varias palabras separadas por espacio: ").split()
    palabra = input("Ingresa la palabra a buscar: ")
    buscarPalabra(palabra, *listaDePalabras)
def buscarPalabra(palabra, *listaDePalabras):
    print(f"La palabra '{palabra}' {'esta en la lista' if palabra in listaDePalabras else 'no esta en la lista'}")

#----------------------------------------------------------------------------------------------------------------------------------------#


#Determinar si un número es par o impar
def TercerEjercicio():
    print("Determina si un número es par o impar")
    numero= int(input("ingresa el numero a analizar: ."))
    parOImpar(numero)
    
def parOImpar(numero):
    print(f"El numero ingresado es {'par' if numero % 2 == 0 else 'impar' }")

#----------------------------------------------------------------------------------------------------------------------------------------#


#Calcular el promedio de una lista de números usando args y un operador ternario
def CuartoEjercicio():
    print("Calcula el promedio de una lista de números usando args y un operador ternario")
    listadeNumeros = input("Ingresa los numeros separados por espacio: ").split()
    listadeNumeros = [int(x) for x in listadeNumeros]
    promedio(*listadeNumeros)

def promedio(*listadeNumeros):
    print(f"El promedio es {sum(listadeNumeros) / len(listadeNumeros) }")

#----------------------------------------------------------------------------------------------------------------------------------------#



#Imprimir un mensaje de error si no se pasan suficientes argumentos
def QuintoEjercicio():
    print("Imprime un mensaje de error si no se pasan suficientes argumentos")
    listaDeElementos = input("Ingresa los elementos separados por espacio: ").split()
    hayArgumentosNecesarios(*listaDeElementos)

def hayArgumentosNecesarios(*listaDeElementos):
        print(f"Los argumentos en la lista son {'suficientes' if len(listaDeElementos)+1 > 1 else'insuficientes'}")

#----------------------------------------------------------------------------------------------------------------------------------------#
#Ejecucion: Descomentar la linea
PrimerEjercicio()