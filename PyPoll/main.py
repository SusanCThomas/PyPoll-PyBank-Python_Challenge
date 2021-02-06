# Imprting Dependencies
import os
import csv

#File Path
election_csv = os.path.join("Resources", "election_data.csv")

Voter_ID = []
Candidate_List = []
Votes = {}
number_of_votes = 0

#Read the CSV file
with open(election_csv, 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_file)

# Conditions
    for row in reader:
        Voter_ID.append(row[0])
        Candidate = row[2]
        if Candidate not in Candidate_List:
            Candidate_List.append(Candidate)
            Votes[Candidate] = 1
        else:
            Votes[Candidate] += 1

    Total_Candidates = len(Candidate_List)
    Total_Voters = len(Voter_ID)
    Most_Votes = sorted(Votes)
        

# Election Result Summary

print('Election Results')
print('------------------------')
print('Total Votes:' + str(Total_Voters))
print('------------------------')
for Runner in Candidate_List:
    print(f"{Runner}: {round(Votes[Runner] * 100 / (Total_Voters), 3)}% ({Votes[Runner]})")
print('------------------------')
print('Winner:' + str(Most_Votes[1]))
print('------------------------')

# Export Text File 
pypoll_analysis = os.path.join("analysis", "election_results.txt")

with open(pypoll_analysis, 'w') as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("------------------------------\n")
    txt_file.write('Total Votes:' + str(Total_Voters) + "\n")
    txt_file.write("------------------------------\n")
    for Runner in Candidate_List:
        txt_file.write(f"{Runner}: {round(Votes[Runner] * 100 / (Total_Voters), 3)}% ({Votes[Runner]})" + "\n")
    
    txt_file.write("------------------------------\n")
    txt_file.write(('Winner:' + str(Most_Votes[1])) + "\n")
    txt_file.write("------------------------------\n")