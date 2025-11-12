# Mall-Customer-Cluster
A small project that uses K-Means clustering to group customers and a Streamlit UI to check discounts based on Customer ID. If the customer exists, the app shows their cluster and discount. If the customer is new, it assigns the default discount and displays it.


#preview

<img width="1124" height="551" alt="Screenshot 2025-11-12 141524" src="https://github.com/user-attachments/assets/486b3358-6564-470d-ab79-f602e3aa9eff" />
<img width="1132" height="480" alt="Screenshot 2025-11-12 141603" src="https://github.com/user-attachments/assets/0c265d60-5fa2-48da-8061-5995c6e99bd6" />


Customer Clustering with K-Means & Streamlit

This project uses K-Means clustering to group customers and provides a simple Streamlit UI to check discounts based on customer ID.

✅ How it works

Enter a Customer ID

If the ID exists in cluster.csv, the app shows:

Cluster number

Discount percentage

If the ID is not found, the app treats the user as a new customer and gives a default discount

Includes two demo product options to simulate purchase

✅ Discount Rules
Cluster	Discount
1	15%
2	10%
0	8%
3	0%
New Customer	8%
🚀 Run the App
pip install streamlit pandas
streamlit run app.py

📁 Files

cluster.csv – Customer & cluster data

app.py – Streamlit UI logic
