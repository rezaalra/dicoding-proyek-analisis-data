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

# Membersihkan tabel order_payments_df
order_payments_df['payment_installments'] = \
  order_payments_df['payment_installments'].replace(0, 1)

# Join semua data yang perlukan
order_products_df = pd.merge(orders_df,
                             order_items_df,
                             left_on='order_id',
                             right_on='order_id',
                             how='inner')
order_products_df = pd.merge(order_products_df,
                             products_df,
                             left_on='product_id',
                             right_on='product_id',
                             how='inner')
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
order_payment_dates_df = pd.merge(orders_df,
                                  order_payments_df,
                                  left_on='order_id',
                                  right_on='order_id',
                                  how='inner')

def product_order_counts_pivot(start_date, end_date):
    product_order_counts = order_products_df[
        (order_products_df.order_purchase_timestamp >= start_date) &
        (order_products_df.order_purchase_timestamp <= end_date)]
    product_order_counts = product_order_counts.groupby(
        by="product_category_name").order_id.count().sort_values(ascending=False)
    product_order_counts.rename("order_count", inplace=True)
    return product_order_counts

def order_items_by_city_pivot(start_date, end_date):
    order_items_by_city = customer_order_items_df[
        (customer_order_items_df.order_purchase_timestamp >= start_date) &
        (customer_order_items_df.order_purchase_timestamp <= end_date)]
    order_items_by_city = order_items_by_city.groupby(
        by="customer_city").order_item_id.count().sort_values(ascending=False)
    order_items_by_city.rename("order_count", inplace=True)
    return order_items_by_city

def order_items_by_state_pivot(start_date, end_date):
    order_items_by_state = customer_order_items_df[
        (customer_order_items_df.order_purchase_timestamp >= start_date) &
        (customer_order_items_df.order_purchase_timestamp <= end_date)]
    order_items_by_state = order_items_by_state.groupby(
        by="customer_state").order_item_id.count().sort_values(ascending=False)
    order_items_by_state.rename("order_count", inplace=True)
    return order_items_by_state

def payment_type_counts_pivot(start_date, end_date):
    payment_type_counts = order_payment_dates_df[
        (order_payment_dates_df.order_purchase_timestamp >= start_date) &
        (order_payment_dates_df.order_purchase_timestamp <= end_date)]
    payment_type_counts = payment_type_counts.groupby(
        by="payment_type").order_id.count().sort_values(ascending=False)
    payment_type_counts.rename("order_count", inplace=True)
    return payment_type_counts

def payment_installment_counts_pivot(start_date, end_date):
    payment_installment_counts = order_payment_dates_df[
        (order_payment_dates_df.order_purchase_timestamp >= start_date) &
        (order_payment_dates_df.order_purchase_timestamp <= end_date)]
    payment_installment_counts = payment_installment_counts[
        payment_installment_counts.payment_type == 'credit_card']
    payment_installment_counts = payment_installment_counts.groupby(
        by='payment_installments').order_id.count()
    payment_installment_counts.rename("order_count", inplace=True)
    return payment_installment_counts

# Visualisasi Penjualan terbaik Berdasarkan Kategori Produk
def show_best_selling_products(best_selling_products):
    st.header("Best Selling Products")
    data_length = len(worst_selling_products)
    if (data_length == 0):
        st.write('Data visualization cannot be displayed because there are no matching data records.')
        return None
    fig1, ax1 = plt.subplots(figsize=(8, 4))
    colors = ["#00FF57"] + ["#D3D3D3"] * (data_length - 1)
    sns.barplot(
        data=best_selling_products,
        x="order_count",
        y="product_category_name",
        ax=ax1,
        palette=colors)
    ax1.set_xlabel("Sales")
    ax1.set_ylabel("Category")
    st.pyplot(fig1)

# Visualisasi Penjualan terburuk Berdasarkan Kategori Produk
def show_worst_selling_products(worst_selling_products):
    st.header("Worst Selling Products")
    data_length = len(worst_selling_products)
    if (data_length == 0):
        st.write('Data visualization cannot be displayed because there are no matching data records.')
        return None
    fig2, ax2 = plt.subplots(figsize=(8, 4))
    colors = ["#F90611"] + ["#D3D3D3"] * (data_length - 1)
    sns.barplot(
        data=worst_selling_products,
        x="order_count",
        y="product_category_name",
        ax=ax2,
        palette=colors)
    ax2.set_xlabel("Sales")
    ax2.set_ylabel("Category")
    ax2.invert_xaxis()
    ax2.yaxis.set_label_position("right")
    ax2.yaxis.tick_right()
    st.pyplot(fig2)

