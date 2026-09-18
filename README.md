# Telecom Customer Churn Analysis

## Project Overview
This project performs an Exploratory Data Analysis (EDA) on telecom customer data to identify key factors influencing customer churn. Using Python data science libraries, the analysis visualizes churn trends based on contract types, tenure, and monthly charges to support data-driven customer retention strategies.

## Key Features
- **Data Preprocessing & Cleaning:** Handled missing values and standardized data types using Pandas.
- **Exploratory Data Analysis (EDA):** Calculated statistical insights on churn distributions.
- **Data Visualization:** Built visual plots using Matplotlib and Seaborn to map tenure vs. churn rates.

## Tech Stack
- **Language:** Python
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn
- **Tools:** VS Code, Git/GitHub

## Key Insights
1. **Tenure Effect:** Customers with shorter tenure (less than 12 months) show significantly higher churn rates.
2. **Contract Impact:** Month-to-month contract holders churn more frequently compared to two-year contract users.

## Project Structure
* `WA_Fn-UseC_-Telco-Customer-Churn.csv` - Raw Customer Dataset
* `churn_analysis.py` - Main Python Script for Data Processing
* `churn_count.png` - Output Chart for Total Churn Count
* `tenure_vs_churn.png` - Output Chart for Tenure Analysis
* `README.md` - Project Documentation