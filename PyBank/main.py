import os
import csv

#File Path
budget_csv = os.path.join("Resources", "budget_data.csv")

profit_loss_list = []
months_list = []

#Read the CSV File
with open(budget_csv, 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    next(reader)

    for row in reader:
        months_list.append(str(row[0]))
        profit_loss_list.append(int(row[1]))

#Total Number of Months included in Data Set
total_months = len(months_list)
# print(total_months)

#Net Total Amount of "Profits/Losses" over the entire period
total = 0

for num in profit_loss_list:
    total = total + num

# print(total)

#Average of the changes in "Profit/Losses" over the entire period
average_change = []
prior_month = 0

for x in range(len(profit_loss_list)):
    if x==0:
        prior_month = profit_loss_list[x]
    else:
        monthly_change = profit_loss_list[x] - prior_month
        average_change.append(monthly_change)
        prior_month = profit_loss_list[x]

# print(average_change)

revenue_average = sum(average_change) / len(average_change)

# print(revenue_average)
y = round(revenue_average, 2)
# print(y)


#Greatest increase in profits (date and amount) over the entire period
#Greatest decrease in losses (date and amount) over the entire period

greatest_increase = 0
greatest_increase_month = ','
greatest_decrease = 0
greatest_decrease_month = ','

for x in range(len(average_change)):
    if average_change[x] > greatest_increase:
        greatest_increase = average_change[x]
        greatest_increase_month = months_list[x+1]
    elif average_change[x] < greatest_decrease:
        greatest_decrease = average_change[x]
        greatest_decrease_month = months_list[x+1]

# print(str(greatest_increase_month) + str(greatest_increase))
# print(str(greatest_decrease_month) + str(greatest_decrease))

# Financial Summary

print('Financial Analysis')
print('------------------')
print('Total Months:' + " " + str(total_months))
print("Total:" + " " + "$" + str(total) + "")
print('Average Change:' + " " + "$" + str(y)+ "")
print('Greatest Increase in Profits:' + " " + str(greatest_increase_month) + " " +
 "($" + str(greatest_increase) + ")")
print('Greatest Decrease in Profits:' + " " + str(greatest_decrease_month) + " " +
 "($" + str(greatest_decrease) + ")")

# Export Text File 
pybank_analysis = os.path.join("analysis", "financial.txt")

with open(pybank_analysis, 'w') as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("------------------------------\n")
    txt_file.write('Total Months:' + " " + str(total_months) + "\n")
    txt_file.write("Total:" + " " + "$" + str(total) + "" + "\n")
    txt_file.write('Average Change:' + " " + "$" + str(y)+ "" + "\n")
    txt_file.write('Greatest Increase in Profits:' + " " + str(greatest_increase_month) + " " +
    "($" + str(greatest_increase) + ")" + "\n")
    txt_file.write('Greatest Decrease in Profits:' + " " + str(greatest_decrease_month) + " " +
    "($" + str(greatest_decrease) + ")" + "\n")


    