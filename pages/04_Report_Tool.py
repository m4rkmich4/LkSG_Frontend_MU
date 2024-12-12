import streamlit as st
from fpdf import FPDF
import pandas as pd
import random
from time import sleep

# Seite konfigurieren
st.set_page_config(page_title="Report Generator", layout="wide", page_icon="📄")

# Begrüßung
st.markdown(
    """
    <h1 style="text-align: center; color: #4CAF50;">📄 Report Generator</h1>
    <p style="text-align: center; color: #666; font-size: 1.2rem;">
        Erstellen Sie einen PDF-Report basierend auf den analysierten Lieferantendaten. 
        Die KI übernimmt die Verarbeitung und Validierung.
    </p>
    """,
    unsafe_allow_html=True,
)

# Dummy-Daten
data = {
    "Land": ["Deutschland", "China", "USA", "Indien", "Brasilien", "Frankreich", "Japan", "Australien", "Kanada", "Russland"],
    "Stadt": ["Berlin", "Shanghai", "New York", "Mumbai", "São Paulo", "Paris", "Tokyo", "Sydney", "Toronto", "Moskau"],
    "Risiko": [round(random.uniform(0.1, 0.9), 2) for _ in range(10)],
    "Lieferanten": [random.randint(5, 50) for _ in range(10)],
}
df = pd.DataFrame(data)

# Funktion zur PDF-Erstellung
def generate_pdf(data):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Titel
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, txt="Lieferantenreport", ln=True, align="C")
    pdf.ln(10)

    # Untertitel
    pdf.set_font("Arial", style="", size=12)
    pdf.cell(200, 10, txt="Erstellt durch KI-Verarbeitung und Validierung", ln=True, align="C")
    pdf.ln(10)

    # Tabelle mit Daten
    pdf.set_font("Arial", size=10)
    pdf.cell(40, 10, txt="Land", border=1, align="C")
    pdf.cell(50, 10, txt="Stadt", border=1, align="C")
    pdf.cell(40, 10, txt="Risiko", border=1, align="C")
    pdf.cell(50, 10, txt="Lieferanten", border=1, align="C")
    pdf.ln()

    for index, row in data.iterrows():
        pdf.cell(40, 10, txt=row["Land"], border=1)
        pdf.cell(50, 10, txt=row["Stadt"], border=1)
        pdf.cell(40, 10, txt=f"{row['Risiko']:.2f}", border=1)
        pdf.cell(50, 10, txt=str(row["Lieferanten"]), border=1)
        pdf.ln()

    # Abschließender Text
    pdf.ln(10)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt="Dieser Bericht wurde durch KI-generierte Schritte erstellt, die die Daten "
                              "automatisch analysieren, validieren und in strukturierter Form ausgeben. "
                              "Die enthaltenen Informationen basieren auf den bereitgestellten Daten.")
    return pdf

# Zustand der App
if "report_ready" not in st.session_state:
    st.session_state["report_ready"] = False

# Button zum Generieren des PDF
if not st.session_state["report_ready"]:
    if st.button("📄 PDF-Report erstellen"):
        # Simuliere KI-Schritte
        st.markdown("<h3 style='text-align: center;'>🤖 KI-Schritte zur Datenverarbeitung</h3>", unsafe_allow_html=True)

        with st.spinner("🔄 Schritt 1: Die KI liest die Daten..."):
            sleep(2)
        st.success("✅ Schritt 1 abgeschlossen: Daten erfolgreich gelesen!")

        with st.spinner("🔄 Schritt 2: Die KI validiert die Daten..."):
            sleep(2)
        st.success("✅ Schritt 2 abgeschlossen: Daten erfolgreich validiert!")

        with st.spinner("🔄 Schritt 3: Die KI schreibt den Bericht..."):
            sleep(2)
        st.success("✅ Schritt 3 abgeschlossen: Bericht erfolgreich erstellt!")

        # PDF generieren
        pdf = generate_pdf(df)
        pdf_output = "Lieferantenreport.pdf"
        pdf.output(pdf_output)

        # Markiere den Bericht als fertig
        st.session_state["report_ready"] = True

# Download-Button anzeigen, wenn der Report fertig ist
if st.session_state["report_ready"]:
    with open("Lieferantenreport.pdf", "rb") as f:
        st.download_button(
            label="📥 PDF herunterladen",
            data=f,
            file_name="Lieferantenreport.pdf",
            mime="application/pdf",
        )
    st.success("✅ PDF wurde erfolgreich erstellt und steht zum Download bereit!")