
# Retail Sales Exploratory Data Analysis (EDA)

## Project Overview
This project performs Exploratory Data Analysis (EDA) on the Sample Superstore dataset to understand sales, profit, customer segments, product categories, regional performance, and discount patterns.

## Objective
- Understand the retail sales dataset.
- Identify sales and profit trends.
- Compare category, region, and customer segment performance.
- Analyze the relationship between discounts and profit.
- Create visualizations to communicate business insights.

## Dataset
- Dataset: Sample Superstore
- File: `Sample - Superstore.csv`
- Format: CSV

## Tools & Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy

## Analysis Performed
1. Data loading and inspection
2. Missing value and duplicate checks
3. Category-wise sales and profit analysis
4. Region-wise sales and profit analysis
5. Customer segment analysis
6. Monthly sales trend analysis
7. Discount and profit analysis
8. Correlation analysis
9. Hypothesis testing

## Visualizations
The following charts were created and saved in the `outputs` folder:

- `category_sales.png`
- `region_profit.png`
- `monthly_sales_trend.png`
- `discount_vs_profit.png`
- `correlation_heatmap.png`

## Project Structure
```text
CodeAlpha_EDA_Retail_Sales/
│
├── data/
│   └── Sample - Superstore.csv
│
├── outputs/
│   ├── category_sales.png
│   ├── region_profit.png
│   ├── monthly_sales_trend.png
│   ├── discount_vs_profit.png
│   └── correlation_heatmap.png
│
├── eda_analysis.py
└── README.md
```

## How to Run
1. Install the required libraries:
   `pip install pandas numpy matplotlib seaborn scipy`
2. Run the Python script:
   `python eda_analysis.py`

## Conclusion
This project uses exploratory data analysis and visualizations to identify patterns in retail sales and profitability. It also applies hypothesis testing to examine differences in profit across discount groups.

## Internship
Completed as part of the CodeAlpha Data Analytics Internship.