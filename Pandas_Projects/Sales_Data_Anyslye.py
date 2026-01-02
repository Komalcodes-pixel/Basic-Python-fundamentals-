import pandas as pd

d = pd.read_csv("sales.csv")
# Convert Date column
d["Date"] = pd.to_datetime(d["Date"])
d["Revenue"] = d["Quantity"] * d["Price"]
print("Sales Data:")
print(d)
total_revenue = d["Revenue"].sum()
print("\nTotal Revenue:", total_revenue)

d["Month"] = d["Date"].dt.month
monthly_sales = d.groupby("Month")["Revenue"].sum()
print("\nMonthly Sales:")
print(monthly_sales)
top_product = d.groupby("Product")["Quantity"].sum().idxmax()
print("\nHighest Selling Product:", top_product)
#Product-wise Revenue
product_revenue = df.groupby("Product")["Revenue"].sum()
print("\nProduct-wise Revenue:")
print(product_revenue)
# Save report
df.to_csv("sales_report.csv", index=False)
print("\nSales report saved to sales_report.csv")
