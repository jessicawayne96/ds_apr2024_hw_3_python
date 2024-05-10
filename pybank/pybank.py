#read the csv file
#skip header row
#count column one
#sum column two
#create column 3 for changes in profit/losses
#average this new column
#find max of new column
#find min of new column

import os
import csv
csvpath = "resources/budget_data.csv"

#create list to store data
total_months = []
total_profit = []
profit_change = []

#open csv
with open(csvpath, encoding= 'UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # read the header row
    csv_header = next(csvreader)
    print(f"CSV Header : {csv_header}")

    # iterate through rows in sheet
    for row in csvreader:

        # append values to the lists, profit values need to be identified as integers
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    # find the profit change for each month, starting at month 2
    # change = month - (current month - 1)
    # append to the list & loop for sheet
    
    # Iterate through the profits in order to get the monthly change in profits
    for i in range(len(total_profit)-1):
        
        # Take the difference between two months and append to monthly profit change
        profit_change.append(total_profit[i+1]-total_profit[i])

    # find average of profit_change
    # find max & min of profit_change
        max_value = max(profit_change)
        min_value = min(profit_change)

    # Correlate max and min to the proper month using month list and index from max and min
    # We use the plus 1 at the end since month associated with change is the + 1 month or next month
    increase_month = profit_change.index(max(profit_change)) + 1
    decrease_month = profit_change.index(min(profit_change)) + 1 

    # define variables to print
tot_months = len(total_months)
average_change = round(sum(profit_change)/len(profit_change),2)

    # print our financial analysis
print("Financial Analysis")
print("-------------------------------------")
print(f"Total Months: {tot_months}")
print(f"Total: ${sum (total_profit)}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {total_months[increase_month]} ${max_value}")
print(f"Greatest Increase in Profits: {total_months[decrease_month]} ${min_value}")

# Write financial analysis to text file
output_file = "output.txt"

with open(output_file, "w") as output:
    output.write("Financial Analysis\n")
    output.write("-------------------------------------\n")
    output.write(f"Total Months: {tot_months}\n")
    output.write(f"Total: ${sum(total_profit)}\n")
    output.write(f"Average Change: ${average_change}\n")
    output.write(f"Greatest Increase in Profits: {total_months[increase_month]} (${max_value})\n")
    output.write(f"Greatest Decrease in Profits: {total_months[decrease_month]} (${min_value})\n")

print(f"Financial analysis has been saved to {output_file}")


    
