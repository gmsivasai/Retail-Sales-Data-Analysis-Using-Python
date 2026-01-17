import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("retail_sales_dataset.csv")

# Rename columns
df = df.rename(columns={
    "Transaction ID": "transaction_id",
    "Date": "transaction_date",
    "Customer ID": "customer_id",
    "Gender": "gender",
    "Age": "age",
    "Product Category": "product_category",
    "Quantity": "quantity",
    "Price per Unit": "price_per_unit",
    "Total Amount": "total_amount"
})

# Handle missing values using NumPy
df['total_amount'] = df['total_amount'].fillna(np.mean(df['total_amount']))

# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert date
df['transaction_date'] = pd.to_datetime(df['transaction_date'])

# Feature engineering
df['Month'] = df['transaction_date'].dt.month
df['Year'] = df['transaction_date'].dt.year

# =========================
# NUMPY USAGE (IMPORTANT)
# =========================

# 1️⃣ Create Age Groups using NumPy
age_bins = np.array([0, 18, 30, 45, 60, 100])
age_labels = ['<18', '18-30', '31-45', '46-60', '60+']
df['age_group'] = pd.cut(df['age'], bins=age_bins, labels=age_labels)

# 2️⃣ High-value transaction threshold (95th percentile)
high_value_threshold = np.percentile(df['total_amount'], 95)
df['high_value_transaction'] = np.where(
    df['total_amount'] > high_value_threshold, 'Yes', 'No'
)

# 3️⃣ Basic statistics using NumPy
avg_sales = np.mean(df['total_amount'])
std_sales = np.std(df['total_amount'])

print("Average Transaction Value:", avg_sales)
print("Transaction Value Std Dev:", std_sales)

# =========================
# ANALYSIS & VISUALIZATION
# =========================

# 🔹 Sales by Product Category
category_sales = df.groupby('product_category')['total_amount'].sum()

plt.figure()
category_sales.plot(kind='bar')
plt.title("Total Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# 🔹 Monthly Sales Trend
monthly_sales = df.groupby('Month')['total_amount'].sum()

plt.figure()
plt.plot(monthly_sales, marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# 🔹 Transaction Amount Distribution
plt.figure()
plt.hist(df['total_amount'], bins=30)
plt.title("Transaction Amount Distribution")
plt.xlabel("Total Amount")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
