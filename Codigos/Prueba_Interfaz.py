#IMPORTANTE#
#Instalar las librerias, escribir en la terminal "pip install streamlit"
#Para ejecutar el codigo escribir en la terminal "streamlit run Codigos/Prueba_Interfaz.py"
#Para abrir la interfaz precionar control + clic izquierdo en el link que aparece en la terminal a la derecha de "Local URL:"


import streamlit as st #Libreria para la interfaz web
import pandas as pd #Libreria para poder tabular los datos y usar archivos .csv
import re #Libreria para poder manipular texto con patrones
st.set_page_config(layout="wide")
#Funciones
#Funcion para cargar los datos del excel en el data frame 
def cargar_Datos(ruta):
    df = pd.read_csv(ruta, sep= ";")
    df["ENTRENADOR"] = df["ENTRENADOR"].apply(lambda x: re.sub(r'(?<!^)(?=[A-Z])', ' ', x)) #Separa el Nombre del Entrenador
    df["ESTADIO"] = df["ESTADIO"].apply(lambda x: re.sub(r'(?<!^)(?=[A-Z])', ' ', x)) #Separa el Nombre del Estadio
    df["EQUIPO"] = df["EQUIPO"].apply(lambda x: re.sub(r'(?<!^)(?=[A-Z])', ' ', x)) #Separa el Nombre del Equipo
    return df

#Programa Principal
#Se guarda en una variable la ruta del excel
ruta = "Datos/Premier_24_25.csv"
df = cargar_Datos(ruta)
df = df.sort_values(by="EQUIPO")  #Se ordena la tabla por defecto por orden Alfabetico

#Columnas De La Premier League
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
    st.subheader("Temporada: 2024/2025")
    st.subheader("Partidos: 380")

with col3:
    st.subheader("Leyenda De Columnas:")
    st.markdown("1. PJ = Partidos Jugados\n2. PG = Partidos Ganados\n3. PE = Partidos Empatados\n4. PP = Partidos Perdidos\n5. GF = Goles A Favor\n" \
    "6. GC = Goles En Contra\n7. DG = Diferencia De Gol\n8. TA = Tarjetas Amarillas\n9. TR = Tarjetas Rojas")

#Se muestra la tabla original de la Premier
st.markdown("---")
st.title("Tabla De La Liga")
st.set_page_config(layout="wide")
st.dataframe(df, use_container_width=True, height=738, hide_index=True)

#Se muestra la tabla con los equipos clasificados a la Champions
st.markdown("---")
st.title("Equipos clasificados a la Champions League")
df_ordenado = df.sort_values(by="PUNTOS", ascending=False).reset_index(drop=True)
top_5 = df_ordenado.head(5)
st.dataframe(top_5, use_container_width=True, hide_index=True)

#Se muestra la tabla con los equipos clasificados a la Europa 
st.markdown("---")
st.title("Equipos Clasificados A La Europa League")
top_6_7 = df_ordenado[5:7]
st.dataframe(top_6_7, use_container_width=True, hide_index=True)

#Se muestra la tabla con los equipos que Descienden
st.markdown("---")
st.title("Equipos Que Descienden")
ultimos_3 = df_ordenado.tail(3)
st.dataframe(ultimos_3, use_container_width=True, hide_index=True)

#Se muestra al equipo que gano la liga en la temporada 24/25
st.markdown("---")
st.title("Campeon de la Premier")
ganador = df.loc[df["PUNTOS"].idxmax()]

#Columnas del equipo ganador
logo,datos = st.columns([5,5])
with logo:
    st.image(f"Logos/{ganador["EQUIPO"]}.png",width=500)
with datos:
    st.title(f"Equipo: {ganador["EQUIPO"]}")
    st.subheader(f"• Entrenador: {ganador["ENTRENADOR"]}")
    st.subheader(f"• Estadio: {ganador["ESTADIO"]}")
    st.subheader(f"• Puntos: {ganador["PUNTOS"]}")
    st.subheader(f"• Victorias: {ganador["PG"]}")
    st.subheader(f"• Empates: {ganador["PE"]}")
    st.subheader(f"• Derrotas: {ganador["PP"]}")
st.markdown("---")

#Futura Opcion en la que el usuario podra buscar un equipo y mostrar sus estadisticas
st.title("Buscar Estadísticas De Un Equipo")

# Lista de equipos ordenada alfabéticamente
equipos = df["EQUIPO"].sort_values().unique()

# Selectbox para elegir el equipo
equipo_seleccionado = st.selectbox("Selecciona un equipo", equipos)

# Filtrar el dataframe para el equipo seleccionado
equipo_df = df[df["EQUIPO"] == equipo_seleccionado].iloc[0]

# Mostrar estadísticas
col_logo,linea,espacio,col_info = st.columns([1,0.01,0.5, 2])
with col_logo:
    try:
        st.image(f"Logos/{equipo_df['EQUIPO']}.png", width=500)
    except:
        st.warning("Logo no disponible.")
with linea:
    st.markdown("|\n"*44)

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