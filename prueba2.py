import pandas as pd
import os #Libreria para limpiar pantalla
import time #Libreria para usar el tiempo

#Funcion para limpiar pantalla
def limpiar_Pantalla():
    # Determina el sistema operativo y ejecuta el comando de limpieza 
    if os.name == 'nt': # 'nt' es para Windows
        os.system('cls')
    else: # 'posix' es para Linux/macOS
        os.system('clear')

# Función para ingresar datos de los equipos
def datos_Equipos(equipos, datos):
    global cantidad
    contador = 0
    cantidad = int(input("Cuantos equipos va a ingresar: "))
    while contador < cantidad:
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
        Temporada = "2023/2024"
        equipos.append(nombre)
        datos.append((PJ, PG, PE, PP, GF, GC, DG, Puntos, Prom_Victorias, TA, TR, Dt, Estadio, Temporada))
        contador += 1
        limpiar_Pantalla() #Limpia Pantalla

# Función para generar diferentes tablas usando pandas
def generar_tablas(equipos, datos):
    columnas = ["PJ", "PG", "PE", "PP", "GF", "GC", "DG", "PUNTOS",
                "% VICTORIAS", "TARJETAS AMARILLAS", "TARJETAS ROJAS",
                "ENTRENADOR", "ESTADIO", "TEMPORADA"]
    df = pd.DataFrame(datos, columns=columnas, index=equipos)
    
    print("\n" + "="*80)
    print("\nTabla original:")
    print(df)
    print("="*80)
    
    print("\nTabla ordenada por PUNTOS (de mayor a menor):")
    print(df.sort_values(by='PUNTOS', ascending=False))
    print("="*80)

    print("\nEquipos con más de 10 puntos:")
    print(df[df['PUNTOS'] > 10])
    print("="*80)

    print("\nEquipos con porcentaje de victorias mayor al 50%:")
    print(df[df['% VICTORIAS'] > 50])
    print("="*80)

    print("\nTabla con columnas seleccionadas (PUNTOS, ENTRENADOR, TEMPORADA):")
    print(df[['PUNTOS', 'ENTRENADOR', 'TEMPORADA']])
    print("="*80)
    
# Programa Principal
equipos = []
datos = []

# Llamada a la función para ingresar datos
datos_Equipos(equipos, datos)
time.sleep(1) #Espera un segundo
limpiar_Pantalla() #Limpia Pantalla

# Mostrar las tablas con pandas
generar_tablas(equipos, datos)
