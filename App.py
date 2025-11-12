import streamlit as st
import pandas as pd

# Load your cluster csv
df = pd.read_csv("cluster.csv")

st.title("Customer Clustering & Discount System")

# Input customer ID
customer_id = st.text_input("Enter Customer ID")

# Demo products
products = ["Product A", "Product B"]
product = st.selectbox("Select a product", products)

if st.button("Check Discount"):
    if customer_id in df['CustomerID'].astype(str).values:
        # Get cluster id
        c_id = int(df.loc[df['CustomerID'].astype(str) == customer_id, 'ClusterID'].values[0])
        
        # Discount logic
        if c_id == 3:
            discount = "No discount"
        elif c_id == 1:
            discount = "15% discount"
        elif c_id == 2:
            discount = "10% discount"
        elif c_id == 0:
            discount = "8% discount"
        else:
            discount = "8% discount (New Customer cluster detected)"
        
        st.success(f"Existing customer. Cluster: {c_id}")
        st.info(f"Eligible Discount: **{discount}**")

    else:
        st.warning("New Customer! Assigning new cluster automatically.")
        st.info("Eligible Discount: **8% discount**")
