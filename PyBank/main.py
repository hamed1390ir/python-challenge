import csv

# Store the file path associated with the file
file = 'budget_data.csv'

# Open the file in "read" mode ('r') and store the contents in the variable "budget_data"
with open(file, 'r') as budget_data:
    next(budget_data)
    csv_reader = csv.reader(budget_data, delimiter = ',')

    total = 0
    total_months = 0

    for row in csv_reader:
        total_months = total_months + 1
        total = total + int(row[1])

with open(file, 'r') as budget_data:
    next(budget_data)
    csv_reader = csv.reader(budget_data, delimiter=',')

    current = 0
    changes = []
    changes_month = []
    for row in csv_reader:
        change = int(row[1]) - current
        changes.append(change)
        changes_month.append(row[0])
        current = int(row[1])

changes = changes[1:len(changes)]
changes_month = changes_month[1:len(changes_month)]

max_change = changes[0]
max_change_month = changes_month[0]

for i in range(len(changes)):
    if changes[i] > max_change:
        max_change = changes[i]
        max_change_month = changes_month[i]

min_change = changes[0]
min_change_month = changes_month[0]

for i in range(len(changes)):
    if changes[i] < min_change:
        min_change = changes[i]
        min_change_month = changes_month[i]


average_change = sum(changes) / (total_months - 1)


output = (f"\nFinancial Analysis\n"
      f"----------------------------\n"
      f"Total Months: {total_months}\n"
      f"Total Revenue: ${total}\n"
      f"Average Revenue Change: ${average_change}\n"
      f"Greatest Increase in Revenue: {max_change_month} (${max_change})\n"
      f"Greatest Decrease in Revenue: {min_change_month} (${min_change})\n"
      )
print(output)
with open("Output.txt", "w") as text_file:
    text_file.write(output)