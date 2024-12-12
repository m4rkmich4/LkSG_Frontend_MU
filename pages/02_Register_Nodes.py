import streamlit as st
from time import sleep
import random

# Seite konfigurieren
st.set_page_config(page_title="Lieferanten & Produkte verwalten", layout="wide", page_icon="🏗️")

# Initialisiere Lieferantenliste falls noch nicht vorhanden
if "suppliers" not in st.session_state:
    st.session_state["suppliers"] = []  # zu Beginn leer

# Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Wählen Sie eine Seite", ["Lieferanten anlegen", "Produkte registrieren"])

# Seite: Lieferanten anlegen
if page == "Lieferanten anlegen":
    st.markdown(
        """
        <h1 style="text-align: center; color: #4CAF50;">🏗️ Lieferanten anlegen</h1>
        <p style="text-align: center; color: #666; font-size: 1.2rem;">
            Fügen Sie neue Lieferanten hinzu, indem Sie entweder eine UID (Unternehmens Identifikations-Nummer) eingeben oder die Daten manuell erfassen.
        </p>
        """,
        unsafe_allow_html=True,
    )

    if "form_submitted" not in st.session_state:
        st.session_state["form_submitted"] = False

    method = st.radio("Eingabemethode für Lieferant:", ["UID eingeben", "Manuelle Eingabe"])

    with st.form("Lieferant Form"):
        if method == "UID eingeben":
            uid = st.text_input("UID (Unternehmens Identifikations-Nummer) eingeben")
        else:
            name = st.text_input("📛 Name des Lieferanten")
            location = st.text_input("📍 Standort")
            country = st.text_input("🌍 Land")
            uid = st.text_input("💼 Unternehmens Identifikations-Nummer (UID)")

        submitted = st.form_submit_button("Speichern")

        if submitted:
            st.session_state["form_submitted"] = True

            # KI-Schritte simulieren
            if method == "UID eingeben":
                st.markdown("<h3 style='text-align: center;'>🤖 Die KI lädt Lieferantendaten anhand der UID...</h3>", unsafe_allow_html=True)
                with st.spinner(f"🔍 KI sucht Daten für UID {uid}..."):
                    sleep(2)
                st.success("✅ Daten erfolgreich geladen!")

                # Beispielhafte Lieferantenvorlagen
                supplier_templates = [
                    {"Name": "Globex Inc.", "Standort": "Berlin", "Land": "Deutschland"},
                    {"Name": "ACME Corporation", "Standort": "Hamburg", "Land": "Deutschland"},
                    {"Name": "Widgets GmbH", "Standort": "München", "Land": "Deutschland"},
                    {"Name": "Rohstoffe AG", "Standort": "Frankfurt am Main", "Land": "Deutschland"},
                    {"Name": "Elemente & Co.", "Standort": "Stuttgart", "Land": "Deutschland"}
                ]

                chosen_supplier = random.choice(supplier_templates)
                name = chosen_supplier["Name"]
                location = chosen_supplier["Standort"]
                country = chosen_supplier["Land"]
            else:
                st.markdown("<h3 style='text-align: center;'>🤖 Die KI zieht Daten...</h3>", unsafe_allow_html=True)
                with st.spinner(f"🔍 KI sucht Daten für {name} in {country}..."):
                    sleep(2)
                st.success("✅ Daten erfolgreich gefunden!")

            st.markdown("<h3 style='text-align: center;'>📊 Validierung der Daten...</h3>", unsafe_allow_html=True)
            with st.spinner("🧠 KI validiert die Daten..."):
                sleep(2)
            st.success("✅ Daten validiert!")

            risk_score = random.randint(0, 100)
            st.markdown("<h3 style='text-align: center;'>⚖️ KI ermittelt Risiko...</h3>", unsafe_allow_html=True)
            with st.spinner("📈 Risiko wird berechnet..."):
                sleep(2)
            st.success(f"✅ Risiko ermittelt: {risk_score}%")

            st.markdown("<h3 style='text-align: center;'>Erfolgreich angemeldet</h3>", unsafe_allow_html=True)
            st.success(f"✅ Lieferant '{name}' erfolgreich hinzugefügt!")

            st.session_state["suppliers"].append({
                "Name": name,
                "Standort": location,
                "Land": country,
                "UID": uid,
                "Risiko": f"{risk_score}%",
            })

    if st.session_state["form_submitted"]:
        if st.button("📤 Weiteren Lieferanten hinzufügen"):
            st.session_state["form_submitted"] = False

    # Lieferanten nur anzeigen, wenn tatsächlich welche angelegt wurden
    if len(st.session_state["suppliers"]) > 0:
        st.markdown("### 📋 Aktuelle Lieferanten")
        for supplier in st.session_state["suppliers"]:
            st.write(supplier)

