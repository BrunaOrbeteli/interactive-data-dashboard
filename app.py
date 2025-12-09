import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Interactive Data Dashboard", layout="wide")

st.title("Interactive Data Dashboard")
st.write("Faça upload de um CSV para explorar os dados.")

file = st.file_uploader("Escolha um arquivo CSV", type=["csv"])

if file is not None:
    df = pd.read_csv(file)
    st.subheader("Pré-visualização")
    st.dataframe(df.head())

    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    if numeric_cols:
        x = st.selectbox("Eixo X", options=df.columns, index=0)
        y = st.selectbox("Eixo Y", options=numeric_cols, index=0)
        fig = px.line(df, x=x, y=y)
        st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Aguardando upload de arquivo.")
