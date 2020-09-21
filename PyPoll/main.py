import os
import csv

#File Path
election_csv = os.path.join("Resources", "election_data.csv")

voterID_list = []
county_list = []
candidate_list = []

#Read the CSV file
with open(election_csv, 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    next(reader)

    for row in reader:
        voterID_list.append(str(row[0]))
        county_list.append(str(row[1]))
        candidate_list.append(str(row[2]))

#Total Number of Votes Cast
total_votes = len(voterID_list)
print(total_votes)

#Complete_list of candidates who received votes
candidate = line[2]

#Percentage of votes each candidate won
#Total number of votes each candidate won
#Winner of the election based on popular vote.