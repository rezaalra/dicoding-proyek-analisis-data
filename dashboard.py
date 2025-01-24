import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Impor semua data yang dibutuhkan dari Google Drive
customers_df = pd.read_csv('https://drive.google.com/uc?id=1bkyvjGOuLX1JnqNil8NpTUQGDxJ5kzyB')

# Placeholder: Simulasi data berdasarkan insight yang ada
# Data penjualan terbaik berdasarkan kategori
best_selling_products = pd.DataFrame({
    "Category": ['bed_bath_table', 'health_beauty', 'sports_leisure',
    'furniture_decor', 'computers_accessories', 'housewares', 'watches_gifts',
    'telephony', 'garden_tools', 'auto'],
    "Sales": [11115, 9670, 8641, 8334, 7827, 6964, 5991, 4545, 4347, 4235]
})

# Data penjualan terburuk berdasarkan kategori
worst_selling_products = pd.DataFrame({
    "Category": ['security_and_services', 'fashion_childrens_clothes',
    'cds_dvds_musicals', 'la_cuisine', 'arts_and_craftmanship',
    'home_comfort_2', 'fashion_sport', 'flowers', 'music',
    'furniture_mattress_and_upholstery'],
    "Sales": [2, 8, 14, 14, 24, 30, 30, 33, 38, 38]
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

st.set_page_config(
    page_title="Dashboard E-commerce by Reza",
    page_icon=":bar_chart",
    layout="wide")
st.title(":bar_chart: Dashboard E-commerce by Reza")
st.subheader("Nama: Muhamad Reza Al Ramadhan")
st.subheader("Email: rezaalramadhan@gmail.com")
st.subheader("ID: https://www.dicoding.com/users/reza_al_ramadhan/")

# Visualisasi Penjualan terbaik Berdasarkan Kategori Produk
st.header("Best Selling Products")
fig1, ax1 = plt.subplots(figsize=(8, 4))
colors = ["#00FF57"] + ["#D3D3D3"] * (len(best_selling_products) - 1)
sns.barplot(
    data=best_selling_products,
    x="Sales",
    y="Category",
    ax=ax1,
    palette=colors)
ax1.set_xlabel("Sales")
ax1.set_ylabel("Category")
st.pyplot(fig1)

# Visualisasi Penjualan terburuk Berdasarkan Kategori Produk
st.header("Worst Selling Products")
fig2, ax2 = plt.subplots(figsize=(8, 4))
colors = ["#F90611"] + ["#D3D3D3"] * (len(worst_selling_products) - 1)
sns.barplot(
    data=worst_selling_products,
    x="Sales",
    y="Category",
    ax=ax2,
    palette=colors)
ax2.set_xlabel("Sales")
ax2.set_ylabel("Category")
ax2.invert_xaxis()
ax2.yaxis.set_label_position("right")
ax2.yaxis.tick_right()
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