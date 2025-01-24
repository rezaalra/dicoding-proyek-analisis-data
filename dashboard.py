import gdown
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(
    page_title="Dashboard E-commerce by Reza",
    page_icon=":bar_chart",
    layout="wide")
st.title(":bar_chart: Dashboard E-commerce by Reza")
st.subheader("Nama: Muhamad Reza Al Ramadhan")
st.subheader("Email: rezaalramadhan@gmail.com")
st.subheader("ID: https://www.dicoding.com/users/reza_al_ramadhan/")

# Placeholder: Simulasi data berdasarkan insight yang ada
# Data penjualan berdasarkan kategori
df_category_sales = pd.DataFrame({
    "Category": ["bed bath table", "security and services", "furniture", "electronics"],
    "Sales": [2000, 500, 1500, 1200]
})

# Data penjualan berdasarkan wilayah (kota)
df_city_sales = pd.DataFrame({
    "City": ["Sao Paulo", "Rio de Janeiro", "Belo Horizonte"],
    "Sales": [5000, 3000, 1500]
})

# Data metode pembayaran
df_payment_methods = pd.DataFrame({
    "Method": ["credit_card", "boleto", "voucher", "debit_card", "not_defined"],
    "Usage": [76795, 19784, 5775, 1529, 3]
})

# Visualisasi Penjualan terbaik Berdasarkan Kategori Produk
st.header("Best Selling Products")
fig1, ax1 = plt.subplots(figsize=(8, 4))
colors = ["#00FF57"] + ["#D3D3D3"] * (len(df_category_sales) - 1)
sns.barplot(
    data=df_category_sales,
    x="Sales",
    y="Category",
    ax=ax1,
    palette=colors)
ax1.set_xlabel("Sales")
ax1.set_ylabel("Category")
st.pyplot(fig1)

# Visualisasi Penjualan terbaik Berdasarkan Kategori Produk
st.header("Worst Selling Products")
fig2, ax2 = plt.subplots(figsize=(8, 4))
colors = ["#F90611"] + ["#D3D3D3"] * (len(df_category_sales) - 1)
sns.barplot(
    data=df_category_sales,
    x="Sales",
    y="Category",
    ax=ax2,
    palette=colors)
ax2.set_xlabel("Sales")
ax2.set_ylabel("Category")
st.pyplot(fig2)

# Visualisasi Penjualan Berdasarkan Wilayah Kota Customer
st.header("Number of Orders by City")
fig3, ax3 = plt.subplots(figsize=(8, 4))
colors = ["#00FF57"] + ["#D3D3D3"] * (len(df_city_sales) - 1)
sns.barplot(
    data=df_city_sales,
    x="Sales",
    y="City",
    ax=ax3,
    palette=colors)
ax3.set_xlabel("Sales")
ax3.set_ylabel("City")
st.pyplot(fig3)

# Visualisasi Penjualan Berdasarkan Wilayah State Customer
st.header("Number of Orders by State")
fig4, ax4 = plt.subplots(figsize=(8, 4))
colors = ["#00FF57"] + ["#D3D3D3"] * (len(df_city_sales) - 1)
sns.barplot(
    data=df_city_sales,
    x="Sales",
    y="City",
    ax=ax4,
    palette=colors)
ax4.set_xlabel("Sales")
ax4.set_ylabel("City")
st.pyplot(fig4)

# Visualisasi Sebaran Metode Pembayaran
st.header("Number of Customers by Payment Method")
fig5, ax5 = plt.subplots(figsize=(8, 4))
colors = ["#00FF57"] + ["#D3D3D3"] * (len(df_payment_methods) - 1)
sns.barplot(
    data=df_payment_methods,
    x="Usage",
    y="Method",
    ax=ax5,
    palette=colors)
ax5.set_xlabel("Usage")
ax5.set_ylabel("Method")
st.pyplot(fig5)