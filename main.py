# PyBank Activity

# First import the os model
import os

# import module for reading CSV files
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')
# print(csvpath)

print("Financial Analysis")
print("----------------------------")

# improve reading of csv - not working?
with open(csvpath, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds content
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)

    # Read the header row first
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    
    # declare variables
    i = 0 
    months = 0
    changes = []
    change_count = 0
    total = 0
    greatest_increase = 0
    greatest_decrease = 0
    date_greatest_increase = None
    date_greatest_decrease = None
    
    # Read each row of data after the header
    for row in csvreader:
        
        # The total number of months included in the dataset
        if i == 0:
            lastmonth = str(row[1])
            i += 1

        else:

            # Calculate the changes in "Profit/Losses" over the entire period,
            change = (row[1]-str(lastmonth))
            print(change)

            lastmonth = row[1]
            print(lastmonth)

            changes.append(change)
            change_count += 1
            # print(change_count)

            # then find the average of those changes
            # ???
          
        # The greatest increase in profits (date and amount) over the entire period
        if change > greatest_increase:
            greatest_increase = change
            date_greatest_increase = row[0]
        # The greatest decrease in profits (date and amount) over the entire period`
        if change < greatest_decrease:
            greatest_decrease = change
            date_greatest_decrease = row[0]
          
    # The net total amount of "Profit/Losses" over the entire period create variable to use as accumulator
    total += row[1]
 

# print to terminal
print("Total Months: " + str(change_count + 1))
print("Total: " + str(change))
print("Average Change: $" + str(change))
print("Greatest Increase in Profits: " + str(date_greatest_increase) + "($" + greatest_increase + ")")
print("Greatest Decrease in Profits: " + str(date_greatest_decrease) + "($" + greatest_decrease + ")")

# export a text file with the results.
output_path = os.path.join("analysis", "results.csv")
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimeter=',')
