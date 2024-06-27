# Escribe una función que reciba una lista de números y devuelva la suma de todos sus elementos

def suma_elementos(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

# Prueba la función
numeros = [1, 2, 3, 4, 5]
print(f"La suma de los elementos es: {suma_elementos(numeros)}")

# Escribe una función que reciba una lista de números y devuelva el número más grande.

def numero_mas_grande(lista):
    mayor = lista[0]
    for numero in lista:
        if numero > mayor:
            mayor = numero
    return mayor

# Prueba la función
numeros = [1, 2, 3, 4, 5]
print(f"El número más grande es: {numero_mas_grande(numeros)}")

#Escribe una función que reciba una lista y devuelva la cantidad de elementos en la lista.

def cuenta_elementos(lista):
    contador = 0
    for _ in lista:
        contador += 1
    return contador

# Prueba la función
numeros = [1, 2, 3, 4, 5]
print(f"La cantidad de elementos es: {cuenta_elementos(numeros)}")

# Escribe una función que reciba una lista de números y devuelva la media (promedio) de sus elementos

def media_elementos(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma / len(lista)

# Prueba la función
numeros = [1, 2, 3, 4, 5]
print(f"La media de los elementos es: {media_elementos(numeros)}")

# Imprimir elementos de una lista
# Declara una lista de números del 1 al 5 e imprime cada elemento de la lista

numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    print(numero)

# Suma de elementos de una lista
# Declara una lista de números y calcula la suma de todos sus elementos. Imprime el resultado.

numeros = [1, 2, 3, 4, 5]
suma_total = sum (numeros)
print("La suma de todos los elementos es: ", suma_total)

# Declarar y usar variables
# Declara una variable con tu nombre y otra con tu edad.
# Luego, imprime un mensaje que diga "Mi nombre es [nombre] y tengo [edad] años".

nombre = "María"
edad = (33)
print(f"Mi nombre es {nombre} y tengo {edad} años")

# Funciones para operaciones matemáticas
#Crea una función llamada multiplicar que tome dos parámetros y
#devuelva su producto. Usa la función para multiplicar 6 por 7 y muestra el resultado.

def multiplicar(a, b):
    return a * b

resultado = multiplicar(6, 7)
print(f"El resultado de multiplicar 6 por 7 es: {resultado}")

#Filtrar elementos en una lista
#Declara una lista de números del 1 al 10 y crea una nueva lista que
#contenga solo los números pares. Imprime la nueva lista.

lista_numero = [1, 2, 3, 4, 5,6,7,8,9,10]
lista_par = [2, 4, 6, 8, 10]
print (lista_par)

#Ejercicio 1: Imprimir un Mensaje
#Enunciado: Escribe un programa que imprima "Hola, mundo!"

print ("Hola Mundo")

#Declarar Variables
#Enunciado: Declara una variable nombre con tu nombre y una variable edad con tu edad. 
#Luego, imprime estos valores.

nombre = "Maria Jose"
edad = 33
print ("Mi nombre es: ",nombre)
print ("Mi edad es: ", edad)

#Ejercicio 3: Sumar dos Números
#Enunciado: Declara dos variables con los valores 10 y 20, y luego imprime su suma.

a = 10
b = 20
suma = a + b

print (suma)

#Ejercicio 4: Condicionales
#Enunciado: Escribe un programa que verifique si un número es positivo.
#Si el número es positivo, imprime "El número es positivo".

# Solución
numero = 9  # Puedes cambiar este valor para probar con otros números

if numero > 0:
    print("El número es positivo")

#Ejercicio 5: Bucles
#Enunciado: Usa un bucle for para imprimir los números del 1 al 5.

for i in (1,5):
    print (i)

# Solución
def primer_elemento(lista):
    return lista[0]

# Llamar a la función
mi_lista = [10, 20, 30]
print("El primer elemento de la lista es:", primer_elemento(mi_lista))

#Define una función llamada sumar que acepte dos parámetros y devuelva su suma.
#Llama a la función con los números 5 y 7, y almacena el resultado en una variable.
#Imprime el resultado.

def sumar (a,b):
    return a + b

resultado = sumar (5,7)
print (resultado)

#Define una función llamada calcular_promedio que acepte una lista de números y devuelva su promedio.
#Llama a la función con la lista [10, 20, 30, 40, 50] y almacena el resultado en una variable.
#Imprime el resultado

def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)
print(calcular_promedio([10,20,30,40,50]))

def suma(a, b):
    return a + b
resultado = suma(5 , 8)
print(resultado)



























    

    
    
    

    


    
