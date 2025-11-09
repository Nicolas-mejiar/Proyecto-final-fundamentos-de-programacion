#IMPORTANTE#
#Instalar las librerias, escribir en la terminal "pip install streamlit"
#Para ejecutar el codigo escribir en la terminal "streamlit run Codigos/Prueba_Interfaz.py"
#Para abrir la interfaz precionar control + clic izquierdo en el link que aparece en la terminal a la derecha de "Local URL:"


import streamlit as st #Libreria para la interfaz web
import pandas as pd #Libreria para utilizar datos tabulares como .csv
import re #Libreria para trabajar con expreciones regulares
import os #Libreria para que el programa pueda hacer uso de archivos externos

#Funciones
#Funcion para cargar los datos de los archivos .csv en un dataframe
def cargar_Datos(ruta):
    df = pd.read_csv(ruta, sep= ";")
    df["ENTRENADOR"] = df["ENTRENADOR"].apply(lambda x: re.sub(r'(?<!^)(?=[A-Z])', ' ', x)) #Separa el Nombre del Entrenador
    df["ESTADIO"] = df["ESTADIO"].apply(lambda x: re.sub(r'(?<!^)(?=[A-Z])', ' ', x)) #Separa el Nombre del Estadio
    df["EQUIPO"] = df["EQUIPO"].apply(lambda x: re.sub(r'(?<!^)(?=[A-Z])', ' ', x)) #Separa el Nombre del Equipo
    return df

#Programa Principal
#Se define que se va a usar todo el ancho de la interfaz
st.set_page_config(layout="wide")

#Selector De Temporadas
#Titulo
st.title(("Elija La Temporada (2000-2025)"))

#Se crea un diccionario que relaciona cada temporada con su archivo .csv correspondiente
temporadas = {
    "2000/2001" : "Datos/premier_2000_2001.csv",
    "2001/2002" : "Datos/premier_2001_2002.csv",
    "2002/2003" : "Datos/premier_2002_2003.csv",
    "2003/2004" : "Datos/premier_2003_2004.csv",
    "2004/2005" : "Datos/premier_2004_2005.csv",
    "2005/2006" : "Datos/premier_2005_2006.csv",
    "2006/2007" : "Datos/premier_2006_2007.csv",
    "2007/2008" : "Datos/premier_2007_2008.csv",
    "2008/2009" : "Datos/premier_2008_2009.csv",
    "2009/2010" : "Datos/premier_2009_2010.csv",
    "2010/2011" : "Datos/premier_2010_2011.csv",
    "2011/2012" : "Datos/premier_2011_2012.csv",
    "2012/2013" : "Datos/premier_2012_2013.csv",
    "2013/2014" : "Datos/premier_2013_2014.csv",
    "2014/2015" : "Datos/premier_2014_2015.csv", 
    "2015/2016" : "Datos/premier_2015_2016.csv",
    "2016/2017" : "Datos/premier_2016_2017.csv",
    "2017/2018" : "Datos/premier_2017_2018.csv",
    "2018/2019" : "Datos/premier_2018_2019.csv",
    "2019/2020" : "Datos/premier_2019_2020.csv",
    "2020/2021" : "Datos/premier_2020_2021.csv",
    "2021/2022" : "Datos/premier_2021_2022.csv",
    "2022/2023" : "Datos/premier_2022_2023.csv",
    "2023/2024" : "Datos/premier_2023_2024.csv",
    "2024/2025" : "Datos/premier_2024_2025.csv"
}

#Boton para que el usuario pueda cambiar de temporada
temporada_sel = st.selectbox("Selecciona una temporada", list(temporadas.keys()))

#Se guarda la temporada seleccionada en ruta 
ruta = temporadas[temporada_sel]
if not os.path.exists(ruta):
    st.error(f"No se encontró el archivo: {ruta}")
    st.stop()

#Se llama a la funcion y se guarda el dataframe en df
df = cargar_Datos(ruta)
df = df.sort_values(by="EQUIPO")

#Se configura la interfaz web para ser mostrada por columnas
col1,linea1,espacio1,col2,col3 = st.columns([3,0.01,0.1,3,3])
with col1:
    st.image("Logos/Premier_League.png",width=500,)
with linea1:
    st.markdown("|\n"*30)
with espacio1:
    st.write("")
with col2:
    st.title("PREMIER LEAGUE")
    st.subheader("Pais: Inglaterra")
    st.subheader("Division: 1")
    st.subheader(f"Temporada: {temporada_sel}")
    st.subheader("Partidos: 380")
with col3:
    st.subheader("Leyenda De Columnas:")
    st.markdown("1. PJ = Partidos Jugados\n2. PG = Partidos Ganados\n3. PE = Partidos Empatados\n4. PP = Partidos Perdidos\n5. GF = Goles A Favor\n" \
    "6. GC = Goles En Contra\n7. DG = Diferencia De Gol\n8. TA = Tarjetas Amarillas\n9. TR = Tarjetas Rojas")

#Se muestra la tabla de origianl de la premier
st.markdown("---")
st.title("Tabla De La Liga")
st.dataframe(df, use_container_width=True, height=738, hide_index=True)

