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

    #print(electionCsvReader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(electionCsvReader)
    print(f"CSV Header: {csv_header}")

    # setting variables to 0 and initiating and empty list and mepty dictionary
    totalVotes = 0
    candidateNameList = []
    candVotesPercCnt = {}
    KhanCount = 0
    CorreyCount = 0
    LiCount = 0
    OTooleyCount = 0


    # starting a for loop to read in the csv file
    for row in electionCsvReader:
        #total number of votes in the dataset
        totalVotes = totalVotes + 1

        # Adding candidates names to a list
        if row[2] not in candidateNameList:
            candidateNameList.append(row[2])

        # creating an if conditional to get the count and percentage for each candidate 
        # and adding them to a dictionary as the value list for the candidate name as the key
        if row[2] == 'Khan':
            KhanCount = KhanCount + 1
            KhanPercentage = KhanCount / totalVotes * 100
            candVotesPercCnt['Khan'] = (KhanPercentage, KhanCount)
        elif row[2] == 'Correy':
            CorreyCount = CorreyCount + 1
            CorreyPercentage = CorreyCount / totalVotes * 100
            candVotesPercCnt['Correy'] = (CorreyPercentage, CorreyCount)
        elif row[2] == 'Li':
            LiCount = LiCount + 1
            LiPercentage = LiCount / totalVotes * 100
            candVotesPercCnt['Li'] = (LiPercentage, LiCount)
        elif row[2] == "O'Tooley":
            OTooleyCount = OTooleyCount + 1
            OTooleyPercentage = OTooleyCount / totalVotes * 100
            candVotesPercCnt["O'Tooley"] = (OTooleyPercentage, OTooleyCount)
        
    # getting the election winner using the operator library and a max function
    winner = max(candVotesPercCnt.items(), key=operator.itemgetter(1))
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
    print("Khan: " + str(candVotesPercCnt['Khan'][0]) + "% " + "(" + str(candVotesPercCnt['Khan'][1]) + ")")
    print("Correy: " + str(candVotesPercCnt['Correy'][0]) + "% " + "(" + str(candVotesPercCnt['Correy'][1]) + ")")
    print("Li: " + str(candVotesPercCnt['Li'][0]) + "% " + "(" + str(candVotesPercCnt['Li'][1]) + ")")
    print("O'Tooley: " + str(candVotesPercCnt["O'Tooley"][0]) + "% " + "(" + str(candVotesPercCnt["O'Tooley"][1]) + ")")
    print("  ")
    print("-----------------------------")
    print("   ")
    print("Winner: " + winner[0]) 
    print("  ")
    print("-----------------------------")   

### starting the code to write to a txt file
# Specify the file to write to
output_path = os.path.join(".", "PollWriter.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as fw:

    # Initialize csv.writer
    # pollCsvWriter = csv.writer(csvWfile, delimiter=',')

    # Write the first row (column headers)
    fw.write("Election Results\n")

    # Write the second row
    fw.write(' \n')

    # Write the third row
    fw.write('-----------------------------\n')

    # Write the fourth row
    fw.write(' \n')

    # Write the fifth row
    fw.write("Total Votes: " + str(totalVotes)+'\n')

    # Write the sixth row
    fw.write(' ')

    # Write the seventh row
    fw.write('-----------------------------\n')

    # Write the eight row
    fw.write(' \n')

    # Write the ninth row
    fw.write("Khan: " + str(candVotesPercCnt['Khan'][0]) + "% " + "(" + str(candVotesPercCnt['Khan'][1]) + ")"+'\n')

    # Write the tenth row
    fw.write("Correy: " + str(candVotesPercCnt['Correy'][0]) + "% " + "(" + str(candVotesPercCnt['Correy'][1]) + ")"+'\n')

    # Write the eleventh row
    fw.write("Li: " + str(candVotesPercCnt['Li'][0]) + "% " + "(" + str(candVotesPercCnt['Li'][1]) + ")"+'\n')

    # Write the twelveth row
    fw.write("O'Tooley: " + str(candVotesPercCnt["O'Tooley"][0]) + "% " + "(" + str(candVotesPercCnt["O'Tooley"][1]) + ")"+'\n')

    # Write the thirteenth row
    fw.write(' \n')

    # Write the fourteenth row
    fw.write('-----------------------------\n')

    # Write the fifteenth row
    fw.write(' \n')

    # Write the sixteenth row
    fw.write("Winner: " + winner[0]+'\n')

    # Write the seventeenth row
    fw.write(' \n')
    
    # Write the eighteenth row
    fw.write('-----------------------------\n')
