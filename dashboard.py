import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Impor semua data yang dibutuhkan dari Google Drive
customers_df = pd.read_csv(
    'https://drive.google.com/uc?id=1bkyvjGOuLX1JnqNil8NpTUQGDxJ5kzyB')
order_items_df = pd.read_csv(
    'https://drive.google.com/uc?id=1X073WBKxBWYRx6T8RSyaNipsOm7M3ByQ')
order_payments_df = pd.read_csv(
    'https://drive.google.com/uc?id=1_RufBMRx7u4pJlE7Gd7k1o9RYHHomroA')
orders_df = pd.read_csv(
    'https://drive.google.com/uc?id=1-MeRdV6SnI0zeleJcixJlEO2u32Ijosu')
products_df = pd.read_csv(
    'https://drive.google.com/uc?id=1VNLJjV35XYRs34DyGfHGa0KEvLIPtzSn')
product_category_name_translation_df = pd.read_csv(
    'https://drive.google.com/uc?id=1DMKWG56iinPGHGC2PUHSoiXSYSX5w0Pn')

# Cleaning Data
# Membersihkan tabel order_items_df
order_items_df['shipping_limit_date'] = pd.to_datetime(order_items_df['shipping_limit_date'])

# Membersihkan tabel orders_df
datetime_columns = ["order_purchase_timestamp",
                    "order_approved_at",
                    "order_delivered_carrier_date",
                    "order_delivered_customer_date",
                    "order_estimated_delivery_date"]
for column in datetime_columns:
  orders_df[column] = pd.to_datetime(orders_df[column])

# Membersihkan tabel products_df
products_df = pd.merge(products_df,
                       product_category_name_translation_df,
                       left_on='product_category_name',
                       right_on='product_category_name',
                       how='left')
products_df['product_category_name'] = (
  products_df['product_category_name_english']
  if products_df['product_category_name_english'] is not None
  else products_df['product_category_name'])
products_df.drop(columns=['product_category_name_english'], inplace=True)

fillna_0_columns = ['product_name_lenght',
                    'product_description_lenght',
                    'product_photos_qty',
                    'product_weight_g',
                    'product_length_cm',
                    'product_height_cm',
                    'product_width_cm']
for column in fillna_0_columns:
  products_df[column] = products_df[column].fillna(0)

integer_columns = ['product_name_lenght',
                   'product_description_lenght',
                   'product_photos_qty']

products_df = products_df.astype(
    {column:'int' for column in integer_columns})

# Exploratory Data Analysis (EDA)
# Explore kategori produk berdasarkan jumlah penjualan yang telah terjadi
order_products_df = pd.merge(order_items_df,
                             products_df,
                             left_on='product_id',
                             right_on='product_id',
                             how='inner')
product_order_counts = order_products_df.groupby(
    by="product_category_name").order_id.count()
product_order_counts.rename("order_count", inplace=True)
product_order_counts = product_order_counts.sort_values(ascending=False)

# Explore jumlah penjualan yang telah terjadi berdasarkan wilayahnya
customer_order_items_df = pd.merge(customers_df,
                                   orders_df,
                                   left_on='customer_id',
                                   right_on='customer_id',
                                   how='inner')
customer_order_items_df = pd.merge(customer_order_items_df,
                                   order_items_df,
                                   left_on='order_id',
                                   right_on='order_id',
                                   how='inner')

order_items_by_city = customer_order_items_df.groupby(
    by="customer_city").order_item_id.count().sort_values(ascending=False)
order_items_by_city.rename("order_count", inplace=True)

order_items_by_state = customer_order_items_df.groupby(
    by="customer_state").order_item_id.count().sort_values(ascending=False)
order_items_by_state.rename("order_count", inplace=True)

# Explore sebaran metode pembayaran yang digunakan dalam data transaksi customer
payment_type_counts = order_payments_df.groupby(
    by="payment_type").order_id.count()
payment_type_counts.rename("order_count", inplace=True)
payment_type_counts = payment_type_counts.sort_values(ascending=False)

payment_installment_counts = order_payments_df.groupby(
    ["payment_type", 'payment_installments']).order_id.count()
payment_installment_counts.rename("order_count", inplace=True)

order_payments_df['payment_installments'] = \
  order_payments_df['payment_installments'].replace(0, 1)

payment_type_counts = order_payments_df.groupby(
    by="payment_type").order_id.count()
payment_type_counts.rename("order_count", inplace=True)
payment_type_counts = payment_type_counts.sort_values(ascending=False)
payment_installment_counts = order_payments_df.groupby(
    ["payment_type", 'payment_installments']).order_id.count()
payment_installment_counts.rename("order_count", inplace=True)



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

# Visualisasi Sebaran Metode Pembayaran
st.header("Number of Customers by Number of Installments")
fig6, ax6 = plt.subplots(figsize=(8, 4))
plt.plot([1, 2, 3, 4, 5, 6],
         [25457, 12413, 10461, 7098, 5239, 3920])
plt.xticks([1, 2, 3, 4, 5, 6])
plt.xlabel("Number of Installments")
plt.ylabel("Number of Customers")
st.pyplot(fig6)