#Se muestra la tabla con los equipos clasificados a la Champions League
st.markdown("---")
st.title("Equipos clasificados a la Champions League")
df_ordenado = df.sort_values(by="PUNTOS", ascending=False).reset_index(drop=True)
top_5 = df_ordenado.head(5)
st.dataframe(top_5, use_container_width=True, hide_index=True)

#Se muestra la tabla con los equipos clasificados a la Europa League
st.markdown("---")
st.title("Equipos Clasificados A La Europa League")
top_6_7 = df_ordenado[5:7]
st.dataframe(top_6_7, use_container_width=True, hide_index=True)

#Se muestra la tabla con los equipos que Descienden 
st.markdown("---")
st.title("Equipos Que Descienden")
ultimos_3 = df_ordenado.tail(3)
st.dataframe(ultimos_3, use_container_width=True, hide_index=True)

#Se muestra al equipo que gano la liga en esa temporada
st.markdown("---")
st.title("Campeon de la Premier")
ganador = df.loc[df["PUNTOS"].idxmax()]

#Se divide la seccion en 2 columnas logo y estadisticas del equipo
logo,datos = st.columns([2,3])
with logo:
    nombre_logo = ganador['EQUIPO'].replace(' ', '').replace('-', '').lower()
    st.image(f"Logos/{nombre_logo}.png", width=500)
with datos:
    st.title(f"Equipo: {ganador["EQUIPO"]}")
    st.subheader(f"• Entrenador: {ganador["ENTRENADOR"]}")
    st.subheader(f"• Estadio: {ganador["ESTADIO"]}")
    st.subheader(f"• Puntos: {ganador["PUNTOS"]}")
    st.subheader(f"• Victorias: {ganador["PG"]}")
    st.subheader(f"• Empates: {ganador["PE"]}")
    st.subheader(f"• Derrotas: {ganador["PP"]}")
st.markdown("---")

#Opcion para buscar las estadisticas de un equipo
#Titulo
st.title("Buscar Estadísticas De Un Equipo")

#Se configura para mostrar los equipos en orden alfabetico
equipos = df["EQUIPO"].sort_values().unique()

#Se crea un boton para que el usuario elija el equipo que desee
equipo_seleccionado = st.selectbox("Selecciona un equipo", equipos)

#Se filtra el dataframe para el equipo seleccionado
equipo_df = df[df["EQUIPO"] == equipo_seleccionado].iloc[0]

#Columnas para mostrar el logo y las estadisticas del equipo seleccionado
col_logo,espacio,col_info = st.columns([1,0.5,2])   
with col_logo:
    nombre_equipo = equipo_df['EQUIPO'].lower().replace(" ", "").replace("-", "").replace("'", "")
    carpeta_logos = "Logos"
    archivos = [f for f in os.listdir(carpeta_logos) if f.lower().endswith(".png")]
    logo_encontrado = None
    for archivo in archivos:
        nombre_archivo = os.path.splitext(archivo)[0].lower().replace(" ", "").replace("-", "").replace("'", "")
        if nombre_equipo in nombre_archivo or nombre_archivo in nombre_equipo:
            logo_encontrado = archivo
            break
    if logo_encontrado:
        st.image(os.path.join(carpeta_logos, logo_encontrado), width=500)
    else:
        st.warning("Logo no disponible.")
with espacio:
    st.write("")
with col_info:
    st.subheader(f"Equipo: {equipo_df['EQUIPO']}")
    st.text(f"Entrenador: {equipo_df['ENTRENADOR']}")
    st.text(f"Estadio: {equipo_df['ESTADIO']}")
    st.text(f"Puntos: {equipo_df['PUNTOS']}")
    st.text(f"Partidos Jugados: {equipo_df['PJ']}")
    st.text(f"Victorias: {equipo_df['PG']}")
    st.text(f"Empates: {equipo_df['PE']}")
    st.text(f"Derrotas: {equipo_df['PP']}")
    st.text(f"Goles a Favor: {equipo_df['GF']}")
    st.text(f"Goles en Contra: {equipo_df['GC']}")
    st.text(f"Diferencia de Gol: {equipo_df['DG']}")
    st.text(f"Tarjetas Amarillas: {equipo_df['TA']}")
    st.text(f"Tarjetas Rojas: {equipo_df['TR']}")

#Se muetran las estadisticas en un grafico de barras
st.markdown("---")
st.subheader("Grafico De Las Estadisticas")
estadisticas = {
    "Puntos": equipo_df["PUNTOS"],
    "Partidos Jugados": equipo_df["PJ"],
    "Victorias": equipo_df["PG"],
    "Empates": equipo_df["PE"],
    "Derrotas": equipo_df["PP"],
    "Goles a Favor": equipo_df["GF"],
    "Goles en Contra": equipo_df["GC"],
    "Tarjetas Amarillas": equipo_df["TA"],
    "Tarjetas Rojas": equipo_df["TR"]
}

# Se convierten las estadisticas en un dataframe
estadisticas_df = pd.DataFrame(list(estadisticas.items()), columns=["Estadística", "Valor"])

#Se crea un grafico de barras con el dataframe
st.bar_chart(data=estadisticas_df, x="Estadística", y="Valor", use_container_width=True)
