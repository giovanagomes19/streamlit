import streamlit as st
import pandas as pd

nome = "Giovana"
idade = 17

st.write("Olá, mundo")
st.write(nome)
st.write(idade)

df = pd.DataFrame({
    "Matéria": ["Português", "Matemática", "Python", "Frame"],
    "Nota": [5, 9, 7, 10]
})

st.title("Meu primeiro dash")
st.subheader("Giovana")

st.write(df)