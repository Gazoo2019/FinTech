# -*- coding: UTF-8 -*-
"""PyRamen Homework Solution."""

import csv
from pathlib import Path
from utils import sum_field, avg_field, min_field, max_field


# Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path("Resources/menu_data.csv")
sales_filepath = Path("Resources/sales_data.csv")


# Initialize list object to hold our menu data
menu = []

# Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# item,category,description,price,cost
# Read in the menu data into the menu list
with open(menu_filepath) as menu_file:
    reader = csv.reader(menu_file)

    # Skip header of menu data
    next(reader)

    for row in reader:
        menu.append(row)


# Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
# Open the csv file and load it in as a csv.reader object
with open(sales_filepath) as csvfile:
    reader = csv.reader(csvfile, delimiter=",")

    # Skip header of sales data
    next(reader)

    row_count = 0

    # Loop over every row in the csv file
    for row in reader:
        print()
        print(row)

        # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
        # Initialize sales data variables
        line_item_id = row[0]
        date = row[1]
        cc_number = row[2]
        quantity = int(row[3])
        sales_item = row[4]

        # If the item value not in the report, add it as a new entry with initialized metrics
        # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit
        if sales_item not in report.keys():
            report[sales_item] = {
                "01-count": 0,
                "02-revenue": 0,
                "03-cogs": 0,
                "04-profit": 0,
            }

        # For every row in our sales data, loop over the menu records to determine a match
        for record in menu:

            # Item,Category,Description,Price,Cost
            # Initialize menu data variables

            item = record[0]
            category = record[1]
            description = record[2]
            price = float(record[3])
            cost = float(record[4])
            profit = price - cost

            # If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item
            if sales_item == item:

                # Print out matching menu data
                print(f"Does {sales_item} equal {item}? WE HAVE A MATCH!!!")
                print(f"   Item: {item}")
                print(f"   Category: {category}")
                print(f"   Price: ${price}")
                print(f"   Cost: ${cost}")
                print(f"   Profit: ${profit}")

                # Cumulatively add up the metrics for each item key
                report[sales_item]["01-count"] += quantity
                report[sales_item]["02-revenue"] += price * quantity
                report[sales_item]["03-cogs"] += cost * quantity
                report[sales_item]["04-profit"] += profit * quantity

            else:
                print("Does", sales_item, "equal", record[0], "? WA WA, NO MATCH")

        row_count += 1

# Print total number of records in sales data
print()
print("Total Number of Records:", row_count)
print()

# Let's visualize the report so far
for key, value in report.items():
    print(key, value)
print()  # Adds a space between the end of the program and the console input

# Find items that are performing above or below the average profitability
under_performing = []
over_performing = []

for item in report:

    if report[item]["04-profit"] < avg_field(report, "04-profit"):

        under_performing.append(item)

    elif report[item]["04-profit"] > avg_field(report, "04-profit"):

        over_performing.append(item)

# Write out report to a text file (won't appear on the command line output)
with open("report.txt", "w") as txt_file:
    txt_file.write("Ramen Analysis Report\n")
    txt_file.write("-----------------------------\n")
    txt_file.write("Summary Statistics:\n")
    txt_file.write("\n")
    txt_file.write(f"Total Number of Ramen Sold: {format(sum_field(report, '01-count'), ',')} bowls\n")
    txt_file.write(f"Total Revenue Generated: ${format(sum_field(report, '02-revenue'), ',')}\n")
    txt_file.write(f"Total Cost of Goods Sold: ${format(sum_field(report, '03-cogs'), ',')}\n")
    txt_file.write(f"Net Profit Generated: ${format(sum_field(report, '04-profit'), ',')}\n")
    txt_file.write("\n")
    txt_file.write("Average Statistics:\n")
    txt_file.write("\n")
    txt_file.write(f"Number of Ramen Types: {len(report.keys())}\n")
    txt_file.write(f"Average Number Sold per Ramen Type: {format(avg_field(report, '01-count'), ',')} bowls\n")
    txt_file.write(f"Average Revenue Generated per Ramen Type: ${format(avg_field(report, '02-revenue'), ',')}\n")
    txt_file.write(f"Average Cost of Goods Sold per Ramen Type: ${format(avg_field(report, '03-cogs'), ',')}\n")
    txt_file.write(f"Average Net Profit Generated per Ramen Type: ${format(avg_field(report, '04-profit'), ',')}\n")
    txt_file.write("\n")
    txt_file.write("Min/Max Statistics:\n")
    txt_file.write("\n")
    txt_file.write(f"Most Popular: {max_field(report, '01-count')}\n")
    txt_file.write(f"Least Popular: {min_field(report, '01-count')}\n")
    txt_file.write(f"Most Revenue Generating: {max_field(report, '02-revenue')}\n")
    txt_file.write(f"Least Revenue Generating: {min_field(report, '02-revenue')}\n")
    txt_file.write(f"Most Costly: {max_field(report, '03-cogs')}\n")
    txt_file.write(f"Least Costly: {min_field(report, '03-cogs')}\n")
    txt_file.write(f"Most Profitable: {max_field(report, '04-profit')}\n")
    txt_file.write(f"Least Profitable: {min_field(report, '04-profit')}\n")
    txt_file.write("\n")
    txt_file.write("Filter Items:\n")
    txt_file.write("\n")
    txt_file.write(f"Overperforming Items: {over_performing}\n")
    txt_file.write(f"Underperforming Items: {under_performing}\n")
    txt_file.write("\n")