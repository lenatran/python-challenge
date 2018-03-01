# Import necessary packages
import pandas as pd
import os

# Create path for csv file
budget1_path = os.path.join("/Users/lenatran/Desktop/UCBBEL201801DATA5-Class-Repository-DATA/03-Python/Homework/Instructions/PyBank/raw_data/","budget_data_1.csv")

# Read csv file
budget1_df = pd.read_csv(budget1_path)

# Calculate total number of months and revenue
total_months = budget1_df["Date"].nunique()
total_revenue = budget1_df["Revenue"].sum()

# Calculate average revenue change
last_revenue = budget1_df.iloc[-1:]["Revenue"].values[0]
avg_revenue_change = int(last_revenue/total_months)

# Shift column to calculate change in revenue
shifted_column = budget1_df["Revenue"].shift(1)
budget1_df["Revenue Shifted"] = shifted_column
revenue_change = budget1_df["Revenue"] - budget1_df["Revenue Shifted"]
budget1_df["Revenue Change"] = revenue_change

# Find greatest increase and decrease in revenue
# Find greatest increase
increase = int(budget1_df["Revenue Change"].max())
month_year = budget1_df.loc[budget1_df["Revenue Change"] == increase, "Date"].values[0]

# Find greatest decrease
decrease = int(budget1_df["Revenue Change"].min())
month_year2 = budget1_df.loc[budget1_df["Revenue Change"] == decrease, "Date"].values[0]


# Print out financial analysis
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(total_months))
print("Total Revenue: $" + str(total_revenue))
print("Average Revenue Change: $" + str(avg_revenue_change))
print("Greatest Increase in Revenue: " + str(month_year) + " ($" + str(increase) + ")")
print("Greatest Decrease in Revenue: " + str(month_year2) + " ($" + str(decrease) + ")")
 

# Write csv file
import csv

with open("budget1_analysis.csv", "w") as budget1:
    budget1_writer = csv.writer(budget1)
    
    budget1_writer.writerow(["Financial Analysis"])
    budget1_writer.writerow(["----------------------------"])
    budget1_writer.writerow(["Total Months: " + str(total_months)])
    budget1_writer.writerow(["Total Revenue: $" + str(total_revenue)])
    budget1_writer.writerow(["Average Revenue Change: $" + str(avg_revenue_change)])
    budget1_writer.writerow(["Greatest Increase in Revenue: " + str(month_year) + " ($" + str(increase) + ")"])
    budget1_writer.writerow(["Greatest Decrease in Revenue: " + str(month_year2) + " ($" + str(decrease) + ")"])