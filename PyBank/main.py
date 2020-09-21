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
#Total Number of Months included in data set
total_months = len(months_list)
print(total_months)
        

#Net Total Amount of "Profit/Losses"
# index = 0

# for num in profit_loss_list:
#     index = index + num

# total_profit_loss = sum(profit_loss_list)
#print(index)


#The Average Profit/Loss
# average_revenue_list = []
# prior_month = 0

# for x in range(len(profit_loss_list)):
#     if x == 0:
#         prior_month = profit_loss_list[x]
#     else:
#         monthly_change = profit_loss_list[x] - prior_month
#         average_revenue_list.append(monthly_change)
#         prior_month = profit_loss_list[x]

#print(average_profit_loss_list)

# revenue_average = sum(average_revenue_list) / len(average_revenue_list)
#print(revenue_average)

#Calculate the greatest increase in profits (date and amount)
#Calculate the greatest decrease in losses (date and amount)
# greatest_increase = 0
# greatest_increase_month = ''
# greatest_decrease = 0
# greatest_decrease_month = ''


# for x in range(len(average_revenue_list)):
#     if average_revenue_list[x] > greatest_increase:
#         greatest_increase = average_revenue_list[x]
#         greastest_increase_month = months_list[x+1]
#     elif average_revenue_list[x] < greatest_decrease:
#         greatest_decrease = average_revenue_list[x]
#         greastest_decrease_month = months_list[x+1]

#Print Analysis and create text file
print('Financial Analysis'),
print('------------------'),
print('Total Months:' + str(total_months)

# print('Net Total Amount of Profits/Losses:' + str(index)),
# print('Average Revenue Change:' + str(revenue_average)),
# print('Greatest Increase in Profit:' + (greastest_increase_month) + "($" + (greatest_increase)),
# print('Greatest Decrease in Losses:' + (greastest_decrease_month) + "($" + (greatest_decrease))


# with open('Analysis/budget.txt, 'w') as file:
#     f.write()