# Visualisasi Penjualan Berdasarkan Wilayah Kota Customer
def show_city_sales(city_sales_df):
    st.header("Number of Orders by City")
    data_length = len(city_sales_df)
    if (data_length == 0):
        st.write('Data visualization cannot be displayed because there are no matching data records.')
        return None
    fig3, ax3 = plt.subplots(figsize=(8, 4))
    colors = ["#00FF57"] + ["#D3D3D3"] * (data_length - 1)
    sns.barplot(
        data=city_sales_df,
        x="order_count",
        y="customer_city",
        ax=ax3,
        palette=colors)
    ax3.set_xlabel("Sales")
    ax3.set_ylabel("City")
    st.pyplot(fig3)

# Visualisasi Penjualan Berdasarkan Wilayah State Customer
def show_state_sales(state_sales_df):
    st.header("Number of Orders by State")
    data_length = len(state_sales_df)
    if (data_length == 0):
        st.write('Data visualization cannot be displayed because there are no matching data records.')
        return None
    fig4, ax4 = plt.subplots(figsize=(8, 4))
    colors = ["#00FF57"] + ["#D3D3D3"] * (data_length - 1)
    sns.barplot(
        data=state_sales_df,
        x="order_count",
        y="customer_state",
        ax=ax4,
        palette=colors)
    ax4.set_xlabel("Sales")
    ax4.set_ylabel("City")
    st.pyplot(fig4)

# Visualisasi Sebaran Metode Pembayaran
def show_payment_methods(payment_methods_df):
    st.header("Number of Customers by Payment Method")
    data_length = len(payment_methods_df)
    if (data_length == 0):
        st.write('Data visualization cannot be displayed because there are no matching data records.')
        return None
    fig5, ax5 = plt.subplots(figsize=(8, 4))
    colors = ["#00FF57"] + ["#D3D3D3"] * (data_length - 1)
    sns.barplot(
        data=payment_methods_df,
        x="order_count",
        y="payment_type",
        ax=ax5,
        palette=colors)
    ax5.set_xlabel("Usage")
    ax5.set_ylabel("Method")
    st.pyplot(fig5)

# Visualisasi Sebaran Metode Pembayaran
def show_payment_installment_methods(payment_installment_credit_card_plot):
    st.header("Number of Customers by Number of Installments")
    data_length = len(payment_installment_credit_card_plot)
    if (data_length == 0):
        st.write('Data visualization cannot be displayed because there are no matching data records.')
        return None
    fig6, ax6 = plt.subplots(figsize=(8, 4))
    plt.plot(payment_installment_credit_card_plot["payment_installments"],
            payment_installment_credit_card_plot["order_count"])
    plt.xticks(payment_installment_credit_card_plot["payment_installments"])
    plt.xlabel("Number of Installments")
    plt.ylabel("Number of Customers")
    st.pyplot(fig6)

# Header
st.set_page_config(
    page_title="Dashboard E-commerce by Reza",
    page_icon=":bar_chart",
    layout="wide")
st.title(":bar_chart: Dashboard E-commerce by Reza")
st.subheader("Nama: Muhamad Reza Al Ramadhan")
st.subheader("Email: rezaalramadhan@gmail.com")
st.subheader("ID: https://www.dicoding.com/users/reza_al_ramadhan/")

# Date Filter
st.subheader("Filter:")
earliest_date = orders_df.order_purchase_timestamp.min()
last_date  = orders_df.order_purchase_timestamp.max()
start_date = st.date_input(
    label="Start Date", 
    value=earliest_date,
    min_value=earliest_date,
    max_value=last_date)
end_date = st.date_input(
    label="End Date",
    value=last_date,
    min_value=earliest_date,
    max_value=last_date)

# Data penjualan berdasarkan kategori
product_order_counts = product_order_counts_pivot(
    pd.to_datetime(start_date), pd.to_datetime(end_date))

# Data penjualan terbaik berdasarkan kategori
best_selling_products = product_order_counts.reset_index().head(10)

# Data penjualan terburuk berdasarkan kategori
worst_selling_products = product_order_counts.reset_index().tail(10)[::-1]

# Data penjualan berdasarkan wilayah (kota)
city_sales_df = order_items_by_city_pivot(
    pd.to_datetime(start_date), pd.to_datetime(end_date)).reset_index().head(10)

# Data penjualan berdasarkan wilayah (state)
state_sales_df = order_items_by_state_pivot(
    pd.to_datetime(start_date), pd.to_datetime(end_date)).reset_index().head(10)

# Data metode pembayaran
payment_methods_df = payment_type_counts_pivot(
    pd.to_datetime(start_date), pd.to_datetime(end_date)).reset_index()

# Data metode pembayaran berdasarkan cicilan credit card
payment_installment_credit_card_plot = payment_installment_counts_pivot(
    pd.to_datetime(start_date), pd.to_datetime(end_date)).reset_index()

# Visualisasi semua data
show_best_selling_products(best_selling_products)
show_worst_selling_products(worst_selling_products)
show_city_sales(city_sales_df)
show_state_sales(state_sales_df)
show_payment_methods(payment_methods_df)
show_payment_installment_methods(payment_installment_credit_card_plot)