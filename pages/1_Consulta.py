import streamlit as st
import pandas as pd

st.title("Consulta de Clientes")
st.divider()

lateral = st.sidebar
lateral.text("Páginas disponíveis")

def carregar_arq():
    dados = pd.read_csv('clientes.csv')
    return dados

dados = carregar_arq()
st.dataframe(dados)