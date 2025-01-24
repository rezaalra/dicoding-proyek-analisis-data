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

def plot_bar_chart(data, x_col, y_col, title, x_label, y_label, palette, figsize):
    """
    Fungsi untuk membuat bar chart menggunakan Seaborn.
    
    Parameters:
        data (DataFrame): Data untuk visualisasi.
        x_col (str): Kolom untuk sumbu x.
        y_col (str): Kolom untuk sumbu y.
        title (str): Judul grafik.
        x_label (str): Label untuk sumbu x.
        y_label (str): Label untuk sumbu y.
        colors (str): Warna bar chart.
        figsize (tuple): Ukuran figure (lebar, tinggi).
    """
    fig, ax = plt.subplots(figsize=figsize)
    sns.barplot(data=data, x=x_col, y=y_col, ax=ax, palette=palette)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    st.pyplot(fig)

# Visualisasi Penjualan Berdasarkan Kategori Produk
st.header("Penjualan Berdasarkan Kategori Produk")
plot_bar_chart(
    data=df_category_sales,
    x_col="Category",
    y_col="Sales",
    title="Penjualan per Kategori",
    x_label="Kategori Produk",
    y_label="Jumlah Penjualan",
    palette=["#00FF57"] + ["#D3D3D3"] * (len(df_category_sales) - 1),
    figsize=(8, 4)
)

# Visualisasi Penjualan Berdasarkan Wilayah Customer
st.header("Penjualan Berdasarkan Wilayah Customer")
plot_bar_chart(
    data=df_city_sales,
    x_col="City",
    y_col="Sales",
    title="Penjualan per Wilayah",
    x_label="Wilayah (Kota)",
    y_label="Jumlah Penjualan",
    palette=["#00FF57"] + ["#D3D3D3"] * (len(df_city_sales) - 1),
    figsize=(8, 4)
)

# Visualisasi Penjualan Berdasarkan Metode Pembayaran
st.header("Penjualan Berdasarkan Metode Pembayaran")
plot_bar_chart(
    data=df_payment_methods,
    x_col="Usage",
    y_col="Method",
    title="Penggunaan Metode Pembayaran",
    x_label="Metode Pembayaran",
    y_label="Persentase Penggunaan",
    palette=["#00FF57"] + ["#D3D3D3"] * (len(df_payment_methods) - 1),
    figsize=(8, 4)
)

# Visualisasi Sebaran Metode Pembayaran
st.header("Number of Customers by Payment Method")
fig4, ax4 = plt.subplots(figsize=(8, 4))
colors = ["#00FF57"] + ["#D3D3D3"] * (len(df_payment_methods) - 1)
sns.barplot(
    data=df_payment_methods,
    x="Usage",
    y="Method",
    ax=ax4,
    palette=colors)
ax4.set_xlabel("Usage")
ax4.set_ylabel("Method")
st.pyplot(fig4)