import os
import csv

# Ensure the script's directory is the current working directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Setting up the path to the CSV file
csvpath = os.path.join("Resources", "budget_data.csv")

# Initializing variables
total_months = 0
total_profit_loss = 0
previous_profit_loss = None
changes = []
greatest_increase = -float('inf')  # Use negative infinity for initial comparison
greatest_decrease = float('inf')  # Use positive infinity for initial comparison
greatest_increase_month = ''
greatest_decrease_month = ''

# Open the CSV file
with open(csvpath, 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)  # Skip the header row

    for row in csvreader:
        # Update the count of total months
        total_months += 1
        current_profit_loss = int(row[1])
        total_profit_loss += current_profit_loss

        # Calculate change from previous month
        if previous_profit_loss is not None:
            change = current_profit_loss - previous_profit_loss
            changes.append(change)

            # Check for the greatest increase in profits
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_month = row[0]

            # Check for the greatest decrease in profits
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_month = row[0]

        # Update previous profit/loss for the next loop iteration
        previous_profit_loss = current_profit_loss

# Calculate average change
average_change = sum(changes) / len(changes) if changes else 0

# test/check results against assignment
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total Profit/Loss: ${total_profit_loss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# Prepare results to write to a file
results = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total Profit/Loss: ${total_profit_loss}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})
Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})
"""

# create path for output .txt file
output_path = os.path.join("analysis", "financial_analysis_results.txt")

# Write the results to a text file
with open(output_path, 'w') as file:
    file.write(results)
