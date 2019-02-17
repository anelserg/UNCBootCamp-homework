# First we'll import the os module
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('.', 'budget_data.csv')

#Reading using CSV module

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    budgetCsvReader = csv.reader(csvfile, delimiter=',')

    print(budgetCsvReader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(budgetCsvReader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    #for row in csvreader:
        #print(row)
