import streamlit as st
import pandas as pd
from datetime import date

# Config Pág

st.set_page_config(
    page_title = "Cadastro de Clientes",
    page_icon = "🤖"
)

lateral = st.sidebar
lateral.text("Páginas disponíveis")

def gravar_dados(nome_cliente, data_nasc, tipo_cliente):
    if nome_cliente and data_nasc <= date.today():
        with open('clientes.csv', 'a', encoding='utf-8') as arq:
            arq.write(f'{nome_cliente}, {data_nasc}, {tipo_cliente}\n')
        st.session_state['sucesso'] = True
    else:
        st.session_state['sucesso'] = False

st.title("Cadastro de Clientes")
st.divider()

# Campos do Cadastro

nome_cliente = st.text_input("Digite o nome do cliente", max_chars = 50, key = 'nome_cliente', placeholder = "Digite o nome completo do cliente")

data_nasc = st.date_input("Data de Nascimento", format = "DD/MM/YYYY")

tipo_cliente = st.selectbox("Tipo do Cliente", ["Pessoa Física", "Pessoa Jurídica"])

btn_cadastro = st.button("Cadastrar", on_click = gravar_dados, args = [nome_cliente, data_nasc, tipo_cliente])

# Validação botão

if btn_cadastro:
    if st.session_state['sucesso']:
        st.success("Cliente cadastrado com sucesso!", icon = "✅")
    else:
        st.error("Erro ao cadastrar o cliente, tente novamente!", icon = "❌")