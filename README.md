
# Lieferketten-Compliance Mock-Up

Dieses Projekt ist ein **Mock-Up** zur Verwaltung von Lieferketten-Compliance-Anforderungen, basierend auf dem Lieferkettensorgfaltspflichtengesetz (LkSG). Es bietet mehrere Funktionen wie Datenimport, Risikoanalyse, Berichtserstellung und ein Meldesystem.

## Funktionen
1. **Datenimport**
   - Import von Lieferantendaten aus Excel, CSV oder JSON.
   - Integration in eine grafische Darstellung für die Lieferkettenanalyse.

2. **Lieferantenverwaltung**
   - Registrierung neuer Lieferanten mit automatischer Risikoanalyse.
   - KI-gestützte Validierung und Speicherung der Daten.

3. **Risikoanalyse**
   - Analyse und Visualisierung der globalen Lieferkettenrisiken.
   - Darstellung mit 3D-Karten und Heatmaps.

4. **Berichtsgenerator**
   - Erstellung von PDF-Berichten, die Risikoanalysen und Lieferantendaten enthalten.
   

---

## Installation

### Voraussetzungen
- **Python 3.8 oder höher**
- Virtuelle Umgebung (optional, aber empfohlen)

### Schritte
1. Klone dieses Repository:
   ```bash
   git clone https://github.com/<dein-benutzername>/<dein-repository>.git
   ```

2. Navigiere in das Projektverzeichnis:
   ```bash
   cd <dein-repository>
   ```

3. Erstelle eine virtuelle Umgebung und aktiviere sie:
   - **Windows**:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - **Mac/Linux**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

4. Installiere die Abhängigkeiten:
   ```bash
   pip install -r requirements.txt
   ```

5. Starte die Anwendung:
   ```bash
   streamlit run Home.py
   ```

---

