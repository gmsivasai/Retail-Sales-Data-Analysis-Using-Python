📊 Retail Sales Data Analysis Using Python
📌 Project Overview

This project performs Exploratory Data Analysis (EDA) on a retail sales dataset using Python.
The goal is to clean raw transaction data, analyze customer and product trends, and generate business insights using data visualization.

The project is implemented in VS Code using Pandas, NumPy, and Matplotlib.

🎯 Objectives

Understand sales performance across product categories

Analyze monthly sales trends

Identify high-value transactions

Perform customer segmentation based on age

Visualize insights for business decision-making

🛠 Tools & Technologies

Python 3

Pandas

NumPy

Matplotlib

Visual Studio Code

📂 Dataset Description

File name: retail_sales_dataset.csv

Columns Used:
Column Name	Description
Transaction ID	Unique transaction identifier
Date	Date of transaction
Customer ID	Unique customer identifier
Gender	Customer gender
Age	Customer age
Product Category	Category of product purchased
Quantity	Number of items purchased
Price per Unit	Price of one unit
Total Amount	Total transaction value
🧹 Data Cleaning Steps

Renamed columns to Python-friendly snake_case format

Handled missing values in total_amount using average value

Removed duplicate records

Converted date column to proper datetime format

🧠 Feature Engineering

Extracted Month and Year from transaction date

Created Age Groups using NumPy

Identified High-Value Transactions using 95th percentile threshold

📊 Data Analysis & Visualization

The following analyses were performed:

Total sales by product category (Bar chart)

Monthly sales trend (Line chart)

Distribution of transaction values (Histogram)

All visualizations were created using Matplotlib.

🔍 Key Insights

Certain product categories contribute the majority of total revenue

Monthly sales show clear seasonal patterns

A small percentage of transactions generate significantly high revenue

Most customers fall within specific age groups with consistent spending behavior

▶️ How to Run the Project

Clone or download the project folder

Open the folder in VS Code

Install required libraries:

pip install pandas numpy matplotlib


Run the Python script:

python sales_eda.py

🗣 Interview Explanation (Short)

“I analyzed retail sales data using Python, cleaned and transformed the dataset, engineered time and customer features, and visualized trends to derive actionable business insights.”

📌 Future Enhancements

Customer lifetime value analysis

Correlation analysis between quantity and revenue

Exporting cleaned data for Power BI dashboard

👤 Author

Siva
Aspiring Data Analyst
