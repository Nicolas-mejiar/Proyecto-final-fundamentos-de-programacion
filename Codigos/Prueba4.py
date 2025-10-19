import pandas as pd #Libreria para tabular los datos 
import os #Libreria para limpiar pantalla
import time #Libreria para usar el tiempo
from tabulate import tabulate #Libreria para diseñar las tablas (Solo se importa la funcion principal)

#Funcion para limpiar pantalla
def limpiar_Pantalla():
    # Determina el sistema operativo y ejecuta el comando de limpieza 
    if os.name == 'nt': # 'nt' es para Windows
        os.system('cls')
    else: # 'posix' es para Linux/macOS
        os.system('clear')

# Función para ingresar datos de los equipos
def datos_Equipos(datos):
    cantidad = int(input("Cuantos equipos va a ingresar: "))
    for i in range(cantidad):
        print("Ingrese los datos del equipo",(i + 1))
        nombre = input("Nombre del equipo: ")
        PJ = int(input("Partidos jugados: "))
        PG = int(input("Partidos ganados: "))
        PE = int(input("Partidos empatados: "))
        PP = int(input("Partidos perdidos: "))
        GF = int(input("Goles a favor: "))
        GC = int(input("Goles en contra: "))
        DG = GF - GC   # Diferencia de goles
        Puntos = (PG * 3) + (PE * 1)
        Prom_Victorias = (PG/PJ) * 100
        TA = int(input("Tarjetas amarillas: "))
        TR = int(input("Tarjetas rojas: "))
        Dt = input("Entrenador: ")
        Estadio = input("Estadio: ")
        Temporada = "2024/2025"
        datos.append((nombre,PJ, PG, PE, PP, GF, GC, DG, Puntos, Prom_Victorias, TA, TR, Dt, Estadio, Temporada))
        limpiar_Pantalla() #Limpia Pantalla

#Funcion para imprimir la tabla con las lineas y el texto centrado
def imprimir_Tabla(df):
    print(tabulate(
        df,
        headers='keys',         # Usa los nombres de las columnas
        tablefmt='fancy_grid',  # Estilo de tabla con bordes
        showindex=False,        # Oculta los números del índice
        stralign='center',      # Centra los textos
        numalign='center'       # Centra los números
    ))

# Función para generar diferentes tablas usando pandas
def generar_tablas(datos):
    columnas = ["EQUIPO","PJ", "PG", "PE", "PP", "GF", "GC", "DG", "PUNTOS",
                "% VICTORIAS", "TARJETAS AMARILLAS", "TARJETAS ROJAS",
                "ENTRENADOR", "ESTADIO", "TEMPORADA"]
    df = pd.DataFrame(datos, columns=columnas)
    
    print("\nTabla original:")
    imprimir_Tabla(df)
    
    print("\nTabla ordenada por PUNTOS (de mayor a menor):")
    imprimir_Tabla(df.sort_values(by='PUNTOS', ascending=False))

    print("\nEquipos con más de 10 puntos:")
    imprimir_Tabla(df[df['PUNTOS'] > 10])

    print("\nEquipos con porcentaje de victorias mayor al 50%:\n")
    imprimir_Tabla(df[df['% VICTORIAS'] > 50])


    print("\nTabla con columnas seleccionadas (PUNTOS, ENTRENADOR, TEMPORADA):\n")
    imprimir_Tabla(df[['PUNTOS', 'ENTRENADOR', 'TEMPORADA']])
    
# Programa Principal
datos = []

# Llamada a la función para ingresar datos
datos_Equipos(datos)
time.sleep(1) #Espera un segundo
limpiar_Pantalla() #Limpia Pantalla

# Mostrar las tablas con pandas
generar_tablas(datos)