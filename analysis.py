import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
# Create output folder
os.makedirs("outputs", exist_ok=True)

# Load dataset
df = pd.read_excel("dataset.xlsx.xlsx")

print(df.head())
print(df.info())

# Remove missing values
df = df.dropna()

# Create Sales column
if 'Quantity' in df.columns and 'UnitPrice' in df.columns:
    df['Sales'] = df['Quantity'] * df['UnitPrice']

# Product Sales Chart
if 'Product' in df.columns:
    product_sales = df.groupby('Product')['Sales'].sum()

    plt.figure(figsize=(8,5))
    product_sales.sort_values().plot(kind='bar')
    plt.title("Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Total Sales")
    plt.tight_layout()
    plt.savefig("outputs/product_sales.png")
    plt.close()
# Order Status Chart
if 'OrderStatus' in df.columns:
    plt.figure(figsize=(6,6))
    df['OrderStatus'].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title("Order Status Distribution")
    plt.ylabel("")
    plt.savefig("outputs/order_status.png")
    plt.close()

print("Project Completed Successfully")