import os
import csv

#File Path
election_csv = os.path.join("Resources", "election_data.csv")

voter_counts = []
candidate_list = []

#Read the CSV file
with open(election_csv, 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    next(reader)

    for row in reader:
        voter_counts.append(str(row[0]))
        

#Total Number of Votes Cast
total_votes = len(voter_counts)
print(total_votes)

#Complete_list of candidates who received votes




#Percentage of votes each candidate won
#Total number of votes each candidate won
#Winner of the election based on popular vote.