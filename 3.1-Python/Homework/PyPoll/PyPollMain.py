# First we'll import the os module
import os

# Module for reading CSV files
import csv

#importing operator library
import operator

csvpath = os.path.join('.', 'election_data.csv')

#Reading using CSV module

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    electionCsvReader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(electionCsvReader)
    print(f"CSV Header: {csv_header}")

    # setting variables to 0 and initiating and empty list and mepty dictionary
    totalVotes = 0
    candidatesDict = {}
    # starting a for loop to read in the csv file
    for row in electionCsvReader:
        #total number of votes in the dataset
        totalVotes = totalVotes + 1

        #saving the row[2] to a variable
        candidateName = row[2]

        # Adding candidates names to a list
        if candidateName not in candidatesDict:
            candidatesDict[candidateName] = 1
        else:
        	candidatesDict[candidateName] += 1
    
    # getting the election winner using the operator library and a max function
    winner = max(candidatesDict.items(), key=operator.itemgetter(1))[0]
    print(winner)



    # printing out the output    
    print("Election Results")
    print(" ")
    print("-----------------------------")
    print("  ")
    print("Total Votes: " + str(totalVotes))
    print(" ")
    print("-----------------------------")
    print(" ")
    for name, count in candidatesDict.items():
    	print(name + ": " + "{0:.3f}".format(count/totalVotes * 100) + "% (" + str(count) + ")")
    print("  ")
    print("-----------------------------")
    print("   ")
    print("Winner: " + winner) 
    print("  ")
    print("-----------------------------")   

### starting the code to write to a txt file
# Specify the file to write to
output_path = os.path.join(".", "PollWriter.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as fw:

    # Write to the text file
    fw.write("Election Results\n")

    fw.write(' \n')

    fw.write('-----------------------------\n')

    fw.write(' \n')

    fw.write("Total Votes: " + str(totalVotes)+'\n')

    fw.write(' \n')

    fw.write('-----------------------------\n')

    fw.write(' \n')

    for name, count in candidatesDict.items():
    	fw.write(name + ": " + "{0:.3f}".format(count/totalVotes * 100) + "% (" + str(count) + ")\n")

    fw.write(' \n')

    fw.write('-----------------------------\n')

    fw.write(' \n')

    fw.write("Winner: " + winner+'\n')

    fw.write(' \n')
    
    fw.write('-----------------------------\n')
