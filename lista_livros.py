import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Minha Biblioteca 📚", page_icon="📖")

st.title("📚 Minha Biblioteca de Livros")

# Nome do arquivo onde os dados serão salvos
arquivo = "livros.csv"

# Carregar dados existentes ou criar dataframe vazio
if os.path.exists(arquivo):
    df = pd.read_csv(arquivo)
else:
    df = pd.DataFrame(columns=["Título", "Autor", "Ano", "Status"])

# Formulário para adicionar livros
with st.form("form_livro"):
    st.subheader("Adicionar novo livro")
    titulo = st.text_input("Título")
    autor = st.text_input("Autor")
    ano = st.number_input("Ano", min_value=0, max_value=2100, step=1)
    status = st.selectbox("Status", ["Lido", "Lendo", "Quero ler"])
    adicionar = st.form_submit_button("Adicionar")

    if adicionar:
        if titulo and autor:
            novo_livro = {"Título": titulo, "Autor": autor, "Ano": ano, "Status": status}
            df = pd.concat([df, pd.DataFrame([novo_livro])], ignore_index=True)
            df.to_csv(arquivo, index=False)
            st.success(f"Livro '{titulo}' adicionado!")
            st.rerun()
        else:
            st.error("Por favor, preencha o título e o autor.")

# Mostrar tabela dos livros
st.subheader("📖 Seus livros:")
st.dataframe(df)

# Filtro por status
st.subheader("🔍 Filtrar por status:")
filtro_status = st.multiselect("Selecione o status", options=df["Status"].unique())

if filtro_status:
    st.dataframe(df[df["Status"].isin(filtro_status)])
else:
    st.dataframe(df)

# Opção para limpar todos os dados
if st.button("🗑️ Limpar todos os livros"):
    df = pd.DataFrame(columns=["Título", "Autor", "Ano", "Status"])
    df.to_csv(arquivo, index=False)
    st.success("Todos os livros foram removidos!")
    st.rerun()
