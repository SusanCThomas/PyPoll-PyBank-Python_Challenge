import os
import csv


budget_csv = os.path.join("Resources", "budget_data.csv")

month_list = []
profit_loss_list = []
total_months = 0

with open(budget_csv, 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    next(reader)
    
    for row in reader:
        total_months += 1
        profit_loss_list.append(int(row[1]))
print(total_months)
        

index = 0

for num in profit_loss_list:
    index = index + num

#total_profit_loss = sum(profit_loss_list)
print(index)



