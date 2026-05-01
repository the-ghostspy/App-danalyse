import streamlit as st

# Titre de la page
st.set_page_config(page_title="Analyse Paludisme", layout="wide")
st.title("📊 Application d'analyse - Paludisme")

# Lire votre fichier HTML et l'afficher
with open("paludisme.html", "r", encoding="utf-8") as fichier:
    contenu_html = fichier.read()
    st.components.v1.html(contenu_html, height=800, scrolling=True)
