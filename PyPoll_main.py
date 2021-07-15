# PyPoll

import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Print to terminal
    print("Election Results")
    print("-------------------------")

    # declare variables
    i = 0
    res = 0
    total_votes = 0
    Khan_votes = 0
    Correy_votes = 0
    Li_votes = 0
    O_Tooley_votes = 0
    winner = None

    # A complete list of candidates who received votes
    candidates_list = [
        "Khan",
        "Correy",
        "Li",
        "O'Tooley"]
    # print(candidates_list)

    # read row by row
    for row in csvreader:
        data = list(csvreader)
        total_votes = len(data)
        print("Total Votes: " + str(total_votes))
        print("-------------------------")

        # Using loop
        # Selective key values in dictionary
        res = 0
        for key in candidates_list:
            if candidates_list[key] == "Khan":
                res = res + 1

# The total number of votes each candidate won

# The percentage of votes each candidate won

# The winner of the election based on popular vote.

# print("-------------------------")
# print("Khan: " + (Khan_votes/total_votes) + "% (" + Khan_votes + ")")
# print("Correy: " + (Correy_votes/total_votes) + "% (" + Correy_votes + ")")
# print("Li: " + (Li_votes/total_votes) + "% (" + Li_votes + ")")
# print("O'Tooley: " + (O_Tooley_votes/total_votes) + "% (" + O_Tooley_votes + ")")
# print("-------------------------")
# print("Winner: " + winner)
# print("-------------------------")

# export text file with results
# output_path = os.path.join("analysis", "results.csv")
# with open(output_path, 'w', newline='') as csvfile:
    # csvwriter = csv.writer(csvfile, delimeter=',')"""
