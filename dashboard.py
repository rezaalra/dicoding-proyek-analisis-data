import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Placeholder: Ganti ini dengan data sebenarnya dari notebook
# Simulasi data berdasarkan insight yang ada
data_segments = {
    "Segment": [
        "Active Big Spenders",
        "High Value Lost Customers",
        "Low Value Lost Customers",
        "High Value Recent Customers",
        "Low Value Recent Customers",
        "Frequent Customers",
        "Others"
    ],
    "Percentage": [22.96, 22.86, 16.93, 7.20, 16.09, 1.97, 11.95]
}

# Simulasi data penjualan berdasarkan kategori
category_sales = {
    "Category": ["bed bath table", "security and services", "furniture", "electronics"],
    "Sales": [2000, 500, 1500, 1200]
}

# Simulasi data penjualan berdasarkan kota
city_sales = {
    "City": ["Sao Paulo", "Rio de Janeiro", "Belo Horizonte"],
    "Sales": [5000, 3000, 1500]
}

# Simulasi data metode pembayaran
payment_methods = {
    "Method": ["Credit Card", "Boleto", "Debit Card"],
    "Usage": [60, 30, 10]
}

# Konversi ke DataFrame
df_segments = pd.DataFrame(data_segments)
df_category_sales = pd.DataFrame(category_sales)
df_city_sales = pd.DataFrame(city_sales)
df_payment_methods = pd.DataFrame(payment_methods)

# Dashboard Streamlit
st.title("Dashboard Penjualan")
st.header("Segmen Pelanggan")

# Pie chart untuk Segmen Pelanggan
fig1, ax1 = plt.subplots()
ax1.pie(
    df_segments["Percentage"], 
    labels=df_segments["Segment"], 
    autopct="%1.1f%%", 
    startangle=90
)
ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig1)

st.header("Penjualan Berdasarkan Kategori")
# Bar chart untuk kategori produk
fig2, ax2 = plt.subplots()
ax2.bar(
    df_category_sales["Category"], 
    df_category_sales["Sales"], 
    color="skyblue"
)
ax2.set_ylabel("Sales")
ax2.set_xlabel("Category")
ax2.set_title("Sales by Category")
st.pyplot(fig2)

st.header("Penjualan Berdasarkan Kota")
# Bar chart untuk penjualan berdasarkan kota
fig3, ax3 = plt.subplots()
ax3.bar(
    df_city_sales["City"], 
    df_city_sales["Sales"], 
    color="green"
)
ax3.set_ylabel("Sales")
ax3.set_xlabel("City")
ax3.set_title("Sales by City")
st.pyplot(fig3)

st.header("Metode Pembayaran")
# Bar chart untuk metode pembayaran
fig4, ax4 = plt.subplots()
ax4.bar(
    df_payment_methods["Method"], 
    df_payment_methods["Usage"], 
    color="orange"
)
ax4.set_ylabel("Usage (%)")
ax4.set_xlabel("Payment Method")
ax4.set_title("Payment Methods Usage")
st.pyplot(fig4)

st.write("\n\nData yang ditampilkan merupakan simulasi berdasarkan insight dari file notebook. Silakan integrasikan dengan data asli.")