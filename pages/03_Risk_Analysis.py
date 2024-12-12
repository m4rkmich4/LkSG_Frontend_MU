import streamlit as st
from utils import generate_supplier_data, generate_heatmap
import pydeck as pdk
import pandas as pd

# Mapbox API-Key setzen
pdk.settings.mapbox_api_key = "pk.eyJ1IjoiYXByeWxsaW9uIiwiYSI6ImNtNGp6b2p4bDBndzYyaXIzc2dldnU3MXMifQ.QKu763IA6iTXvgkdFSq3Dw"  # Ersetze "DEIN_MAPBOX_TOKEN" durch deinen tatsächlichen Token

# Funktion: Linienverbindungen zwischen Punkten erstellen
def create_line_data(data):
    # Firmensitz als Startpunkt definieren (erster Eintrag in der Tabelle)
    base_lat = data.iloc[0]["Latitude"]
    base_lon = data.iloc[0]["Longitude"]

    # Linien von Firmensitz zu anderen Standorten erstellen
    lines = []
    for _, row in data.iterrows():
        lines.append({
            "start_lat": base_lat,
            "start_lon": base_lon,
            "end_lat": row["Latitude"],
            "end_lon": row["Longitude"],
        })
    return pd.DataFrame(lines)

# Seite konfigurieren
st.set_page_config(page_title="Risikoanalyse", layout="wide", page_icon="🌍")

# Begrüßung
st.markdown(
    """
    <h1 style="text-align: center; color: #4CAF50;">🌍 Risikoanalyse</h1>
    <p style="text-align: center; color: #666; font-size: 1.2rem;">
        Analysieren Sie Risiken weltweit mit interaktiven Karten und Daten.
    </p>
    """,
    unsafe_allow_html=True,
)

# Dummy-Daten generieren
df = generate_supplier_data()

# Heatmap
st.markdown("<h3 style='text-align: center;'>🌍 Globale Risiko-Heatmap</h3>", unsafe_allow_html=True)
fig_2d = generate_heatmap(df)
st.plotly_chart(fig_2d, use_container_width=True)

# Lieferantentabelle
st.markdown("<h3 style='text-align: center;'>📋 Lieferantendetails</h3>", unsafe_allow_html=True)
st.dataframe(df)

# Linien-Daten generieren
line_data = create_line_data(df)

# Schwarze zoomfähige Karte (Stadtstandorte visualisieren)
st.markdown("<h3 style='text-align: center;'>🗺️ Interaktive Lieferketten-Karte</h3>", unsafe_allow_html=True)

# Scatterplot-Layer mit größeren Punkten
scatter_layer = pdk.Layer(
    "ScatterplotLayer",
    data=df,
    get_position=["Longitude", "Latitude"],
    get_color="[255, 0, 0, 160]",  # Rot mit Transparenz
    get_radius=30000,  # Radius der Punkte erhöht
)

# LineLayer für die Verbindungen
line_layer = pdk.Layer(
    "LineLayer",
    data=line_data,
    get_source_position=["start_lon", "start_lat"],
    get_target_position=["end_lon", "end_lat"],
    get_color="[255, 255, 255, 160]",  # Weiße Linien mit Transparenz
    get_width=3,  # Breite der Linien
)

# View-Settings für die Karte
view_state = pdk.ViewState(
    latitude=51.1657,
    longitude=10.4515,
    zoom=3.5,
    pitch=50
)

# Pydeck-Karte erstellen
r = pdk.Deck(
    layers=[scatter_layer, line_layer],
    initial_view_state=view_state,
    map_style="mapbox://styles/mapbox/satellite-streets-v11",  # Satellitenbilder als Kartenstil
)

# Karte anzeigen
st.pydeck_chart(r)
