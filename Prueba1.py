#Prueba Numero 1
#Funciones
#En esta funcion se piden los datos de los equipos y se guardan en las listas
def datos_Equipos(equipos,datos):
    global cantidad
    contador = 0
    cantidad = int(input("Cuantos equipos va a ingresar: "))
    while contador < cantidad:
        nombre = input("Nombre del equipo: ")
        PJ = int(input("Partidos jugados: "))
        PG = int(input("Paridos ganados: "))
        PE = int(input("Partidos empatados: "))
        PP = int(input("Partidos perdidos: "))
        GF = int(input("Goles a favor: "))
        GC = int(input("Goles en contra: "))
        DG = GF - GC   #DG es diferencia de gol
        Puntos = (PG * 3) + (PE * 1)
        Prom_Victorias = (PG/PJ) * 100
        TA = int(input("Tarjetas amarillas: "))
        TR = int(input("Tarjetas rojas: "))
        Dt = input("Entrenador: ")
        Estadio = input("Estadio: ")
        Temporada = ("2023/2024")
        equipos.append(nombre)
        datos.append((PJ,PG,PE,PP,GF,GC,DG,Puntos,Prom_Victorias,TA,TR,Dt,Estadio,Temporada))
        contador += 1

#Programa Principal
cantidad = 0
equipos = []
datos = []
datos_Equipos(equipos,datos)
#Esta no es la tabla definitiva toca hacerla con la biblioteca pandas, solo es para verificar que si se guardaron los datos en las listas 
#Tambien toca mirar como ordenar los equipos de mayor a menor con los puntos 
print("\n///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
print("| NOMBRE | PJ | PG | PE | PP | GF | GC | DG | PUNTOS | % VICTORIAS | TARJETAS AMARILLAS | TARJETAS ROJAS | ENTRENADOR | ESTADIO | TEMPORADA |")
for i in range(cantidad):
    print(equipos[i],datos[i])
print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")


