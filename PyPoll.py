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

# 1. Initialize a total vote counter
total_votes = 0

# create list for candidate name
candidate_options = []

#declare empty dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# open the election results and read the file
with open(file_to_load) as election_data:
    #read the file object with the reader function
    file_reader = csv.reader(election_data)
    #print each row in the csv file
    headers = next(file_reader)
    for row in file_reader:
        # 2. Add to the total vote count
        total_votes += 1
        #print candidate name for each row
        candidate_name = row[2]
        #add candidate name to the candidate list
        if candidate_name not in candidate_options:
            #add the candidate name to candidate list
            candidate_options.append(candidate_name)
            #begin tracking the candidates vote count
            candidate_votes[candidate_name] = 0
        #add a vote to that candidates count
        candidate_votes[candidate_name] += 1
#save results to our txt file
with open(file_to_save, "w") as txt_file:
    #print final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------\n")
    print(election_results, end="")
    #save the final vote count to the txt file
    txt_file.write(election_results)
        
    #Determine the percentage of votes for each candidate by looping through the counts
    # 1. iterate through the candidate list
    for candidate_name in candidate_votes:
        # 2. retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # 3. calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        #print out each candidates name, vote count, and percentage of vote to terminal
        print(candidate_results)
        #save candidate results to our txt file
        txt_file.write(candidate_results)

        #determine winning vote count and candidate
        #determine if the votes is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # if true then set winning_count = votes and winning_percentage = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #and, set the winning_candidate equal to the candidates name
            winning_candidate = candidate_name

    # print out the winning candidate, vote count, and percentage of vote to terminal
    winning_candidate_summary = (
        f"----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------\n")
    print(winning_candidate_summary)
    #save winning candidates results to txt file
    txt_file.write(winning_candidate_summary)