import streamlit as st
from utils import generate_supplier_data, generate_3d_map

# Seite konfigurieren
st.set_page_config(page_title="Dashboard Mock-Up", layout="wide", page_icon="📊")

# Begrüßung
st.markdown(
    """
    <h1 style="text-align: center; color: #4CAF50;">🌐 ClearChain Dashboard</h1>
    <p style="text-align: center; color: #666; font-size: 1.2rem; margin-bottom: 2rem;">
        Willkommen! Behalten Sie die wichtigsten Lieferketten- und Risikostatistiken im Blick.
    </p>
    """,
    unsafe_allow_html=True,
)

# Custom CSS für animierte KPI-Karten
st.markdown(
    """
    <style>
    .card {
        background: linear-gradient(120deg, #84fab0 0%, #8fd3f4 100%);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        text-align: center;
        transition: transform 0.2s, box-shadow 0.2s;
        color: white;
        margin-bottom: 1.5rem;
    }
    .card:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 16px rgba(0,0,0,0.4);
    }
    .card-title {
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .card-value {
        font-size: 3rem;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# KPI-Karten
st.markdown("<h2 style='text-align: center; margin-top: 2rem;'>📊 Wichtige Kennzahlen</h2>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.markdown(
        """
        <div class="card">
            <div class="card-title">📦 Anzahl Lieferanten</div>
            <div class="card-value">42</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="card">
            <div class="card-title">⚠️ Offene Risiken</div>
            <div class="card-value">7</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
        <div class="card">
            <div class="card-title">📝 Berichte erstellt</div>
            <div class="card-value">3</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# 3D-Weltkugel: Lieferkettenvisualisierung
st.markdown("<h3 style='text-align: center; margin-top: 3rem;'>🌍 3D-Lieferkettenwelt</h3>", unsafe_allow_html=True)
df = generate_supplier_data()
fig_3d = generate_3d_map(df)
st.plotly_chart(fig_3d, use_container_width=True)