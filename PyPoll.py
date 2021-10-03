# The data we need to retrieve
# 1. The total number of votes case
# 2. A complete list of candidates who received votes
# 3. The percentage of the votes each candidate won
# 4. the total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Add our dependencies
import csv
import os
# assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")
# open the election results and read the file
with open(file_to_load) as election_data:
    #read the file object with the reader function
    file_reader = csv.reader(election_data)
    #print each row in the csv file
    headers = next(file_reader)
    print(headers)