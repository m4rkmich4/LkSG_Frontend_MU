import streamlit as st
import pandas as pd
from time import sleep
import random

# Seite konfigurieren
st.set_page_config(page_title="Datenimport", layout="wide", page_icon="📂")

# Falls wir eine globale Lieferantenliste benötigen:
if "suppliers" not in st.session_state:
    st.session_state["suppliers"] = [
        # Beispielhaft schon vorhandene Lieferanten
        {"Name": "Globex Inc.", "Standort": "Berlin", "Land": "Deutschland", "UID": "DE-12345", "Risiko": "10%"},
        {"Name": "ACME Corporation", "Standort": "Hamburg", "Land": "Deutschland", "UID": "DE-98765", "Risiko": "20%"}
    ]

# Begrüßung
st.markdown(
    """
    <h1 style="text-align: center; color: #4CAF50;">📂 Datenimport</h1>
    <p style="text-align: center; color: #666; font-size: 1.2rem;">
        Laden Sie Ihre Lieferantendaten hoch, um den Prozess zu starten.
    </p>
    """,
    unsafe_allow_html=True,
)

# Dateiupload
uploaded_file = st.file_uploader(
    "🚀 Laden Sie eine Datei hoch (Excel, CSV, JSON, PDF, JPEG)",
    type=["xlsx", "xls", "csv", "json", "pdf", "jpg", "jpeg"]
)

df = None
file_type = None

if uploaded_file:
    # Fortschrittsanzeige
    loading_message = st.empty()
    loading_message.markdown("<h3 style='text-align: center;'>🔄 Datei wird verarbeitet...</h3>", unsafe_allow_html=True)
    progress = st.progress(0)

    for i in range(100):  # Simuliert das Verarbeiten der Datei
        sleep(0.01)
        progress.progress(i + 1)

    # Erfolgsanzeige
    loading_message.empty()
    progress.empty()
    st.success("✅ Datei erfolgreich hochgeladen!")

    # Datei verarbeiten
    try:
        if uploaded_file.name.endswith(".xlsx") or uploaded_file.name.endswith(".xls"):
            # Excel-Datei verarbeiten
            df = pd.read_excel(uploaded_file)
            file_type = "excel"
        elif uploaded_file.name.endswith(".csv"):
            # CSV-Datei verarbeiten
            df = pd.read_csv(uploaded_file)
            file_type = "csv"
        elif uploaded_file.name.endswith(".json"):
            # JSON-Datei verarbeiten
            df = pd.read_json(uploaded_file)
            file_type = "json"
        elif uploaded_file.name.endswith(".pdf") or uploaded_file.name.endswith(".jpg") or uploaded_file.name.endswith(
                ".jpeg"):
            # PDF oder Bild-Datei: hier können keine direkten tabellarischen Daten ausgelesen werden
            # Stattdessen simulieren wir einen KI-Prozess, der Daten extrahiert.
            st.info("📄 Die hochgeladene Datei ist eine PDF- oder Bilddatei. Daten werden mittels KI extrahiert (Mock).")
            file_type = "non_tabular"
            df = None
        else:
            raise ValueError("Unbekanntes Dateiformat!")

        if df is not None:
            st.markdown("<h3 style='text-align: center;'>📋 Vorschau der hochgeladenen Daten</h3>",
                        unsafe_allow_html=True)
            st.dataframe(df)

    except Exception as e:
        st.error(f"❌ Fehler beim Verarbeiten der Datei: {e}")
else:
    st.info("Bitte laden Sie eine Datei hoch, um fortzufahren.")

# Hinweis
st.markdown(
    """
    <p style="text-align: center; color: #666; font-size: 1rem; margin-top: 2rem;">
        Unterstützte Formate: Excel, CSV, JSON, PDF, JPEG.
        Stellen Sie sicher, dass die Datei gültige Daten enthält.
    </p>
    """,
    unsafe_allow_html=True,
)

