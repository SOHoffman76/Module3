import os
import csv

# Ensure the script's directory is the current working directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Setting up the path to the CSV file
csvpath = os.path.join("Resources", "election_data.csv")

# Initializing variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Open the CSV file
with open(csvpath, 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)  # Skip the header row

# for loop to count votes
    for row in csvreader:
        # Count each vote
        total_votes += 1
        candidate_name = row[2]

        # If the candidate is in the dictionary, increment their vote count
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

# Determine the winner/prep output
results = "Election Results\n" 
# +=: variable = variable + value - or - variable += value
results += "----------------------------\n"
results += f"Total Votes: {total_votes}\n"
results += "----------------------------\n"

for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    results += f"{candidate}: {percentage:.3f}% ({votes})\n"
    if votes > winner_votes:
        winner_votes = votes
        winner = candidate

results += "----------------------------\n"
results += f"Winner: {winner}\n"
results += "----------------------------\n"

# test/check results against assignment
print(results)

# create path for output .txt file
output_path = os.path.join("analysis", "election_results.txt")

# write results to a .txt file
with open(output_path, 'w') as file:
    file.write(results)