# Seite: Produkte registrieren
elif page == "Produkte registrieren":
    st.markdown(
        """
        <h1 style="text-align: center; color: #4CAF50;">📦 Produkte registrieren</h1>
        <p style="text-align: center; color: #666; font-size: 1.2rem;">
            Erfassen Sie Produkte, entweder nur per Artikelnummer oder durch detaillierte Eingabe.
        </p>
        """,
        unsafe_allow_html=True,
    )

    if len(st.session_state["suppliers"]) == 0:
        st.warning("⚠️ Bitte registrieren Sie zuerst Lieferanten, bevor Sie ein Produkt hinzufügen!")
    else:
        method = st.radio("Eingabemethode für Produkt:", ["Artikelnummer eingeben", "Manuelle Eingabe"])

        with st.form("Produkt Form"):
            if method == "Artikelnummer eingeben":
                article_number = st.text_input("📦 Artikelnummer des Produkts")
                product_name = f"Produkt_{article_number}"
                category = "Unbekannt"
                bom = "Teil A, Rohstoff B, Teil C"  # Dummy BOM
                selected_supplier = st.selectbox(
                    "Wählen Sie einen Lieferanten für dieses Produkt:",
                    [supplier["Name"] for supplier in st.session_state["suppliers"]]
                )
            else:
                product_name = st.text_input("📛 Name des Produkts")
                category = st.text_input("🏷️ Kategorie")
                source_type = st.radio(
                    "🔍 Stückliste beziehen aus:",
                    ["Eigenes ERP-System", "Manuelle Eingabe", "PDF-Scan"]
                )
                if source_type == "Manuelle Eingabe":
                    bom = st.text_area("🛠️ Stückliste (BOM - Rohstoffe und Komponenten, durch Komma getrennt)")
                else:
                    st.info(f"🔄 KI generiert die Stückliste aus {source_type}...")
                    bom = "Teil A, Rohstoff B, Teil C"

                selected_supplier = st.selectbox(
                    "Wählen Sie einen Lieferanten für dieses Produkt:",
                    [supplier["Name"] for supplier in st.session_state["suppliers"]]
                )

            submitted = st.form_submit_button("Produkt registrieren")

            if submitted:
                st.markdown("<h3 style='text-align: center;'>🤖 KI verarbeitet das Produkt...</h3>", unsafe_allow_html=True)

                with st.spinner("🔄 KI lädt Produktdaten..."):
                    sleep(2)
                st.success("✅ Produktdaten erfolgreich geladen!")

                with st.spinner(f"🔍 KI analysiert die Stückliste für {product_name}..."):
                    sleep(2)
                st.success("✅ Stückliste erfolgreich analysiert!")

                bom_items = [item.strip() for item in bom.split(",")]

                st.markdown("<h3 style='text-align: center;'>🔗 Verknüpfe Produkte mit Kundendaten (über BOM)...</h3>", unsafe_allow_html=True)
                with st.spinner("🔄 KI verknüpft Produkte mit Kundendaten über BOM..."):
                    sleep(2)
                st.success("✅ Produkte erfolgreich mit Kundendaten (BOM-basiert) verknüpft!")

                with st.spinner("🔧 KI fügt Abhängigkeiten von Teilen und Rohstoffen in die Supply Chain ein..."):
                    sleep(2)
                st.success("✅ Abhängigkeiten erfolgreich hinzugefügt!")

                with st.spinner("🔗 KI berechnet Netzwerk-Abhängigkeiten..."):
                    sleep(2)
                st.success("✅ Netzwerk-Abhängigkeiten erfolgreich berechnet!")

                with st.spinner("🧠 KI validiert die Eingaben zum Lieferanten und Produkt..."):
                    sleep(2)
                st.success("✅ Eingaben erfolgreich validiert!")

                with st.spinner("💾 KI schreibt Daten in die Datenbank..."):
                    sleep(2)
                st.success("✅ Daten erfolgreich in Datenbank geschrieben!")

                st.markdown("<h3 style='text-align: center;'>🔗 Verknüpfung mit Rohstoffen/Teilen und Lieferanten</h3>", unsafe_allow_html=True)
                for item in bom_items:
                    st.write(f"🔧 **{item}** wird von **{selected_supplier}** geliefert.")

                st.success(f"✅ Produkt '{product_name}' erfolgreich registriert!")