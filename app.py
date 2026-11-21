"""Streamlit-demonstratie. Voorspellen wordt na modeltraining toegevoegd."""

import streamlit as st

st.set_page_config(page_title="Mushroom ML", page_icon="🍄")
st.title("Mushroom Classifier")
st.info("De classificatie-interface wordt gebouwd zodra het model getraind is.")
st.caption(
    "Educatief prototype: niet gebruiken om de eetbaarheid van echte "
    "paddenstoelen te bepalen."
)