if uploaded_file is not None:
    if st.button("Importierte Daten verarbeiten"):
        # KI-Prozess simulieren
        st.markdown("<h3 style='text-align: center;'>🤖 KI-Prozess wird gestartet...</h3>", unsafe_allow_html=True)

        # Wenn die Datei nicht tabellarisch war (PDF/JPEG), simulieren wir jetzt einen KI-Schritt,
        # der Daten extrahiert und ein Dummy-DataFrame erzeugt.
        if file_type == "non_tabular":
            with st.spinner("🧠 KI extrahiert Daten aus dem Dokument..."):
                sleep(2)
            st.success("✅ Daten aus nicht-tabellarischem Format extrahiert!")

            # Erzeuge einen Mock-DataFrame mit realistisch klingenden Lieferantennamen und realen Ländern
            mock_names = ["NovaTech Ltd.", "GreenField Supplies", "EuroParts Co.", "GlobalSource AG"]
            mock_locations = ["Zürich", "Wien", "Amsterdam", "Kopenhagen"]
            mock_countries = ["Schweiz", "Österreich", "Niederlande", "Dänemark"]

            extracted_data = {
                "Name": [random.choice(mock_names) for _ in range(2)],
                "Standort": [random.choice(mock_locations) for _ in range(2)],
                "Land": [random.choice(mock_countries) for _ in range(2)],
                "UID": [f"EU-{random.randint(10000, 99999)}" for _ in range(2)]
            }
            df = pd.DataFrame(extracted_data)

            st.markdown("<h3 style='text-align: center;'>📋 Extrahierte Daten (Mock)</h3>", unsafe_allow_html=True)
            st.dataframe(df)

        required_columns = ["Name", "Standort", "Land", "UID"]
        if df is None or not all(col in df.columns for col in required_columns):
            st.error(
                "❌ Die extrahierten Daten enthalten nicht alle erforderlichen Spalten (Name, Standort, Land, UID). Vorgang abgebrochen.")
            st.stop()  # Bricht die Ausführung hier ab

        # 1. KI initialisiert
        with st.spinner("🔄 KI initialisiert..."):
            sleep(2)
        st.success("✅ KI bereit!")

        # 2. KI erstellt Supply Chain aus Dokumenten/Excel
        with st.spinner("🔧 KI erstellt Supply Chain..."):
            sleep(2)
        st.success("✅ Supply Chain-Struktur erstellt!")

        # 3. KI prüft Lieferanten und erweitert/aktualisiert sie in der Graphendatenbank
        with st.spinner("🧠 KI prüft und aktualisiert Lieferantendaten..."):
            sleep(2)

        for _, row in df.iterrows():
            name = row["Name"]
            location = row["Standort"]
            country = row["Land"]
            uid = row["UID"]

            # Prüfung, ob Lieferant schon existiert
            existing_supplier = None
            for supplier in st.session_state["suppliers"]:
                if supplier["UID"] == uid:
                    existing_supplier = supplier
                    break

            if existing_supplier:
                # Lieferant existiert - Update
                st.info(f"🔄 Aktualisiere bestehenden Lieferanten: {name}")
                existing_supplier["Name"] = name
                existing_supplier["Standort"] = location
                existing_supplier["Land"] = country
                # Risiko neu berechnen (fake)
                new_risk = f"{random.randint(0, 100)}%"
                existing_supplier["Risiko"] = new_risk
                st.success(f"✅ Lieferant {name} aktualisiert (UID: {uid}, Neues Risiko: {new_risk})")
            else:
                # Neuer Lieferant
                st.info(f"➕ Neuer Lieferant wird hinzugefügt: {name}")
                new_risk = f"{random.randint(0, 100)}%"
                st.session_state["suppliers"].append({
                    "Name": name,
                    "Standort": location,
                    "Land": country,
                    "UID": uid,
                    "Risiko": new_risk,
                })
                st.success(f"✅ Lieferant {name} neu angelegt (UID: {uid}, Risiko: {new_risk})")

        # 4. KI schreibt die aktualisierten Daten in die Graphendatenbank (fake)
        with st.spinner("💾 KI schreibt Daten in die Graphendatenbank..."):
            sleep(2)
        st.success("✅ Daten in Graphendatenbank geschrieben!")

        st.markdown("<h3 style='text-align: center;'>🎉 Prozess abgeschlossen!</h3>", unsafe_allow_html=True)

        st.markdown("### 📋 Aktuelle Lieferantenliste (nach Update)")
        st.dataframe(pd.DataFrame(st.session_state["suppliers"]))