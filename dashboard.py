import gdown
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Halaman depan
st.set_page_config(
    page_title="Dashboard E-commerce by Reza",
    page_icon=":bar_chart",
    layout="wide")
st.title(":bar_chart: Dashboard E-commerce by Reza")
st.markdown("""
    **Nama:** Muhamad Reza Al Ramadhan
    **Email:** rezaalramadhan@gmail.com
    **ID Dicoding:** https://www.dicoding.com/users/reza_al_ramadhan/""")

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

# **1. Visualisasi Penjualan Berdasarkan Kategori Produk**
fig1, ax1 = plt.subplots()
ax1.bar(
    df_category_sales["Sales"], 
    df_category_sales["Category"], 
    color="skyblue"
)
ax1.set_ylabel("Jumlah Penjualan")
ax1.set_xlabel("Kategori Produk")
ax1.set_title("Penjualan per Kategori")
st.pyplot(fig1)

# **2. Visualisasi Penjualan Berdasarkan Wilayah Customer**
fig2, ax2 = plt.subplots()
ax2.bar(
    df_city_sales["Sales"], 
    df_city_sales["City"], 
    color="green"
)
ax2.set_ylabel("Jumlah Penjualan")
ax2.set_xlabel("Wilayah (Kota)")
ax2.set_title("Penjualan per Wilayah")
st.pyplot(fig2)

# **3. Visualisasi Penjualan Berdasarkan Metode Pembayaran**
fig3, ax3 = plt.subplots()
ax3.bar(
    df_payment_methods["Usage"], 
    df_payment_methods["Method"], 
    color="orange"
)
ax3.set_ylabel("Persentase Penggunaan")
ax3.set_xlabel("Metode Pembayaran")
ax3.set_title("Penggunaan Metode Pembayaran")
st.pyplot(fig3)