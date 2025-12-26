import pandas as pd
import numpy as np

df = pd.read_csv("store_data.csv")
print(df.isnull().sum())
print(df["Discount"].unique())

df = df.drop(columns=["Row ID" , "Ship Mode" , "Order Date" , "Ship Date" , "Order ID" , "Segment" , "Postal Code" , "Region" , "Sub-Category"])
df = df.rename(columns={"Category" : "Product Category"})
print(df)

def categorize_discount(Discount):
    if Discount <= 0.1:
       return "Low"
    elif Discount <= 0.25:
       return "Low-medium"
    elif Discount <= 0.4:
       return "Medium"
    elif Discount <= 0.6:
       return "Medium-high"
    elif Discount <= 0.75:
       return "High"
    
df["Discount Level"] = df["Discount"].apply(categorize_discount)
print(df)

print(df["Discount Level"].value_counts())


df["Profit Margin"] = ((df["Profit"] / df["Sales"])*100).round(0).astype(int)


df_agg = df.groupby("Discount Level").agg(
    Total_Sales=pd.NamedAgg(column="Sales", aggfunc="sum"),
    Total_Profit=pd.NamedAgg(column="Profit", aggfunc="sum"),
    Avg_Profit_Margin=pd.NamedAgg(column="Profit Margin", aggfunc="mean"),
    Count_Orders=pd.NamedAgg(column="Customer ID", aggfunc="count"),
).reset_index()
df_agg["Avg_Profit_Margin"] = df_agg["Avg_Profit_Margin"].round(0).astype(int)
print(df_agg)


df_agg_category = df.groupby(["Product Category", "Discount Level"]).agg(
    Total_Sales=pd.NamedAgg(column="Sales", aggfunc="sum"),
    Total_Profit=pd.NamedAgg(column="Profit", aggfunc="sum"),
    Count_Orders=pd.NamedAgg(column="Customer ID", aggfunc="count"),
).reset_index()
print(df_agg_category)

with pd.ExcelWriter("Customer_Discount_Analysis.xlsx", engine="xlsxwriter") as writer:
    df.to_excel(writer, sheet_name="Raw_Data", index=False)
    df_agg.to_excel(writer, sheet_name="Discount_Aggregation", index=False)
    df_agg_category.to_excel(writer, sheet_name="Category_Aggregation", index=False)

print("Excel file created")