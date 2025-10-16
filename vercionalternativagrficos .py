import pandas as pd
import matplotlib.pyplot as plt
import os  # Importamos os para limpiar pantalla

# -----------------------------------------------------------
# Función para limpiar pantalla
# -----------------------------------------------------------
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')  
def datos_Equipos():
    equipos = []
    datos = []
    cantidad = int(input("¿Cuántos equipos vas a ingresar?: "))

    for i in range(cantidad):
        limpiar_pantalla() 
        print(f"\n=== Equipo #{i+1} ===")
        nombre = input("Nombre del equipo: ")
        PJ = int(input("Partidos jugados: "))
        PG = int(input("Partidos ganados: "))
        PE = int(input("Partidos empatados: "))
        PP = int(input("Partidos perdidos: "))
        GF = int(input("Goles a favor: "))
        GC = int(input("Goles en contra: "))
        DG = GF - GC
        Puntos = (PG * 3) + (PE * 1)
        Prom_Victorias = round((PG / PJ) * 100, 2)
        TA = int(input("Tarjetas amarillas: "))
        TR = int(input("Tarjetas rojas: "))
        Dt = input("Entrenador: ")
        Estadio = input("Estadio: ")
        Temporada = "2023/2024"

        equipos.append(nombre)
        datos.append((PJ, PG, PE, PP, GF, GC, DG, Puntos, Prom_Victorias, TA, TR, Dt, Estadio, Temporada))

    return equipos, datos


# Función para construir la tabla con pandas

def construir_tabla(equipos, datos):
    columnas = [
        "Equipo", "PJ", "PG", "PE", "PP", "GF", "GC", "DG",
        "Puntos", "%Victorias", "TA", "TR", "Entrenador", "Estadio", "Temporada"
    ]
    filas = []

    for i in range(len(equipos)):
        fila = [equipos[i]] + list(datos[i])
        filas.append(fila)

    tabla = pd.DataFrame(filas, columns=columnas)

    # Ordenar por puntos de mayor a menor
    tabla = tabla.sort_values(by="Puntos", ascending=False).reset_index(drop=True)
    tabla.index += 1
    return tabla
# Función para mostrar tabla y guardar archivo
def mostrar_y_guardar(tabla):
    print("\n=== TABLA DE POSICIONES PREMIER LEAGUE 2023/2024 ===")
    print(tabla.to_string(index=True))

    # Guardar en CSV
    tabla.to_csv("tabla_premier_2324.csv", index=False, encoding="utf-8-sig")
    print("\n Datos guardados en 'tabla_premier_2324.csv' correctamente.")
# Función opcional: gráfico de puntos
def graficar(tabla):
    plt.figure(figsize=(10, 6))
    plt.bar(tabla["Equipo"], tabla["Puntos"], color="royalblue")
    plt.xticks(rotation=45, ha="right")
    plt.title("Puntos por equipo - Premier League 2023/2024")
    plt.ylabel("Puntos")
    plt.tight_layout()
    plt.show()
# Programa principal
def main():
    while True:
        limpiar_pantalla()
        print("===== PROYECTO: PREMIER LEAGUE 2023/2024 =====")
        equipos, datos = datos_Equipos()
        tabla = construir_tabla(equipos, datos)
        limpiar_pantalla() 
        mostrar_y_guardar(tabla)

        opcion = input("\n¿Deseas ver un gráfico de puntos? (s/n): ").lower()
        if opcion == "s":
            graficar(tabla)

        continuar = input("\n¿Deseas ingresar más equipos? (s/n): ").lower()
        if continuar != "s":
            print("\nFin del programa.")
            break

# Ejecutar
if __name__ == "__main__":
    main()

