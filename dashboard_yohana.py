import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(page_title="Dashboard E-commerce by Yohana", page_icon=":bar_chart", layout="wide")
st.title(" :bar_chart: Dashboard E-commerce by Yohana :bar_chart:")
st.header("Dashboard E-Commerce")
st.subheader("Yohana Beatrice Nainggolan, yohanabeatrice1263@gmail.com")
st.subheader("ID: yohanabeatrice")
all_df = pd.read_csv('all_data.csv')

st.title("Sales Dashboard")


st.subheader("Data Overview")
st.dataframe(all_df)

all_df = pd.read_csv('all_data.csv')  

def top_states_bar_plot(data):
    bystate_df = data.groupby(by="city").customer_id.nunique().reset_index()
    bystate_df.rename(columns={"customer_id": "customer_count"}, inplace=True)
    
    top_10_states = bystate_df.sort_values(by="customer_count", ascending=False).head(10)

    plt.figure(figsize=(10, 5))
    colors_ = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
    sns.barplot(x="customer_count", y="city", data=top_10_states, palette=colors_)
    plt.title("Number of Customer by States (Top 10)", loc="center", fontsize=15)
    plt.ylabel(None)
    plt.xlabel(None)
    plt.tick_params(axis='y', labelsize=12)

    return plt


def monthly_orders_bar_plot(data):
    if 'order_approved_at' not in data.columns:
        st.error("Error: 'order_approved_at' column not found in the DataFrame.")
        return None

    data['order_approved_at'] = pd.to_datetime(data['order_approved_at'], errors='coerce')

    data = data.dropna(subset=['order_approved_at'])

    monthly_orders_df = data.resample(rule='M', on='order_approved_at').agg({
        "order_id": "nunique",
        "price": "sum"
    })
    monthly_orders_df.index = monthly_orders_df.index.strftime('%Y-%m')
    monthly_orders_df = monthly_orders_df.reset_index()
    monthly_orders_df.rename(columns={"order_id": "order_count", "price": "revenue"}, inplace=True)

    plt.figure(figsize=(10, 5))

    # membuat bar plot
    plt.bar(monthly_orders_df["order_approved_at"], monthly_orders_df["order_count"], color="#72BCD4", alpha=0.7)

    for i, value in enumerate(monthly_orders_df["order_count"]):
        plt.text(monthly_orders_df["order_approved_at"].iloc[i], value + 50, str(value), ha='center', va='bottom', fontsize=8)

    plt.xticks(monthly_orders_df["order_approved_at"], monthly_orders_df["order_approved_at"], rotation=45, ha='right', fontsize=10)

    # menambah label dan detail
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Number of Orders", fontsize=12)
    plt.title("Number of Orders per Month", loc="center", fontsize=20)

    # menambah grid
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    return plt


# Streamlit App
st.title("Sales Dashboard")
st.subheader("Top 10 States by Customer Count")
top_states_plot = top_states_bar_plot(all_df)
st.pyplot(top_states_plot)

st.subheader("Monthly Orders")
monthly_orders_plot = monthly_orders_bar_plot(all_df)

if monthly_orders_plot:
    st.pyplot(monthly_orders_plot)
else:
    st.warning("Monthly Orders plot could not be generated.")