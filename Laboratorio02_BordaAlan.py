# Borda Aguirre Alan Rafael
# Rodrigo Alejandro Vildoso 
# Adrian Oña Medrano 
# Evelin Erica Rodriguez Sanchez 
# Mia Noemi Tango Torres
# Romulo Vilchez Alcides Zorrilla 
# Alejandra Reyes Ortiz Perez

# Info: Agente simple  en entorno observable, sus movimientos se realizan de manera 
# aleatoria con la condicion de que persiga al objetivo,los 5 objetivos "monedas" se generan de manera aleatoria en el entorno 
# El agente percibe el entorno para poder desplazarse en el laberinto solo en los espacios asignados como permitidos 

import random
from tkinter import Y 

def crear_mapa_laberinto(numero_filas, numero_columnas, numero_paredes, numero_espacios, numero_monedas):
    # Se crea un mapa lleno de paredes
    mapa_laberinto = []
    numero_paredes_generadas = 0
    for fila in range(0, numero_filas):
        fila_mapa_laberinto = []
        for columna in range(0, numero_columnas):
            fila_mapa_laberinto.append('#')
        mapa_laberinto.append(fila_mapa_laberinto)

    #Se ubica aleatoriamente un punto de inicio y a partir de ese punto se llenan espacios
    numero_espacios_generados = 0
    fila_posicion_actual = random.randrange(numero_filas)
    columna_posicion_actual = random.randrange(numero_columnas)
    mapa_laberinto[fila_posicion_actual][columna_posicion_actual] = ' '
    numero_espacios_generados += 1

    Agente = Y
    ficha_fila = random.randrange(numero_filas)
    ficha_columnas = random.randrange(numero_columnas)
    mapa_laberinto[fila_posicion_actual][columna_posicion_actual] = 'Y'


    while numero_espacios_generados < numero_espacios:
        direccion = random.randrange(4)
        if direccion == 0 and fila_posicion_actual > 0:
            fila_posicion_actual -= 1
        elif direccion == 1 and fila_posicion_actual < numero_filas - 1:
            fila_posicion_actual += 1
        elif direccion == 2 and columna_posicion_actual > 0:
            columna_posicion_actual -= 1
        else:
            if columna_posicion_actual < numero_columnas - 1:
                    columna_posicion_actual += 1
            
        if mapa_laberinto[fila_posicion_actual][columna_posicion_actual] == '#':
            mapa_laberinto[fila_posicion_actual][columna_posicion_actual] = ' '
            if mapa_laberinto[fila_posicion_actual][columna_posicion_actual] == ' ':
              laberinto[numero_monedas] = "o"
            numero_espacios_generados += 1

    return mapa_laberinto

numero_filas = int(input('Introduzca el número de filas del laberinto: '))
numero_columnas = int(input('Introduzca el número de columnas del laberinto: '))
numero_paredes = int(input('Introduzca el número de paredes del laberinto: '))
numero_monedas = int(input('Introduzca el número de monedas del laberinto: '))
numero_espacios = numero_filas * numero_columnas - numero_paredes - numero_monedas

laberinto = crear_mapa_laberinto(numero_filas, numero_columnas, numero_paredes, numero_espacios,numero_monedas)

for fila_mapa_laberinto in laberinto:
    print(fila_mapa_laberinto)

# recorrer todo el vector
for index, value in enumerate(laberinto):
    for index2, value2 in enumerate(value):
        if value2 == 'Y':
            contadorx = index
            contadory = index2
            print("posicion en x: ", contadorx)
            print("posicion en y: ", contadory)
#random de 1 a 4
for i in range(10):
  n = random.randint(1,4)
  # movimiento hacia arriba : 1
  # movimiento hacia abajo : 2
  # movimiento hacia la izquierda : 3
  # movimiento hacia la derecha : 4
  # validar movimiento en la matriz
  if n == 1:
    print("movimiento hacia arriba")
    if(laberinto[contadorx-1][contadory] == ' '):
      laberinto[contadorx][contadory] = ' '
      laberinto[contadorx-1][contadory] = 'Y'
      contadorx = contadorx-1
  if n == 2:
    print("movimiento hacia abajo")
    if(laberinto[contadorx+1][contadory] == ' '):
      laberinto[contadorx][contadory] = ' '
      laberinto[contadorx+1][contadory] = 'Y'
      contadorx = contadorx+1

  if n == 3:
    print("movimiento hacia la izquierda")
    if(laberinto[contadorx][contadory-1] == ' '):
      laberinto[contadorx][contadory] = ' '
      laberinto[contadorx][contadory-1] = 'Y'
      contadory = contadory-1

  if n == 4:
    print("derecha")
    if(laberinto[contadorx][contadory+1] == ' '):
      laberinto[contadorx][contadory] = ' '
      laberinto[contadorx][contadory+1] = 'Y'
      contadory = contadory+1

  for fila_mapa_laberinto in laberinto:
    print(fila_mapa_laberinto)