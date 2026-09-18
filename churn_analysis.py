import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Dataset Load Cheyadam
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

# 2. Data Cleaning
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df.dropna(inplace=True)

# 3. Graph 1: Churn Count Chart
plt.figure(figsize=(6, 4))
sns.countplot(x="Churn", data=df, palette="coolwarm")
plt.title("Overall Customer Churn Count")
plt.xlabel("Customer Churned?")
plt.ylabel("Count")
plt.savefig("churn_count.png")
plt.show()

# 4. Graph 2: Tenure vs Churn Chart
plt.figure(figsize=(8, 5))
sns.boxplot(x="Churn", y="tenure", data=df)
plt.title("Customer Tenure vs Churn Rate")
plt.savefig("tenure_vs_churn.png")
plt.show()