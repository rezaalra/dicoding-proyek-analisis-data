import gdown
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(
    page_title="Dashboard E-commerce by Reza",
    page_icon=":bar_chart", layout="wide")
st.title(":bar_chart: Dashboard E-commerce by Reza")
st.header("Proyek Analisis Data: E-Commerce Public Dataset")
st.subheader("Muhamad Reza Al Ramadhan, rezaalramadhan@gmail.com")
st.subheader("ID: https://www.dicoding.com/users/reza_al_ramadhan/")

# Dashboard penjualan berdasarkan metode pembayaran
payment_type_counts = pd.DataFrame({
    "Method": ["credit_card", "boleto", "voucher", "debit_card", "not_defined"],
    "Usage": [76795, 19784, 5775, 1529, 3]
})

plt.figure(figsize=(12, 6))
colors= ["#00FF57"] + ["#D3D3D3"] * (len(payment_type_counts) - 1)
sns.barplot(data=payment_type_counts,
            x="order_count",
            y="payment_type",
            palette=colors)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='both', labelsize=12)
plt.show()