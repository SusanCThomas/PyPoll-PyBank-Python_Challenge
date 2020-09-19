import os
import csv


budget_csv = os.path.join("Resources", "budget_data.csv")

month_list = []
profit_loss_list = []

with open(budget_csv, 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    next(reader)
    
    for row in reader:
        month_list.append(str(row[0]))
        profit_loss_list.append(int(row[1]))

total_months = len(month_list)
#print(total_months)

index = 0

for num in profit_loss_list:
    index = index + num

#net_profit = sum(profit_loss_list)
#print(index)
