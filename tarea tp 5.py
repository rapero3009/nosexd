def redondear(numero):
    parte_decimal = numero - int(numero)  # Obtener la parte decimal
    if parte_decimal > 0.5:
        return int(numero) + 1  # Redondear hacia arriba
    else:
        return int(numero)  # Redondear hacia abajo
    
    # redondeo/redondeo.py
def redondear(numero):
    """
    Redondea un número decimal según el criterio:
    - Si la parte decimal es mayor que 0.5, devuelve el entero siguiente.
    - Si la parte decimal es menor o igual a 0.5, devuelve el entero anterior.
    """
    parte_entera = int(numero)  # Obtener la parte entera del número
    parte_decimal = numero - parte_entera  # Obtener la parte decimal

    if parte_decimal > 0.5:
        return parte_entera + 1  # Redondear hacia arriba
    else:
        return parte_entera  # Redondear hacia abajo
    
    # main.py
from redondeo.redondeo import redondear  # Importar la función redondear del paquete

def suma_redondeada(*numeros):
    """
    Suma una lista de números y redondea el resultado usando la función redondear().
    """
    suma = sum(numeros)  # Sumar todos los números
    return redondear(suma)  # Redondear el resultado

# Ejemplo de uso
if _name_ == "_main_":
    resultado = suma_redondeada(3.5, 2.4, 1.2)
    print("Resultado redondeado:", resultado)  # Salida: 7


from datetime import datetime

# Obtener la fecha y hora actuales
fecha_hora_actual = datetime.now()

# Formatear la fecha y hora en un formato legible
fecha_hora_formateada = fecha_hora_actual.strftime("%Y-%m-%d %H:%M:%S")

# Mostrar la fecha y hora actuales
print("Fecha y hora actuales:", fecha_hora_formateada)

import random

def generar_par_aleatorio():
    numeros_pares = [2, 4, 6, 8, 10]
    return random.choice(numeros_pares)

# Prueba en ciclo infinito
if _name_ == "_main_":
    while True:
        print("Número par al azar entre 2 y 10:", generar_par_aleatorio())
        input("Presiona Enter para generar otro número...")  # Pausa para ver el resultado


import random

def bola_magica():
    """
    Simula una Bola Mágica (Magic 8 Ball) que responde con una de 8 respuestas posibles.
    """
    respuestas = [
        "Es seguro que sí",
        "Las chances son buenas",
        "Puedes contar con ello",
        "Pregúntame de nuevo más tarde",
        "Concéntrate y pregunta de nuevo",
        "No veo con claridad, intenta de nuevo",
        "Mi respuesta es no",
        "Mis fuentes me dicen que no"
    ]
    return random.choice(respuestas)  # Selecciona una respuesta al azar

# Ejemplo de uso
if _name_ == "_main_":
    input("Haz tu pregunta: ")  # El usuario hace una pregunta
    print("La Bola Mágica dice:", bola_magica())


if _name_ == "_main_":
    while True:
        input("Haz tu pregunta (o escribe 'salir' para terminar): ")
        print("La Bola Mágica dice:", bola_magica())
        print()  # Espacio para mejor legibilidad


