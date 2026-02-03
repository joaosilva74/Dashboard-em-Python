import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#  Confing. da página
st.set_page_config(page_title="Dashboard Varejo", layout="wide")

#  Página de dados 
df = pd.read_csv('simple_kaggle_dataset.csv')
df['Revenue'] = df['Price'] * df['Quantity_Sold']

# Título do Dashboard 
st.title("Dashboard de Vendas no Varejo")

# Principais Métricas
total_revenue = df['Revenue'].sum()
avg_price = df['Price'].mean()
avg_rating = df['Rating'].mean()
total_sold = df['Quantity_Sold'].sum()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Faturamento Total", f"R$ {total_revenue:,.2f}")
col2.metric("Preço Médio", f"R$ {avg_price:,.2f}")
col3.metric("Avaliação Média", f"{avg_rating:.2f}")
col4.metric("Quantidade Vendida", total_sold)

st.divider()

#  Gráficos
#------------------------
#Linha 1
col5, col6 = st.columns(2)

with col5:
    st.subheader("Faturamento por Categoria")
    revenue_category = df.groupby('Category')['Revenue'].sum()

    fig1, ax1 = plt.subplots(figsize=(5,3))
    revenue_category.plot(
        kind='bar',
        ax=ax1,
        color=['#4CAF50', '#2196F3', '#FF9800']
    )
    ax1.set_xlabel("Categoria")
    ax1.set_ylabel("Faturamento")
    st.pyplot(fig1, use_container_width=False)


with col6:
    st.subheader("Quantidade Vendida por Categoria")
    quantity_category = df.groupby('Category')['Quantity_Sold'].sum()

    fig2, ax2 = plt.subplots(figsize=(5,3))
    quantity_category.plot(
        kind='bar',
        ax=ax2,
        color=['#9C27B0', '#03A9F4', '#FFC107']
    )
    ax2.set_xlabel("Categoria")
    ax2.set_ylabel("Quantidade Vendida")
    st.pyplot(fig2, use_container_width=False)


#Linha 2
col7, col8 = st.columns(2)

with col7:
    st.subheader("Preço vs Quantidade Vendida")

    fig3, ax3 = plt.subplots(figsize=(5,3))
    ax3.scatter(
        df['Price'],
        df['Quantity_Sold'],
        color='#E91E63'
    )
    ax3.set_xlabel("Preço")
    ax3.set_ylabel("Quantidade Vendida")
    st.pyplot(fig3, use_container_width=False)


with col8:
    st.subheader("Avaliação Média por Categoria")
    rating_category = df.groupby('Category')['Rating'].mean()

    fig4, ax4 = plt.subplots(figsize=(5,3))
    rating_category.plot(
        kind='bar',
        ax=ax4,
        color=['#00BCD4', '#8BC34A', '#FF5722']
    )
    ax4.set_xlabel("Categoria")
    ax4.set_ylabel("Avaliação Média")
    st.pyplot(fig4, use_container_width=False)
