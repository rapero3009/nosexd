# def generar_lista_enteros():
    
#     inicio = int(input("Ingresa el primer número: "))
#     fin = int(input("Ingresa el segundo número: "))

    
#     lista = list(range(inicio, fin + 1))

    
#     print("La lista generada es:", lista)

# generar_lista_enteros()







def generar_lista_enteros():
    
    inicio = int(input("Ingresa el primer número: "))
    fin = int(input("Ingresa el segundo número: "))

   
    lista = list(range(inicio, fin + 1))

    
    print("La lista generada es:", lista)


generar_lista_enteros()


def contar_caracteres():
    # Pedir al usuario que ingrese la cadena
    cadena = input("Ingresa una cadena de texto: ")
    
    # Pedir al usuario que ingrese el carácter
    caracter = input("Ingresa el carácter que deseas contar: ")
    
    # Asegurarse de que el carácter sea un solo carácter
    if len(caracter) != 1:
        print("Por favor, ingresa un solo carácter.")
        return
    
    # Contar la cantidad de veces que aparece el carácter en la cadena
    cantidad = cadena.lower().count(caracter.lower())
    
    # Mostrar el resultado
    print(f"El carácter '{caracter}' aparece {cantidad} veces en la cadena.")

# Llamar a la función
contar_caracteres()

def es_primo(num):
    # Función auxiliar para verificar si un número es primo
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def numeros_primos_entre():
    # Pedir al usuario que ingrese los dos números
    inicio = int(input("Ingresa el primer número: "))
    fin = int(input("Ingresa el segundo número: "))

    # Generar la lista de números primos entre inicio y fin
    primos = [num for num in range(inicio + 1, fin) if es_primo(num)]

    # Mostrar el resultado
    print(f"Los números primos entre {inicio} y {fin} son: {primos}")

# Llamar a la función
numeros_primos_entre()


def todos_pares():
    # Pedir al usuario que ingrese una lista de números separados por comas
    entrada = input("Ingresa una lista de números separados por comas: ")
    
    # Convertir la entrada en una lista de enteros
    lista = [int(num) for num in entrada.split(",")]
    
    # Verificar si todos los números en la lista son pares
    todos_pares = all(num % 2 == 0 for num in lista)
    
    # Mostrar el resultado
    print(f"¿Todos los números en la lista son pares? {todos_pares}")

# Llamar a la función
todos_pares()

def es_primo(num):
    # Función auxiliar para verificar si un número es primo
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def todos_primos():
    # Pedir al usuario que ingrese una lista de números separados por comas
    entrada = input("Ingresa una lista de números separados por comas: ")
    
    # Convertir la entrada en una lista de enteros
    lista = [int(num) for num in entrada.split(",")]
    
    # Verificar si todos los números en la lista son primos
    todos_primos = all(es_primo(num) for num in lista)
    
    # Mostrar el resultado
    print(f"¿Todos los números en la lista son primos? {todos_primos}")

# Llamar a la función
todos_primos()



 def calculadora():
    while True:
        # Mostrar el menú de opciones
        print("\n--- Calculadora ---")
        print("a. Suma")
        print("b. Resta")
        print("c. Multiplicación")
        print("d. División")
        print("e. Potencia")
        print("SALIR. Cerrar calculadora")
        
        # Pedir al usuario que elija una opción
        opcion = input("Elige una opción: ").strip().lower()
        
        # Salir si el usuario elige "SALIR"
        if opcion == "salir":
            print("¡Gracias por usar la calculadora! ¡Hasta luego!")
            break
        
        # Pedir los números si no es "SALIR"
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Error: Ingresa números válidos.")
            continue
        
        # Realizar la operación seleccionada
        if opcion == "a":
            print(f"Resultado de la suma: {num1 + num2}")
        elif opcion == "b":
            print(f"Resultado de la resta: {num1 - num2}")
        elif opcion == "c":
            print(f"Resultado de la multiplicación: {num1 * num2}")
        elif opcion == "d":
            if num2 == 0:
                print("Error: No se puede dividir entre cero.")
            else:
                print(f"Resultado de la división: {num1 / num2}")
        elif opcion == "e":
            print(f"Resultado de la potencia: {num1 ** num2}")
        else:
            print("Opción no válida. Intenta de nuevo.")

# Llamar a la función de la calculadora
calculadora()

def es_palindromo():
    # Pedir al usuario que ingrese una cadena
    cadena = input("Ingresa una cadena para verificar si es un palíndromo: ")
    
    # Convertir la cadena a minúsculas y eliminar espacios
    cadena = cadena.lower().replace(" ", "")
    
    # Verificar si la cadena es igual a su inversa
    es_palindromo = cadena == cadena[::-1]
    
    # Mostrar el resultado
    print(f"¿La cadena '{cadena}' es un palíndromo? {es_palindromo}")

# Llamar a la función
es_palindromo()

def es_numero_armstrong():
    # Pedir al usuario que ingrese un número
    numero = input("Ingresa un número para verificar si es un número Armstrong: ")
    
    # Convertir la entrada a un número entero
    try:
        numero = int(numero)
    except ValueError:
        print("Error: Ingresa un número válido.")
        return
    
    # Calcular la suma de los cubos de los dígitos
    suma_cubos = sum(int(digito) ** 3 for digito in str(numero))
    
    # Verificar si es un número Armstrong
    es_armstrong = suma_cubos == numero
    
    # Mostrar el resultado
    print(f"¿El número {numero} es un número Armstrong? {es_armstrong}")

# Llamar a la función
es_numero_armstrong()