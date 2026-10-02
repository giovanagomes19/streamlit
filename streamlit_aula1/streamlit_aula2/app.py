import streamlit as st

st.title(" Expresso Mobilidade")
st.header("Painel do Operador")

st.write("Sistema de consulta e gerenciamento das linhas de ônibus.")

# Identificação do operador
nome = st.text_input("Digite seu nome:")

if nome:
    st.write("Olá,", nome, "! Bem-vindo ao painel da Expresso Mobilidade.")

# Consulta de rota
st.subheader(" Consulta de Rota")

linha = st.selectbox(
    "Escolha uma linha:",
    ["510", "520", "550"]
)

st.write("Linha selecionada:", linha)

# Seleção de várias linhas
st.subheader(" Relatório de Linhas")

linhas = st.multiselect(
    "Escolha as linhas para o relatório:",
    ["510", "520", "550", "620"]
)

if linhas:
    st.write("Linhas selecionadas:", linhas)
else:
    st.write("Nenhuma linha selecionada.")

# Cálculo de demanda e frota
st.subheader(" Cálculo de Frota")

if st.button("Calcular"):
    st.write("Calculando...")
    st.success("Cálculo de demanda e distribuição de frota realizado!")