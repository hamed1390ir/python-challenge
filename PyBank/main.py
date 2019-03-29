import csv
import os
print(os.getcwd())
# Store the file path associated with the file
file = 'budget_data.csv'

# Open the file in "read" mode ('r') and store the contents in the variable "budget_data"
with open(file, 'r') as budget_data:
    next(budget_data)
    csv_reader = csv.reader(budget_data, delimiter = ',')

    total = 0
    total_months = 0
    current = 0
    changes = []
    for row in csv_reader:
        change = int(row[1]) - current
        changes.append(change)
        total_months = total_months + 1
        total = total + int(row[1])
        current = int(row[1])

    changes = changes[1:len(changes)]

    average_change = sum(changes)/(total_months-1)
    greatest_increase_amount = max(changes)
    greatest_decrease_amount = min(changes)


    print('Financial Analysis')
    print('----------------------------')
    print(f"Total Months: {total_months}")
    print(f"Total: ${total}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_amount})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_amount})")

