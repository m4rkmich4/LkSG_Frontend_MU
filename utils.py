import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import random

# Funktion: Dummy-Daten für Lieferanten generieren
def generate_supplier_data():
    return pd.DataFrame({
        "Land": ["Deutschland", "China", "USA", "Indien", "Brasilien", "Frankreich", "Japan", "Australien", "Kanada", "Russland"],
        "Stadt": ["Berlin", "Shanghai", "New York", "Mumbai", "São Paulo", "Paris", "Tokyo", "Sydney", "Toronto", "Moskau"],
        "Risiko": [round(random.uniform(0.1, 0.9), 2) for _ in range(10)],
        "Lieferanten": [random.randint(5, 50) for _ in range(10)],
        "Latitude": [52.52, 31.23, 40.71, 19.08, -23.55, 48.85, 35.68, -33.87, 43.65, 55.75],
        "Longitude": [13.41, 121.47, -74.01, 72.88, -46.63, 2.35, 139.65, 151.21, -79.38, 37.61],
    })

# Funktion: Risiko-Heatmap generieren
def generate_heatmap(data):
    return px.choropleth(
        data,
        locations="Land",
        locationmode="country names",
        color="Risiko",
        hover_name="Stadt",
        hover_data={"Risiko": ":.2f", "Lieferanten": True},
        color_continuous_scale="Reds",
        title=""
    )

# Funktion: 3D-Lieferkettenkarte generieren
def generate_3d_map(data, start_country="Deutschland"):
    fig = go.Figure()

    # Basis: 3D-Karte mit Ländern und Städten
    fig.add_trace(
        go.Scattergeo(
            locationmode="ISO-3",
            lon=data["Longitude"],
            lat=data["Latitude"],
            text=data["Stadt"] + " (" + data["Land"] + ")<br>Risiko: " + data["Risiko"].astype(str) + "<br>Lieferanten: " + data["Lieferanten"].astype(str),
            marker=dict(
                size=[x * 1.1 + 10 for x in data["Lieferanten"]],  # Größe der Punkte skalieren
                color=data["Risiko"],
                colorscale="Viridis",
                cmin=0,
                cmax=1,
                line=dict(width=1, color='darkgray'),  # Umrandung der Punkte
            ),
            name="Lieferantenstandorte",
        )
    )

    # Lieferkettenpfeile simulieren
    start_lat = data[data["Land"] == start_country]["Latitude"].values[0]
    start_lon = data[data["Land"] == start_country]["Longitude"].values[0]

    for _, row in data.iterrows():
        if row["Land"] != start_country:
            fig.add_trace(
                go.Scattergeo(
                    locationmode="ISO-3",
                    lon=[start_lon, row["Longitude"]],
                    lat=[start_lat, row["Latitude"]],
                    mode="lines",
                    line=dict(width=2, color="red"),
                    name=f"Lieferkette {start_country} → {row['Stadt']}",
                )
            )

    # Globale Einstellungen der Karte
    fig.update_geos(
        showcountries=True, countrycolor="lightgray",
        showcoastlines=True, coastlinecolor="lightgray",
        projection_type="orthographic",
        projection_rotation=dict(lat=10, lon=20),
        landcolor="rgb(217, 217, 217)",
        oceancolor="lightblue",
        showocean=True,
    )
    fig.update_layout(
        title="",
        margin={"r": 0, "t": 50, "l": 0, "b": 0},
        height=700,
    )
    return fig