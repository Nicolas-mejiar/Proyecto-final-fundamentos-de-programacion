import pandas as pd

# =========================================
# FUNCIÓN: INGRESAR DATOS DE LOS EQUIPOS
# =========================================
def datos_equipos():
    equipos = []
    datos = []

    cantidad = int(input("¿Cuántos equipos vas a ingresar?: "))

    for i in range(cantidad):
        print(f"\n=== Equipo {i+1} de {cantidad} ===")

        # Entrada de datos básicos
        nombre = input("Nombre del equipo: ").strip()
        PJ = int(input("Partidos jugados (PJ): "))
        PG = int(input("Partidos ganados (PG): "))
        PE = int(input("Partidos empatados (PE): "))
        PP = int(input("Partidos perdidos (PP): "))

        # Validación: coherencia de partidos
        if PG + PE + PP != PJ:
            print("⚠️  Advertencia: La suma de ganados, empatados y perdidos no coincide con los jugados.")

        # Goles
        GF = int(input("Goles a favor (GF): "))
        GC = int(input("Goles en contra (GC): "))
        DG = GF - GC

        # Cálculos
        PUNTOS = (PG * 3) + PE
        Prom_Victorias = 0 if PJ == 0 else round((PG / PJ) * 100, 2)

        # Tarjetas
        TA = int(input("Tarjetas amarillas: "))
        TR = int(input("Tarjetas rojas: "))

        # Entrenador y estadio
        Dt = input("Entrenador: ").strip()
        Estadio = input("Estadio: ").strip()

        # Temporada (fija o editable)
        Temporada = input("Temporada (ej. 2024/2025): ").strip()

        # Agregar datos
        equipos.append(nombre)
        datos.append((PJ, PG, PE, PP, GF, GC, DG, PUNTOS,
                      Prom_Victorias, TA, TR, Dt, Estadio, Temporada))

    return equipos, datos


# =========================================
# FUNCIÓN: MOSTRAR TABLAS Y RESULTADOS
# =========================================
def generar_tablas(equipos, datos):
    columnas = ["PJ", "PG", "PE", "PP", "GF", "GC", "DG", "PUNTOS",
                "% VICTORIAS", "TARJETAS AMARILLAS", "TARJETAS ROJAS",
                "ENTRENADOR", "ESTADIO", "TEMPORADA"]

    df = pd.DataFrame(datos, columns=columnas, index=equipos)

    print("\n📋 TABLA ORIGINAL:")
    print(df)

    print("\n🏆 TABLA ORDENADA POR PUNTOS (MAYOR A MENOR):")
    print(df.sort_values(by="PUNTOS", ascending=False))

    print("\n⚽ EQUIPOS CON MÁS DE 10 PUNTOS:")
    print(df[df["PUNTOS"] > 10])

    print("\n🔥 EQUIPOS CON % DE VICTORIAS MAYOR A 50%:")
    print(df[df["% VICTORIAS"] > 50])

    print("\n📊 TABLA RESUMIDA (PUNTOS, ENTRENADOR, TEMPORADA):")
    print(df[["PUNTOS", "ENTRENADOR", "TEMPORADA"]])

    print("\n✅ Temporada finalizada.")


# =========================================
# PROGRAMA PRINCIPAL
# =========================================
def main():
    print("===============================================")
    print("     SISTEMA DE TABLA DE RESULTADOS FUTBOL     ")
    print("               TEMPORADA 2024/2025             ")
    print("===============================================")

    equipos, datos = datos_equipos()
    generar_tablas(equipos, datos)

    print("\nFin del programa ⚽. ¡Gracias por usar el sistema!")


# =========================================
# EJECUCIÓN
# =========================================
if __name__ == "__main__":
    main()
