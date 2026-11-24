import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("Libraries imported successfully!")
print("CodeAlpha - Exploratory Data Analysis")

#load retail sales dataset

df = pd.read_csv("data/sample - Superstore.csv", encoding="latin1")

print("\nDataset loaded successfully!")
print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nDataset information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

#data Quality Checks

print("\nMissing Values:")
print(df.isnull().sum())

print("\nTotal Missing Values:")
print(df.isnull().sum().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nDataset Shape Before Cleaning:")
print(df.shape)

#Remove duplicate rows
df = df.drop_duplicates()

print("\nDataset Shape After cleaning:")
print(df.shape)

# Business Questions For EDA

questions = [
    "1. What is the total sales and total profit?",
    "2. Which product category generates the highest sales?",
    "3. Which region generates the highest profit?",
    "4. Which segment contributes the most sales?",
    "5. Which products generate losses?",
    "6. How do monthly sales change over time?",
    "7. What is the relationship between discount and profit?"
]

print("\nBusiness Questions:")
for question in questions:
    print(question)

# Sales and profit Analysis

total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
total_orders = df['Order ID'].nunique()
total_customers = df['Customer ID'].nunique()

print("\n===== Sales Performance  =====")

print("Total Sales:", round(total_sales, 2))
print("Total Profit:", round(total_profit, 2))
print("Total Orders:", total_orders)
print("Total Customers:", total_customers)

# Category-wise Sales and Profit Analysis

category_analysis = df.groupby("Category").agg({
    "Sales": "sum",
    "Profit": "sum",
    "Quantity": "sum"
}).round(2)

print("\n===== Category-wise Analysis =====")
print(category_analysis)

print("\nHighest Sales Category:")
print(category_analysis["Sales"].idxmax())

print("\nHighest Profit Category:")
print(category_analysis["Profit"].idxmax())

# Region-wise Sales and Profit Analysis

region_analysis = df.groupby("Region").agg({
    "Sales": "sum",
    "Profit": "sum",
    "Quantity": "sum"
}).round(2)

print("\n===== Region-wise Analysis =====")
print(region_analysis)

print("\nHighest Sales Region:")
print(region_analysis["Sales"].idxmax())

print("\nHighest Profit Region:")
print(region_analysis["Profit"].idxmax())

print("\nLowest Profit Region:")
print(region_analysis["Profit"].idxmin())

# Segment-wise Sales and Profit Analysis

segment_analysis = df.groupby("Segment").agg({
    "Sales": "sum",
    "Profit": "sum",
    "Quantity": "sum"
}).round(2)

print("\n===== Segment-wise Analysis =====")
print(segment_analysis)

print("\nHighest Sales Segment:")
print(segment_analysis["Sales"].idxmax())

print("\nHighest Profit Segment:")
print(segment_analysis["Profit"].idxmax())

# Monthly Sales Trend Analysis

df["Order Date"]= pd.to_datetime(df["Order Date"])

df["Month"]= df["Order Date"].dt.to_period('M')

monthly_sales = df.groupby("Month")["Sales"].sum()

print("\n===== Monthly Sales Analysis =====")
print(monthly_sales)

print("\nHighest Sales Month:")
print(monthly_sales.idxmax())

print("\nLowest Sales Month:")
print(monthly_sales.idxmin())

# Discount vs Profit Analysis

discount_analysis = df.groupby("Discount").agg({
    "Sales": "sum",
    "Profit": "mean",
    "Quantity": "sum"
}).round(2)

print("\n===== Discount vs Profit Analysis =====")
print(discount_analysis)

print("\nHighest Average Profit Discount:")
print(discount_analysis["Profit"].idxmax())

print("\nLowest Average Profit Discount:")
print(discount_analysis["Profit"].idxmin())

# Category-wise Sales Visualization

plt.figure(figsize=(8, 5))

category_sales = df.groupby("Category")["Sales"].sum()

sns.barplot(x=category_sales.index, y=category_sales.values)

plt.title("Total Sales by Product Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()

plt.savefig("outputs/category_sales.png", dpi=300)
plt.show()

print("\nCategory sales Chart saved successfully!")

# Monthly Sales Trend Visualization

plt.figure(figsize=(12, 6))

monthly_sales = df.groupby(
    df["Order Date"].dt.to_period("M")
)["Sales"].sum()

sns.lineplot(
    x=monthly_sales.index.astype(str),
    y=monthly_sales.values,
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=90)

plt.tight_layout()
plt.savefig("outputs/monthly_sales_trend.png", dpi=300)
plt.show()

print("\nMonthly sales trend Chart saved successfully!")

# Discount vs Profit Visualization

plt.figure(figsize=(9, 5))

sns.scatterplot(
    data=df,
    x="Discount",
    y="Profit",
    alpha=0.5
)

plt.title("Relationship between Discount and Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.axhline(y=0, linestyle="--")

plt.tight_layout()
plt.savefig("outputs/discount_vs_profit.png", dpi=300)
plt.show()


# Correlation Heatmap

plt.figure(figsize=(9, 6))

numeric_df = df.select_dtypes(include=["number"])

correlation = numeric_df.corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)

plt.title("Correlation Heatmap of Retail Sales Data")

plt.tight_layout()
plt.savefig("outputs/correlation_heatmap.png", dpi=300)
plt.show()

print("\nCorrelation Heatmap saved successfully!")


# Statistical Hypothesis Testing

from scipy.stats import ttest_ind

# Divide data into two groups
no_discount = df[df["Discount"] == 0]["Profit"]
high_discount = df[df["Discount"] > 0.20]["Profit"]

# Perform Welch's t-test
t_stat, p_value = ttest_ind(
    no_discount,
    high_discount,
    equal_var=False
)

print("\n===== HYPOTHESIS TESTING =====")

print("Average Profit (No Discount):", round(no_discount.mean(), 2))
print("Average Profit (High Discount):", round(high_discount.mean(), 2))

print("T-Statistic:", round(t_stat, 4))
print("P-Value:", p_value)

if p_value < 0.05:
    print("Result: Reject Null Hypothesis")
    print("There is a statistically significant difference.")
else:
    print("Result: Fail to Reject Null Hypothesis")
    print("There is not enough evidence of a significant difference.")


# Final Business Insights

print("\n========== FINAL BUSINESS INSIGHTS ==========")

# 1. Total Performance
print("\n1. Overall Performance")
print("Total Sales:", round(df["Sales"].sum(), 2))
print("Total Profit:", round(df["Profit"].sum(), 2))

# 2. Best Category
best_category = df.groupby("Category")["Sales"].sum().idxmax()
print("\n2. Best Performing Category:", best_category)

# 3. Best Region
best_region = df.groupby("Region")["Profit"].sum().idxmax()
print("\n3. Most Profitable Region:", best_region)

# 4. Best Customer Segment
best_segment = df.groupby("Segment")["Sales"].sum().idxmax()
print("\n4. Highest Sales Segment:", best_segment)

# 5. Loss Making Transactions
loss_count = (df["Profit"] < 0).sum()
print("\n5. Loss Making Transactions:", loss_count)

# 6. Discount Observation
print("\n6. Average Profit:", round(df["Profit"].mean(), 2))

print("\nEDA Analysis Completed Successfully!")

# Region-wise Profit Chart

plt.figure(figsize=(8, 5))

sns.barplot(
    data=df,
    x="Region",
    y="Profit",
    estimator=sum
)

plt.title("Region-wise Total Profit")
plt.xlabel("Region")
plt.ylabel("Total Profit")
plt.tight_layout()

plt.savefig("outputs/region_profit.png", dpi=300)
plt.show()