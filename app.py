import streamlit as st
from email_graph import criar_app

st.set_page_config(page_title="Multi-Agentes Email")

st.title("📧 Escrita de Email com Multi-Agentes")

tom = st.selectbox(
    "Escolha o tom:",
    ["Formal", "Amigável", "Técnico"]
)

tema = st.text_area("Descreva o email:")

if st.button("Gerar"):

    app = criar_app()

    estado = {
        "tema": tema,
        "tom": tom,
        "plano": "",
        "email": "",
        "avaliacao": "",
        "aprovado": False,
        "historico": []
    }

    resultado = app.invoke(estado)

    st.subheader("EMAIL FINAL")
    st.write(resultado["email"])

    st.subheader("AVALIAÇÃO")
    st.write(resultado["avaliacao"])

    st.subheader("HISTÓRICO")

    for etapa, conteudo in resultado["historico"]:
        with st.expander(etapa):
            st.write(conteudo)