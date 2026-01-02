import pandas as pd
import datetime as dt
pf = pd.read_csv("employees.csv")

print("Employee Data:")
print(pf)
print("\nAverage Salary:", pf["Salary"].mean())
dept_avg = pf.groupby("Department")["Salary"].mean()
print("\nDepartment-wise Average Salary:")
print(dept_avg)
highest = pf.loc[df["Salary"].idxmax()]
print("\nHighest Paid Employee:")
print(highest)
lowest = pf.loc[df["Salary"].idxmin()]
print("\nLowest Paid Employee:")
print(lowest)
df.to_csv("employee_report.csv", index=False)