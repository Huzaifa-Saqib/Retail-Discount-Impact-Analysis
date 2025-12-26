# Discount Effectiveness Analysis

## Overview
This project analyzes the effectiveness of discount strategies in a retail dataset by evaluating how different discount levels impact sales, profit, profit margins, and customer behavior. Discounts were categorized into levels, aggregated, and analyzed to identify profitable and unprofitable discount practices. Results were exported to Excel for further analysis and visualization.

---

## Objectives
- Categorize discount percentages into meaningful discount levels  
- Analyze the impact of discounts on sales, profit, and profit margins  
- Examine customer order patterns across discount levels  
- Evaluate discount performance by product category  
- Identify optimal discount ranges for profitability  

---

## Data
- Retail transaction dataset (`store_data.csv`)  
- Includes customer purchases, sales revenue, profit, discounts, and product categories  
- Data was cleaned and unnecessary columns were removed to focus on discount-related analysis  

---

## Analysis & Approach
1. Loaded and cleaned the dataset using Python (pandas)  
2. Categorized discounts into five levels: Low, Low-Medium, Medium, Medium-High, and High  
3. Calculated profit margins for each transaction  
4. Aggregated metrics by discount level:
   - Total sales  
   - Total profit  
   - Average profit margin  
   - Number of customer orders  
5. Performed category-wise aggregation by discount level  
6. Exported cleaned and aggregated data to a multi-sheet Excel file  

---

## Key Findings
- High discounts resulted in **lower profits and reduced profit margins**  
- Low and Low-Medium discounts generated **significantly higher profits**  
- High discount levels attracted **fewer customers and fewer orders**  
- Low discount levels had **more customers and higher order volumes**  
- Discount effectiveness varied across product categories  

---

## Recommendations
- Limit the use of high discounts as they negatively impact profitability  
- Focus on low and low-medium discounts to maximize profit and customer volume  
- Apply discounts selectively based on product category performance  
- Regularly monitor discount-level performance to optimize pricing strategies  

---

## Tools Used
- **Python (pandas, numpy, xlsxwriter)** – data cleaning, analysis, and Excel export  
- **MS Excel** – reviewing and analyzing output data  
- **Power BI** for visualization
















**Huzaifa Saqib**
