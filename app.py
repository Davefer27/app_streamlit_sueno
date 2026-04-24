#app
import streamlit as st

st.title("¡Hola Mundo! 👋")

st.markdown("""
Este es un espacio de pruebas.

Hemos preparado algunos ejemplos para que descubras
todo lo que puedes hacer con Streamlit.
""")

if st.button("¡Enviar globos! 🎈"):
    st.balloons()